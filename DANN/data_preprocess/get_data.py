# -*- coding: utf-8 -*-
# @Time : 2020/12/26 21:53
# @Author : CHT
# @Site : 
# @File : get_data.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:

import numpy as np
import os
import torch.utils.data as data
import torch
from scipy.io import loadmat


def get_feas_labels(root_path, domain, fea_type='Resnet50'):
    # 得到原始特征
    path = os.path.join(root_path, domain)
    if fea_type == 'Resnet50':
        with open(path, encoding='utf-8') as f:
            imgs_data = np.loadtxt(f, delimiter=",")
            features = imgs_data[:, :-1]
            labels = imgs_data[:, -1]

    elif fea_type =='MDSA':
        # dict_keys(['__header__', '__version__', '__globals__', 'fts', 'labels'])
        domain_data = loadmat(path)
        features = np.asarray(domain_data['fts'])
        labels = np.asarray(domain_data['labels']).squeeze()

    else: # DeCAF6
        domain_data = loadmat(path)
        features = np.asarray(domain_data['feas'])
        labels = np.asarray(domain_data['labels']).squeeze() - 1
    return features, labels


def get_src_dataloader_by_feas_labels(feas, labels, batch_size = 128, drop_last=False):
    dataset = data.TensorDataset(torch.tensor(feas), torch.tensor(labels))
    dataloader = data.DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=drop_last,
    )
    return dataloader


def get_src_dataloader(root_path, domain, batch_size, drop_last=False, fea_type='Resnet50'):
    feas, labels = get_feas_labels(root_path, domain, fea_type)

    dataset = data.TensorDataset(torch.tensor(feas), torch.tensor(labels))
    dataloader = data.DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=drop_last,
    )

    return dataloader


def get_td_with_labels(fea_src, labels_src, fea_tgt, labels_tgt, n):
    extra_index = np.random.choice(len(fea_tgt), int(n * len(fea_tgt)), replace=False)

    fea_tgt_label = np.asarray([fea_tgt[i] for i in extra_index])
    labels_tgt_label = np.asarray([labels_tgt[i] for i in extra_index])

    fea_tgt = np.asarray([fea_tgt[i] for i in range(len(fea_tgt)) if i not in extra_index])
    labels_tgt = np.asarray([labels_tgt[i] for i in range(len(labels_tgt)) if i not in extra_index])

    fea_src = np.concatenate((fea_src, fea_tgt_label), 0)
    labels_src = np.concatenate((labels_src, labels_tgt_label), 0)

    return fea_src, labels_src, fea_tgt, labels_tgt


def get_sd_td_with_labels_dataloader(root_path, domain_src, domain_tgt, n_Dtl, fea_type, batch_size=100):
    feas_src, labels_src = get_feas_labels(root_path, domain_src, fea_type=fea_type)
    feas_tgt, labels_tgt = get_feas_labels(root_path, domain_tgt, fea_type=fea_type)

    feas_src, labels_src, feas_tgt, labels_tgt = get_td_with_labels(feas_src, labels_src, feas_tgt, labels_tgt, n_Dtl)

    fea_type = data.TensorDataset(torch.tensor(feas_src), torch.tensor(labels_src))
    dataloader_src = data.DataLoader(
        dataset=fea_type,
        batch_size=batch_size,
        shuffle=True,
        drop_last=False,
    )

    fea_type = data.TensorDataset(torch.tensor(feas_tgt), torch.tensor(labels_tgt))
    dataloader_tgt = data.DataLoader(
        dataset=fea_type,
        batch_size=batch_size,
        shuffle=True,
        drop_last=False,
    )
    return dataloader_src, dataloader_tgt





if __name__ == '__main__':
    pass


