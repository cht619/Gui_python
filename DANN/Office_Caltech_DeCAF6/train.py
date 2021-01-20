# -*- coding: utf-8 -*-
# @Time : 2020/12/26 22:13
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

FloatTensor = torch.cuda.FloatTensor
LongTensor = torch.cuda.LongTensor
feature_dim = 4096
num_classes = 10
batch_size = 128

def train_to_csv(domain_src, domain_tgt, domain_name, iteration, n_Dtl=0.03,fea_type='DeCAF6'):
    print('----------------{}---------------'.format(domain_name))

    root_path = data_path.Office_Caltech_root_path

    dataloader_src, dataloader_tgt = get_data.get_sd_td_with_labels_dataloader(
        root_path, domain_src, domain_tgt, fea_type=fea_type, n_Dtl=n_Dtl, batch_size=batch_size)

    train_epochs = 81

    dan = networks.DANN_Net(in_dim=feature_dim, out_dim=num_classes).cuda()
    # with SummaryWriter('./runs/{}_1028'.format( domain_name)) as writer:
    domain_label = [1.0, 0.0]
    acc_tgt_best = train.train(dataloader_src, dataloader_tgt, dan, domain_labels=domain_label, train_epochs=train_epochs)

    with open(r'E:\cht_project\Experimental_Result\ER\Office_Caltech_DeCAF6\DANN\{}.csv'.format(domain_name), 'a+',
              newline='') as f:
        f_csv = csv.writer(f)
        if iteration == 0:

            dataloader_src0 = get_data.get_src_dataloader(root_path, domain_src, batch_size=batch_size, fea_type=fea_type)
            dataloader_tgt0 = get_data.get_src_dataloader(root_path, domain_tgt, batch_size=batch_size, fea_type=fea_type)

            for _ in range(5):  # 多次说服力强一点
                dan = networks.DANN_Net(in_dim=feature_dim, out_dim=num_classes).cuda()
                acc_tgt_original = train.train(
                    dataloader_src0, dataloader_tgt0, dan, domain_labels=domain_label, train_epochs=train_epochs)
                f_csv.writerow([acc_tgt_original])
            f_csv.writerow(['with Dtl'])
        f_csv.writerow([float(acc_tgt_best)])




if __name__ == '__main__':
    from torch.backends import cudnn
    torch.backends.cudnn.benchmark = True

    for iteration in range(50):
        train_to_csv(data_path.caltech_path, data_path.amazon_path, 'C_A', iteration=iteration)
        train_to_csv(data_path.caltech_path, data_path.dslr_path, 'C_D', iteration=iteration)
        train_to_csv(data_path.caltech_path, data_path.webcam_path, 'C_W', iteration=iteration)

        train_to_csv(data_path.amazon_path, data_path.caltech_path, 'A_C', iteration=iteration)
        train_to_csv(data_path.amazon_path, data_path.webcam_path, 'A_W', iteration=iteration)
        train_to_csv(data_path.amazon_path, data_path.dslr_path, 'A_D', iteration=iteration)

        train_to_csv(data_path.dslr_path, data_path.amazon_path, 'D_A', iteration=iteration)
        train_to_csv(data_path.dslr_path, data_path.webcam_path, 'D_W', iteration=iteration)
        train_to_csv(data_path.dslr_path, data_path.caltech_path, 'D_C', iteration=iteration)

        train_to_csv(data_path.webcam_path, data_path.amazon_path, 'W_A', iteration=iteration)
        train_to_csv(data_path.webcam_path, data_path.caltech_path, 'W_C', iteration=iteration)
        train_to_csv(data_path.webcam_path, data_path.dslr_path, 'W_D', iteration=iteration)




