# -*- coding: utf-8 -*-
# @Time : 2021/1/16 20:07
# @Author : CHT
# @Site : 
# @File : test1.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk

window = tk.Tk()
window.title('My window')
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
    # .grid 与get会有冲突
    # 下拉框
    var1 = tk.StringVar()
    # set label
    l = tk.Label(window, bg='green', fg='blue', width=20, textvariable=var1)
    l.grid(sticky=tk.N+tk.S)
    # l.pack()

    def print_selection():
        value = lb.get(lb.curselection()) # get the current selected
        var1.set(value)

    # set button
    b1 = tk.Button(window, text='print selection', command=print_selection)
    b1.grid(sticky=tk.N+tk.S)
    # b1.pack()

    # create Listbox
    var2=tk.StringVar()
    var2.set(('ADDA', 'DANN', 'CDAN', 'DAN'))
    lb = tk.Listbox(window, listvariable=var2)
    lb.grid(sticky=tk.N+tk.S)

    list_items = [11, 22, 33, 44]
    # for item in list_items:
    #     lb.insert('end', item)  # insert 就是最开始
    # lb.insert(1, 'first')  # 根据index堆上面的var2进行添加
    # lb.insert(2, 'second')
    # lb.delete(2)  # 删除第二个位置的字符
    # lb.pack()

    window.mainloop()


def set_canvas():
    canvas = tk.Canvas(window, bg='green', height=1000, width=1000)
    image_file = ImageTk.PhotoImage(file=r'C:\Users\Administrator\Desktop\frame_0001.png')
    # 图片要放在画布canvas的哪个位置 (250, 0)
    image = canvas.create_image(0, 0, anchor='n', image=image_file)
    # 定义多边形参数，然后在画布上画出指定图形
    x0, y0, x1, y1 = 100, 100, 150, 150
    line = canvas.create_line(x0 - 50, y0 - 50, x1 - 50, y1 - 50)  # 画直线
    oval = canvas.create_oval(x0 + 120, y0 + 50, x1 + 120, y1 + 50, fill='yellow')  # 画圆 用黄色填充
    arc = canvas.create_arc(x0, y0 + 50, x1, y1 + 50, start=0, extent=180)  # 画扇形 从0度打开收到180度结束
    rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20)  # 画矩形正方形
    canvas.pack(side='top')


    # function
    def moveit():
        canvas.move(oval, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动

    b = tk.Button(window, text='move item', command=moveit).pack()

    window.mainloop()


def set_png():
    photo = ImageTk.PhotoImage(file=r'C:\Users\Administrator\Desktop\frame_0001.png')
    tk.Label(window, image=photo).pack()

    window.mainloop()


def set_frame():
    tk.Label(window, text='on the window', bg='red').pack()

    # create frame
    frame = tk.Frame(window)
    frame.pack()

    # create the second layer of frame
    frame_l = tk.Frame(frame)
    frame_r = tk.Frame(frame)
    frame_l.pack(side='left')
    frame_r.pack(side='right')
    # create the third layer of frame
    tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
    tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
    tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
    tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
    tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
    tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

    window.mainloop()


def set_messageBox():
    # tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')  # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')  # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))  # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

    def hit_me():
        tk.Label(window, text='hi')
        tkinter.messagebox.showwarning(title='Hi', message='有警告！')
        tk.Label(window, text='hi')

    tk.Button(window, text='messageBox!', command=hit_me).pack()
    window.mainloop()


def set_Manager():
    # grid
    for i in range(3):
        for j in range(3):
            # padx就是单元格左右间距，pady就是单元格上下间距，ipadx是单元格内部元素与单元格的左右间距，
            # ipady是单元格内部元素与单元格的上下间距。
            tk.Label(window, text='{}'.format(j)).grid(row=i, column=j)

    # pack 就只是上下左右
    # tk.Label(window, text='P', fg='red').pack(side='top')  # 上
    # tk.Label(window, text='P', fg='red').pack(side='bottom')  # 下
    # tk.Label(window, text='P', fg='red').pack(side='left')  # 左
    # tk.Label(window, text='P', fg='red').pack(side='right')  # 右

    # place 精确定位 nw: north west 西北
    # tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')

    window.mainloop()


def set_Toplevel():
    def create_window():
        top = tk.Toplevel(window)
        top.geometry('300x200')
        top.title('A')

        msg = tk.Button(top, text='Hi,tis is a button!')
        tk.Button(top, text='Hi,tis is a button!').pack()
        tk.Button(top, text='Hi,tis is a button!').pack()
        tk.Button(top, text='Hi,tis is a button!').pack()
        tk.Button(top, text='Hi,tis is a button!').pack()
        msg.pack()
    tk.Button(window, text='make window', command=create_window).pack()

    window.mainloop()


if __name__ == '__main__':
    set_canvas()