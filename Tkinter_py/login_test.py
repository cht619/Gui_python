# -*- coding: utf-8 -*-
# @Time : 2021/1/19 16:51
# @Author : CHT
# @Site : 
# @File : login_test.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import tkinter as tk
import tkinter.messagebox
import pickle


def login():
    window = tk.Tk()
    window.title('Transfer Learning')
    window.geometry('400x300')

    # set a image
    canvas = tk.Canvas(window, width=400, height=135, bg='green')
    image_file = tk.PhotoImage(file=r'')
    image = canvas.create_image(200, 0, anchor='n', image=image_file)
    canvas.pack(side='top')
    tk.Label(window, text='Welcome!', font=('Arial', 16)).pack()

    # user information
    tk.Label(window, text='User name:', font=('Arial', 14)).place(x=10, y=170)
    tk.Label(window, text='Password:', font=('Arial', 14)).place(x=10, y=210)

    # input Entry
    var_user_name = tk.StringVar()
    var_user_name.set('xxx@gmail.com')  # initial value
    entry_user_name = tk.Entry(window, textvariable=var_user_name, font=('Arial', 14))
    entry_user_name.place(x=120, y=175)

    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
    entry_usr_pwd.place(x=120, y=215)

    # function
    def usr_login():
        # get input
        user_name = var_user_name.get()
        user_pwd = var_usr_pwd.get()

        # 自定义一些功能
        try:
            with open(r'', 'r') as f:
                print(f.readlines())

        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()  # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input

        # 这里就是给出一些信息，比如说输出错误之类的
        if user_name in usrs_info:
            if user_pwd == usrs_info[user_name]:
                tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + user_name)
            # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
            else:
                tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
        else:  # 如果发现用户名不存在
            is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
            # 提示需不需要注册新用户
            if is_sign_up:
                usr_sign_up()

    def usr_sign_up():
        def sign_to_Hongwei_Website():
            # 以下三行就是获取我们注册时所输入的信息
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()

            # 这里是打开我们记录数据的文件，将注册信息读出
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
            # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
            if np != npf:
                tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')

            # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
            elif nn in exist_usr_info:
                tkinter.messagebox.showerror('Error', 'The user has already signed up!')

            # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                # 然后销毁窗口。
                window_sign_up.destroy()

        # 二级窗口
        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('300x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()
        new_name.set('@gmail.com')
        tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=130, y=50)

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=130, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=130, y=90)

        btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up!')
        btn_comfirm_sign_up.place(x=180, y=120)

    # 第7步，login and sign up 按钮
    btn_login = tk.Button(window, text='Login', command=usr_login)
    btn_login.place(x=120, y=240)
    btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
    btn_sign_up.place(x=200, y=240)

    window.mainloop()



if __name__ == '__main__':
    login()



