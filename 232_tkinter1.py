#starter code
##import tkinter
##from tkinter import *
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()  #root/win/window
win.title('GUI')

# create labels
# widgets = label, buttons, radio buttons--- tk, ttk(module)
name_label = ttk.Label(win, text='Enter your name : ')   #pack()/ grid()
name_label.grid(row=0,column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row=1,column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=2,column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Select your gender : ')
gender_label.grid(row=3,column=0, sticky=tk.W)

# create entry boxes
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2,column=1)

# create combobox
gender_var=tk.StringVar()
gender_combobox = ttk.Combobox(win, width=13, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# radio button
usertype = tk.StringVar()
radio_btn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radio_btn1.grid(row=4,column=0)
radio_btn1 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radio_btn1.grid(row=4,column=1)

# check button
checkbtn_var = tk.IntVar()
check_btn = ttk.Checkbutton(win, text='check if you want to subscribe our newsletter', variable=checkbtn_var)
check_btn.grid(row=5,columnspan=3)

# create a button
def action():
    username = name_var.get()
    useremail = email_var.get()
    userage = age_var.get()
    print(f'{username} is {userage} years old, {useremail}')
    usergender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var==0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'
    print(f'{usergender} {user_type} {subscribed}')

    # write to txt file
##    with open('guifile.txt','a') as f:
##        f.write(f'{username},{userage},{useremail},{usergender},{user_type},{subscribed}\n')

    # write to csv file
    with open('guifile.csv','a',newline='') as f:
        dict_writer = DictWriter(f,fieldnames=['User_Name','User_Email','User_Age','User_Gender','User_Type','Subscribed'])
        if os.stat('guifile.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
                'User_Name' : username,
                'User_Email' : useremail,
                'User_Age' : userage,
                'User_Gender' : usergender,
                'User_Type' : user_type,
                'Subscribed' : subscribed
            })
    

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='#ff00ff')

    submit_btn.configure(foreground='Blue')

submit_btn = tk.Button(win, text='Submit', command=action)
submit_btn.grid(row=6,column=0)

win.mainloop()
