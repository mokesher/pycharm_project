#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tkMessageBox
from ScrolledText import ScrolledText
from Tkinter import *
import tkFileDialog
import os
import fnmatch


def search():
    kw = ent_search.get()
    type_str = ent_type.get()
    if not kw or not type_str:
        tkMessageBox.showerror('警告', '请输入！！！')
        return
    path = tkFileDialog.askdirectory()
    fnlist = os.walk(path)
    listBox.delete(0, END)
    for root, dirs, files in fnlist:
        for i in fnmatch.filter(files, type_str):
            fn = '%s/%s' % (root, i)
            fn.replace('\\', '/')
            f = open(fn)
            if kw in f.read():
                listBox.insert(END, fn)
                f.close()


def edit(e):
    fn = listBox.get(listBox.curselection())
    fileWindow = Tk()
    fileWindow.geometry('+800+200')
    text = ScrolledText(fileWindow, width=80, height=40)
    text.grid()
    text.insert(INSERT, open(fn).read())
    fileWindow.mainloop()


root = Tk()
root.title('文件搜索')
root.geometry('+900+300')
Label(root, text='关键字:').grid()
ent_search = Entry(root)
ent_search.grid(row=0, column=1)
Label(root, text='文件类型:').grid(row=0, column=2)
ent_type = Entry(root)
ent_type.grid(row=0, column=3)
btn = Button(root, text='搜索', command=search)
btn.grid(row=0, column=4)
listBox = Listbox(root, width=60)
listBox.bind('<Double-Button-1>', edit)
listBox.grid(row=1, columnspan=5)
root.mainloop()
