# -*- coding: utf-8 -*-
# @Time : 2020/12/26 21:56
# @Author : CHT
# @Site : 
# @File : train.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:

from torch import nn
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
import numpy as np

cuda = True if torch.cuda.is_available() else False
FloatTensor = torch.cuda.FloatTensor if cuda else torch.FloatTensor
LongTensor = torch.cuda.LongTensor if cuda else torch.LongTensor

def evaluate(net, dataloader_src, dataloader_tgt, alpha):
    """Evaluation for target encoder by source classifier on target dataset."""
    # set eval state for Dropout and BN layers
    net.eval()

    # init loss and accuracy
    loss_src = loss_tgt = 0
    acc_src = acc_tgt = 0

    # set loss function
    criterion = nn.CrossEntropyLoss()

    # evaluate network
    for (images, labels) in dataloader_src:
        images = Variable(images.type(FloatTensor)).reshape(images.shape[0], -1)
        labels = Variable(labels.type(LongTensor))

        # preds = classifier(encoder(images, labels))
        preds, _ = net(x=images, alpha=alpha)
        # loss += criterion(preds, labels).data[0]
        loss_src += criterion(preds, labels).item()

        pred_cls = preds.data.max(1)[1]
        acc_src += pred_cls.eq(labels.data).cpu().sum()

    loss_src /= len(dataloader_src)
    acc_src = int(acc_src) / len(dataloader_src.dataset)

    for (images, labels) in dataloader_tgt:
        images = Variable(images.type(FloatTensor)).reshape(images.shape[0], -1)
        labels = Variable(labels.type(LongTensor))

        # preds = classifier(encoder(images, labels))
        preds, _ = net(images, alpha)
        # loss += criterion(preds, labels).data[0]
        loss_tgt += criterion(preds, labels).item()

        pred_cls = preds.data.max(1)[1]
        acc_tgt += pred_cls.eq(labels.data).cpu().sum()

    loss_tgt /= len(dataloader_tgt)
    # acc /= len(data_loader.dataset)
    acc_tgt = int(acc_tgt) / len(dataloader_tgt.dataset)

    print("Avg Loss = src:{}, tgt:{}, Avg Accuracy = src: {:2%} tgt:{:2%}".format(
        loss_src, loss_tgt,  acc_src, acc_tgt))
    return acc_src, acc_tgt



def train(dataloader_src, dataloader_tgt, net, domain_labels, train_epochs, writer=None):

    optimizer = optim.Adam(net.parameters(), lr=1e-3)
    loss_c = nn.CrossEntropyLoss()
    loss_d = nn.BCELoss()

    acc_tgt_best = 0

    for epoch in range(train_epochs):
        len_dataloader = min(len(dataloader_src), len(dataloader_tgt))
        for step, ((imgs_src, labels_src), (imgs_tgt, labels_tgt)) in enumerate(zip(dataloader_src, dataloader_tgt)):

            p = float(step + epoch * len_dataloader) / train_epochs / len_dataloader
            alpha = 2. / (1. + np.exp(-10 * p)) - 1

            imgs_src = Variable(imgs_src.type(FloatTensor))
            labels_src = Variable(labels_src.type(LongTensor))

            imgs_tgt = Variable(imgs_tgt.type(FloatTensor))
            labels_tgt = Variable(labels_tgt.type(FloatTensor))

            domain_label_src = Variable(FloatTensor(imgs_src.shape[0], 1).fill_(domain_labels[0]))
            domain_label_tgt = Variable(FloatTensor(imgs_tgt.shape[0], 1).fill_(domain_labels[1]))

            # Source Domain

            output_c, output_d = net(x=imgs_src, alpha=alpha)
            loss_c_src = loss_c(output_c, labels_src)
            loss_d_src = loss_d(output_d, domain_label_src)

            # Target Domain
            _, d_output = net(x=imgs_tgt, alpha=alpha)
            loss_d_tgt = loss_d(d_output, domain_label_tgt)

            optimizer.zero_grad()
            loss_total = loss_c_src + loss_d_src + loss_d_tgt
            loss_total.backward()
            optimizer.step()

        if epoch % 3 == 0:
            acc_src, acc_tgt = evaluate(net, dataloader_src, dataloader_tgt, alpha)
            acc_tgt_best = acc_tgt if acc_tgt_best < acc_tgt else acc_tgt_best
            if writer:
                writer.add_scalar('Train/loss_c_src', loss_c_src, epoch)
                writer.add_scalar('Train/loss_d_src', loss_d_src, epoch)
                writer.add_scalar('Train/loss_d_src_tgt', loss_d_tgt, epoch)
                writer.add_scalar('Evaluate/Acc_src', acc_src, epoch)
                writer.add_scalar('Evaluate/Acc_tgt', acc_tgt, epoch)
    return acc_tgt_best




if __name__ == '__main__':
    pass











