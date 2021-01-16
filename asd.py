# -*- coding: utf-8 -*-
# @Time : 2020/12/23 21:14
# @Author : CHT
# @Site : 
# @File : asd.py
# @Software: PyCharm 
# @Blog: https://www.zhihu.com/people/xia-gan-yi-dan-chen-hao-tian
# @Function:


import sys
import untitled
from PyQt5.QtWidgets import QApplication, QDialog
if __name__ == '__main__':
  myapp = QApplication(sys.argv)
  myDlg = QDialog()
  myUI = QtTest.Ui_Dialog()
  myUI.setupUi(myDlg)
  myDlg.show()
  sys.exit(myapp.exec_())
