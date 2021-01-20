# -*- coding: utf-8 -*-
# @Time : 2020/12/26 21:49
# @Author : CHT
# @Site : 
# @File : networks.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:

import torch.nn as nn
import torch
from DANN.DANN.functions import ReverseLayerF

cuda = True if torch.cuda.is_available() else False
FloatTensor = torch.cuda.FloatTensor if cuda else torch.FloatTensor
LongTensor = torch.cuda.LongTensor if cuda else torch.LongTensor


class DANN_Net(nn.Module):

    def __init__(self, in_dim, out_dim):
        super(DANN_Net, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(in_dim, 2048),
            nn.BatchNorm1d(2048, 0.8),
            nn.LeakyReLU(inplace=True),
            nn.Linear(2048, 1024),
            nn.BatchNorm1d(1024, 0.8),
            nn.LeakyReLU(inplace=True),
            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(inplace=True),
        )

        self.classifier = nn.Sequential(
            nn.Linear(512, 256),
            nn.BatchNorm1d(256, 0.8),
            nn.LeakyReLU(inplace=True),
            nn.Linear(256, out_dim),
        )

        self.discriminator = nn.Sequential(
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 1),
            nn.Sigmoid(),
        )

    def forward(self, x, alpha):
        x = x.reshape(x.shape[0], -1)
        feature = self.encoder(x)
        reverse_feature = ReverseLayerF.apply(feature, alpha)
        class_output = self.classifier(feature)
        domain_output = self.discriminator(reverse_feature)

        return class_output, domain_output


if __name__ == '__main__':
    from torch.backends import cudnn

    torch.backends.cudnn.benchmark = True

    root_path = r'E:\cht_project\domain_adaptation_images\imageCLEF_resnet50'
    domain_c = 'c_c.csv'
    domain_i = 'i_i.csv'
    domain_p = 'p_p.csv'
    domain_ci = 'c_i.csv'
    domain_cp = 'c_p.csv'
    domain_ic = 'i_c.csv'
    domain_ip = 'i_p.csv'
    domain_pc = 'p_c.csv'
    domain_pi = 'p_i.csv'

