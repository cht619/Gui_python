# -*- coding: utf-8 -*-
# @Time : 2020/12/26 19:56
# @Author : CHT
# @Site : 
# @File : train.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import csv
import torch
from DANN import train, networks
from data_preprocess import get_data, data_path
from tensorboardX import SummaryWriter

FloatTensor = torch.cuda.FloatTensor
LongTensor = torch.cuda.LongTensor
feature_dim = 400
num_classes = 2
batch_size = 128

def train_to_csv(domain_src, domain_tgt, domain_name, iteration, n_Dtl=0.03,fea_type='MDSA'):
    print('----------------{}---------------'.format(domain_name))

    root_path = data_path.MDSA_root_path

    dataloader_src, dataloader_tgt = get_data.get_sd_td_with_labels_dataloader(
        root_path, domain_src, domain_tgt, fea_type=fea_type, n_Dtl=n_Dtl, batch_size=batch_size)

    train_epochs = 81

    dan = networks.DANN_Net(in_dim=feature_dim, out_dim=num_classes).cuda()
    # with SummaryWriter('./runs/{}_1028'.format( domain_name)) as writer:
    domain_label = [1.0, 0.0]
    acc_tgt_best = train.train(dataloader_src, dataloader_tgt, dan, domain_labels=domain_label,
                               train_epochs=train_epochs)

    with open(r'E:\cht_project\Experimental_Result\ER\Multi_Domain_Sentiment_Dataset\DANN\{}.csv'.format(domain_name), 'a+',
              newline='') as f:
        f_csv = csv.writer(f)
        if iteration == 0:
            dataloader_src0 = get_data.get_src_dataloader(root_path, domain_src, batch_size=batch_size, fea_type=fea_type)
            dataloader_tgt0 = get_data.get_src_dataloader(root_path, domain_tgt, batch_size=batch_size, fea_type=fea_type)

            for _ in range(5):  # 多次说服力强一点
                dan = networks.DANN_Net(in_dim=feature_dim, out_dim=num_classes).cuda()
                acc_tgt_original = train.train(dataloader_src0, dataloader_tgt0, dan, domain_labels=domain_label,
                               train_epochs=train_epochs)
                f_csv.writerow([acc_tgt_original])
            f_csv.writerow(['with Dtl'])
        f_csv.writerow([float(acc_tgt_best)])


if __name__ == '__main__':
    from torch.backends import cudnn

    torch.backends.cudnn.benchmark = True

    domain_B = 'books_400.mat'
    domain_D = 'dvd_400.mat'
    domain_K = 'kitchen_400.mat'
    domain_E = 'elec_400.mat'

    for iteration in range(50):
        train_to_csv(data_path.domain_B, data_path.domain_D, 'B_D', iteration=iteration)
        train_to_csv(data_path.domain_B, data_path.domain_K, 'B_K', iteration=iteration)
        train_to_csv(data_path.domain_B, data_path.domain_E, 'B_E', iteration=iteration)

        train_to_csv(data_path.domain_D, data_path.domain_B, 'D_B', iteration=iteration)
        train_to_csv(data_path.domain_D, data_path.domain_K, 'D_K', iteration=iteration)
        train_to_csv(data_path.domain_D, data_path.domain_E, 'D_E', iteration=iteration)

        train_to_csv(data_path.domain_K, data_path.domain_B, 'K_B', iteration=iteration)
        train_to_csv(data_path.domain_K, data_path.domain_D, 'K_D', iteration=iteration)
        train_to_csv(data_path.domain_K, data_path.domain_E, 'K_E', iteration=iteration)

        train_to_csv(data_path.domain_E, data_path.domain_B, 'E_B', iteration=iteration)
        train_to_csv(data_path.domain_E, data_path.domain_K, 'E_K', iteration=iteration)
        train_to_csv(data_path.domain_E, data_path.domain_D, 'E_D', iteration=iteration)


