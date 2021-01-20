# -*- coding: utf-8 -*-
# @Time : 2021/1/20 14:52
# @Author : CHT
# @Site : 
# @File : transfer_learning_approaches.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import tkinter as tk
import tkinter.messagebox
import pickle
from transfer_learning_gui import tkinter_component

# 定义一些字体
font_top1 = ('Arial', 15)
font_top2 = ('Arial', 14)
transfer_learning_approaches = ['DAN', 'CDAN', 'ADDA', 'DANN', 'SSDA', 'TAT', 'TAT_Kmeans']
dataset = ['Image-CLEF', 'Office-Caltech', 'Office-Home', 'Multi Domain Sentiment', 'VisDa-2017']



def get_result_window(window, approach):
    result_window = tk.Toplevel(window)
    result_window.geometry('400x300')
    result_window.title('The Result of {}'.format(approach))

    # 4 Dataset
    tk.Label(result_window, font=font_top2, text=", ".join(dataset)).pack()

    def accuracy_display():
        pass



    tk.Button(result_window, font=font_top2, text='Office-Home').pack()
    tk.Label(result_window, font=font_top2, text='Accuracy: 98.5%').pack()


def transfer_learning_gui():
    window = tk.Tk()
    window.title('Transfer Learning')
    window.geometry('700x500')

    # .grid(row=2, column=1, sticky='E')
    # tk.Label(window, text='Transfer learning approaches', font=font_top1).pack()

    # set Listbox
    var_approach = tk.StringVar()  # 用于展示点击内容
    var_approach.set('Transfer learning approaches')
    tk.Label(window, bg='green', font=font_top2, textvariable=var_approach).pack()

    # function
    def selection():
        value = lb.get(lb.curselection())
        var_approach.set(value)

        # 后续处理在这里！！
        current_approach = var_approach.get()  # get current approach
        if current_approach == 'DAN':
            tkinter_component.get_result_window(window, current_approach)
            # tkinter_component.get_dataset_accuracy_table(window, 'Office-Home')
            # tkinter.messagebox.showinfo(title='Welcome', message='How are you? ')

    button_selection = tk.Button(window, text='Select approach!', command=selection)
    button_selection.pack()

    var_approaches_list = tk.StringVar()  # Listbox的值
    var_approaches_list.set(transfer_learning_approaches)
    lb = tk.Listbox(window, listvariable=var_approaches_list)
    lb.pack()


    window.mainloop()


if __name__ == '__main__':
    transfer_learning_gui()