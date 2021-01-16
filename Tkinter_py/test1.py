# -*- coding: utf-8 -*-
# @Time : 2021/1/16 20:07
# @Author : CHT
# @Site : 
# @File : test1.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import tkinter as tk


def set_button():
    on_hit = False
    def hit_me():
        global on_hit
        if on_hit == False:
            on_hit = True
            var.set('you hit me!')
        else:
            on_hit = False
            var.set('')


    # 实例化window
    window = tk.Tk()

    # set title
    window.title('Method summary of transfer learning')

    # set window size
    window.geometry('500x300')

    # set label
    # height=2 就是这个标签有两个label这么高
    # label = tk.Label(window, text='Hi!', bg='yellow', font=('Arial', 12), width=30, height=2)

    # set button
    var = tk.StringVar()
    # fg 为字体颜色
    label = tk.Label(window, textvariable=var, fg='green', width=30, height=2)

    # pack
    label.pack()

    button = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
    button.pack()

    # loop
    window.mainloop()


def set_entry():
    window = tk.Tk()
    window.title('Entry')
    window.geometry('500x300')
    e1 = tk.Entry(window, show='*')
    e2 = tk.Entry(window, show=None)
    e1.pack()
    e2.pack()

    window.mainloop()

if __name__ == '__main__':
    set_entry()
