import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('LOOP')

labels = ['what is your name : ','What is your age : ','What is your gender : ','Country : ','State : ','City : ']
for i in range(len(labels)):
    cur_label = 'label'+str(i)
    cur_label = ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

##cur_var = tk.StringVar()
user_info = {
        'name': tk.StringVar(),
        'age': tk.StringVar(),
        'gender': tk.StringVar(),
        'country': tk.StringVar(),
        'state': tk.StringVar(),
        'city':  tk.StringVar()
    }

counter=0
for i in user_info:
    cur_entry = 'entry' + i
    cur_entry = ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entry.grid(row=counter,column=1)
    counter += 1

def submit():
    for i in user_info:
        print(user_info[i].get())
    

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=6,columnspan=2)

win.mainloop()
