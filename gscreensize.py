# coding:utf-8
#
# ----------------------------------
#            getScreenSize
# ----------------------------------
#
# a simple tool to get your device
# screen size  using tkinter
#
# dev : JULIEN ROUSSEL
# dev_mail : julien.roussel22@gmail.com
# version : 1.0.0

import tkinter
 
root = tkinter.Tk()
root.configure(bg='lightgrey')
root.geometry('400x600')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

lbl = tkinter.Label(root,text=f"Width: {w}, Height: {h}", borderwidth=2,relief=tkinter.SUNKEN)
btn = tkinter.Button(root, text='QUIT', width=10, command=root.quit)
								
lbl.pack(expand=tkinter.YES, ipadx=10, ipady=10)
btn.pack(pady=100)

root.mainloop()