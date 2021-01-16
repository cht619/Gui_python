# -*- coding: utf-8 -*-
# @Time : 2021/1/16 20:07
# @Author : CHT
# @Site : 
# @File : test1.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import tkinter as tk

window = tk.Tk()
window.title('Entry')
window.geometry('500x300')


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


def set_text():
    # how to use text!
    window = tk.Tk()
    window.title('Entry')
    window.geometry('500x300')
    e = tk.Entry(window, show=None)
    e.pack()

    # the function must before the button setting
    def insert_point():
        var = e.get() # 获取鼠标的位置
        t.insert('insert', var)

    def insert_end():
        # 文本框最后面接着插入内容
        var = e.get()
        t.insert('end', var)  # 无论鼠标选中哪里一定是在最后面那里插入

    # set button
    b1 = tk.Button(window, text='insert point', height=2, command=insert_point)
    b1.pack()
    b2 = tk.Button(window, text='insert_end', height=2, command=insert_end)
    b2.pack()

    t = tk.Text(window, height=5)
    t.pack()

    window.mainloop()


def set_listbox():
    # 下拉框
    var1 = tk.StringVar()
    # set label
    l = tk.Label(window, bg='green', fg='yellow')
    l.pack()

    def print_selection():
        value = lb.get(lb.curselection()) # 获取当取选中的样本
        val1.set(value)

    # set button
    b1 = tk.Button(window, text='print selection', command=print_selection)
    b1.pack()

    # create Listbox
    var2=tk.StringVar()
    var2.set((1, 2, 3, 4))
    lb = tk.Listbox(window, listvariable=var2)




if __name__ == '__main__':
    set_text()
