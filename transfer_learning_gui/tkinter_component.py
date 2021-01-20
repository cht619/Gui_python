# -*- coding: utf-8 -*-
# @Time : 2021/1/20 19:12
# @Author : CHT
# @Site : 
# @File : tkinter_component.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:

import tkinter as tk
from tkinter import ttk
from DANN.Image_CLEF_Resnet50 import train
from DANN.data_preprocess import data_path

font_top1 = ('Arial', 15)
font_top2 = ('Arial', 14)
font_top3 = ('Arial', 10)
transfer_learning_approaches = ['DAN', 'CDAN', 'ADDA', 'DANN', 'SSDA', 'TAT', 'TAT_Kmeans']
Dataset = ['Image-CLEF', 'Office-Caltech', 'Office-Home', 'Multi Domain Sentiment', 'VisDA-2017']

Office_Home = (
'Ar->Cl', 'Ar->Pr', 'Ar->Rw', 'Cl->Ar', 'Cl->Pr', 'Cl->Rw', 'Pr->Ar', 'Pr->Cl', 'Pr->Rw', 'Rw->Ar', 'Rw->Cl', 'Rw->Pr')
Image_CLEF = ('C->I','C->P','I->C','I->P','P->C','P->I')
Office_Caltech = ('A->C','A->D','A->W','C->A','C->D','C->W','D->A','D->C','D->W','W->A','W->C','W->D')
MDS = ('B->D', 'B->E', 'B->K', 'D->B', 'D->E', 'D->K', 'E->B', 'E->D', 'E->K', 'K->B', 'K->D', 'K->E')
VisDA = ('train->vali', ' ')


def get_dataset_accuracy_table(window, dataset, train_epochs, n_Dtl):
    d = None
    print(train_epochs, n_Dtl)

    experimental_result_window = tk.Toplevel(window)
    experimental_result_window.title('Experimental Result')
    experimental_result_window.geometry('700x500')

    # experimental_result_table
    experimental_result_table = ttk.Treeview(experimental_result_window)

    if dataset == 'Office-Home':
        d = Office_Home
    elif dataset == 'Image-CLEF':
        d = Image_CLEF
        # result = [train.get_result(data_path.domain_c, data_path.domain_ci, train_epochs=train_epochs),
        # train.get_result(data_path.domain_c, data_path.domain_cp, train_epochs=train_epochs),
        # train.get_result(data_path.domain_p, data_path.domain_pc, train_epochs=train_epochs),
        # train.get_result(data_path.domain_p, data_path.domain_pi, train_epochs=train_epochs),
        # train.get_result(data_path.domain_i, data_path.domain_ic, train_epochs=train_epochs),
        # train.get_result(data_path.domain_i, data_path.domain_ip, train_epochs=train_epochs)]
        result = [train.get_result(data_path.domain_c, data_path.domain_ci, train_epochs=train_epochs),]


    elif dataset == 'Office-Caltech':
        d = Office_Caltech
    elif dataset == 'VisDA-2017':
        d = VisDA
    elif dataset == 'Multi Domain Sentiment':
        d = MDS

    experimental_result_table["columns"] = d
    for col in d:
        experimental_result_table.column(col, width=70)
        experimental_result_table.heading(column=col, text='{}'.format(col))
    experimental_result_table.insert('', 0, text='Accuracy 0% Dtl', values=result)

    experimental_result_table.pack()


def get_method_window_DAN(window, approach):
    result_window = tk.Toplevel(window)
    result_window.geometry('400x300')
    result_window.title('The Result of {}'.format(approach))

    # 5 Dataset
    # tk.Label(result_window, font=font_top2, text=", ".join(Dataset)).pack()
    tk.Label(result_window, font=font_top3, text='Proportion of labeled Target Domain: ').grid(row=0, column=0)
    entry_n_Dtl = tk.Entry(result_window, font=font_top3, show=None, width=10)
    entry_n_Dtl.grid(row=0, column=1)
    tk.Label(result_window, font=font_top3, text='Train epochs: ').grid(row=1, column=0)
    entry_train_epochs = tk.Entry(result_window, font=font_top3, show=None, width=10)
    entry_train_epochs.grid(row=1, column=1)

    def go():
        # Image-CLEF
        train_epochs = int(entry_train_epochs.get())
        n_Dtl = float(entry_n_Dtl.get())
        print(entry_n_Dtl.get(), entry_train_epochs.get())
        # train.get_result(data_path.domain_c, data_path.domain_ci, 'C_I', train_epochs=train_epochs)
        # train.get_result(data_path.domain_c, data_path.domain_cp, 'C_P', train_epochs=train_epochs)
        # train.get_result(data_path.domain_p, data_path.domain_pc, 'P_C', train_epochs=train_epochs)
        # train.get_result(data_path.domain_p, data_path.domain_pi, 'P_I', train_epochs=train_epochs)
        # train.get_result(data_path.domain_i, data_path.domain_ic, 'I_C', train_epochs=train_epochs)
        # train.get_result(data_path.domain_i, data_path.domain_ip, 'I_P', train_epochs=train_epochs)
    tk.Button(result_window, text='Confirm.', font=font_top3, command=go).grid(row=2, column=0)

    def accuracy_display(d):
        train_epochs = int(entry_train_epochs.get())
        n_Dtl = float(entry_n_Dtl.get())
        get_dataset_accuracy_table(result_window, d, train_epochs=train_epochs, n_Dtl=n_Dtl)

    # 用for循环传参，lambda会覆盖掉参数，无法正常调用函数
    # for i in range(4, 3 + len(Dataset)): 这样做也会影响lambda取值！！
    tk.Button(result_window, font=font_top2, text=Dataset[0], command=lambda: accuracy_display(Dataset[0])).grid(row=3, column=2)
    tk.Button(result_window, font=font_top2, text=Dataset[1], command=lambda: accuracy_display(Dataset[1])).grid(row=4, column=2)
    tk.Button(result_window, font=font_top2, text=Dataset[2], command=lambda: accuracy_display(Dataset[2])).grid(row=5, column=2)
    tk.Button(result_window, font=font_top2, text=Dataset[3], command=lambda: accuracy_display(Dataset[3])).grid(row=6, column=2)
    tk.Button(result_window, font=font_top2, text=Dataset[4], command=lambda: accuracy_display(Dataset[4])).grid(row=7, column=2)



if __name__ == '__main__':

    # get_dataset_accuracy_table()
    Dataset = ['B', 'D', 'E', 'K']
    for i in Dataset:
        for j in Dataset:
            if j != i:
                print('\'{}->{}\''.format(i, j), end=',')

