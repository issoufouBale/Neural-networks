import Data
import Net
import matplotlib.pyplot as plt
import os
import numpy as np

#from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.messagebox


from tkinter import Tk, Text
import tkinter as tk




# Root window
root = tk.Tk()
root.title('Neural Network')
root.resizable(False, False)
root.geometry('850x750')

# Text editor
text = tk.Text(root, height=12,width=73)
text.grid(column=1, row=2, sticky='nsew')


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

pred = []
y = []

model = Net.CreateNet(Data.x_train)

if os.path.exists("Weights.h5"):
    pred = Net.Solve(model, Data.x)

    pred = pred * Data.max_y + Data.min_y

    y = Data.y * Data.max_y + Data.min_y
else:
    history = Net.Lear(model, Data.x_train, Data.y_train)

    pred = Net.Solve(model, Data.x)

    pred = pred * Data.max_y + Data.min_y

    y = Data.y * Data.max_y + Data.min_y

v =tk.Label(root,text='Total error :',font="comicsansms 9 bold",relief ='groove')
v.place(x=400,y=300)
t3= tk.Text(root, height=2,width=20)
t3.place(x=400,y=330)
c=v =tk.Label(root,text='solids concentration in solution :',font="comicsansms 9 bold",relief ='groove')
c.place(x=400,y=380)
def d():
    TotalERR = 0
    for i in range(len(pred)):
        X = "Neural result:", round(pred[i], 3), " correct answer:", round(y[i], 3), "difference: ", round(pred[i] - y[i], 3),"\n"
        text.insert('1.0',X)
        TotalERR += abs(round(pred[i] - y[i], 3))
    t3.insert('1.0',TotalERR)
        #l1 = tk.Label(root,textvariable=TotalERR,font="Arial 20").place(x=300,y=340)
  
open_button = tk.Button(
    root,
    text='Open a File',
    command=open_text_file,font="comicsansms 9 bold",relief ='groove'
)
learn_button = tk.Button(
    root,
    text='Teach',
    command=d,font="comicsansms 9 bold",relief ='groove'
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
learn_button.grid(column=0,row=3,sticky='w',padx=10, pady=10)


#print("Общая ошибка: ", TotalERR)
'''
plt.plot(y,'r-',
         label='Реальный ответ',)
plt.plot(pred,'b*',
         label='ответ сети')
plt.legend()
plt.show()



'''



s = []

s.append([])





a=tk.Label(root, text = "Enter Temperature :",font="comicsansms 9 bold",relief ='groove')
b=tk.Label(root, text = "Enter Temp depression :",font="comicsansms 9 bold",relief ='groove')
c=tk.Label(root, text = "Enter Frequency % :",font="comicsansms 9 bold",relief ='groove')
tk.blank =tk.Entry(root)
t2= tk.Text(root, height=2,width=20)
t2.place(x=400,y=405)

Ans=tk.DoubleVar()


a.place(x=1,y=300)
b.place(x=1,y=340)
c.place(x=1,y=380)

x1=tk.DoubleVar(root)
x2=tk.DoubleVar(root)
x3=tk.DoubleVar(root)
a=tk.Entry(root,textvariable=x1 ).place(x=150,y=300)
b=tk.Entry(root,textvariable=x2).place(x=150,y=340)
c=tk.Entry(root,textvariable=x3).place(x=150,y=380)
#tk.blank.grid(row=10, column=1)


x1 = float()
x2 = float()
x3 = float()
s[0].append(x1)
s[0].append(x2)
s[0].append(x3)
s = np.array(s)
s = (s + Data.mean) / Data.std

def f1():
    bb = Net.Solve(model, s)
    bb = bb * Data.max_y + Data.min_y
    t2.insert('1.0',bb)



#l2= tk.Label(root,textvariable=bb,font="Arial 20").place(x=300,y=300)
b1=tk.Button(root, text='Quit', command=root.destroy,font="comicsansms 12 bold",relief ='groove').place(x=150,y=520)
b2=tk.Button(root, text='Calculate',command=f1,font="comicsansms 12 bold",relief ='groove' ).place(x=400,y=520)


#input()
root.mainloop()