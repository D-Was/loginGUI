from pygame import mixer
from tkinter import messagebox
import webbrowser
from tkinter import *
# first part
wind=Tk()
wind.geometry('350x200')
lblu=Label(wind ,text='Welcome to login').grid(column=5, row=0)
lbl1=Label(wind, text='username').grid(row=2)
lbl2=Label(wind, text='password').grid(row=3)
txt1=Entry(wind, width=10)
txt1.grid(column=2, row=2)
txt2=Entry(wind, width=10)
txt2.grid(column=2, row=3)
def click():
    get_ustname=txt1.get()
    get_password=txt2.get()
    with open('/home/dwas/Desktop/key','w') as a:
        a.write(get_ustname)
        a.close()

    with open('/home/dwas/Desktop/new','w') as s:
        s.write(get_password)
        s.close()

    if not get_ustname:
        messagebox.showinfo( 'error', 'Cannot leave empty')

    elif not get_password:
        messagebox.showinfo('error', 'cannot leave empty')

    else:
        wind.destroy()

bttn1=Button(wind, text='ok', command=click).grid(column=3,row=4)
mixer.init()
mixer.music.load('/home/dwas/Downloads/elev')
mixer.music.play()
def pause():
    mixer.music.pause()
bttn_mus=Button(wind, text='pause', command=pause).grid(column=0,row=10)
wind.mainloop()
# second part
# from tkinter import *
wid1=Tk()
wid1.title('Login Page')
labl_main1=Label(wid1, text='SignIn').grid(column=5)
lbl_main2=Label(wid1, text='username').grid(column=0, row=2)
lbl2_main2=Label(wid1, text='password').grid(column=0, row=3)
txt_main1=Entry(wid1, width=10)
txt_main1.grid(column=1, row=2)
txt_main2=Entry(wid1, width=10)
txt_main2.grid(column=1, row=3)
def clickmain():
    with open('/home/dwas/Desktop/key') as h:
        read_us=h.read()

    with open('/home/dwas/Desktop/new') as d:
        read_pass=d.read()

    get_maius=txt_main1.get()
    get_mainpas=txt_main2.get()
    if get_maius==read_us and get_mainpas==read_pass:
        messagebox.showinfo('sucess','access granted')
        webbrowser.open('https://d-was.github.io/Supercell/')
        wid1.destroy()
    else:
        messagebox.showwarning('error','password doesnt matcj')



btn_main1=Button(wid1, text='ok', command=clickmain).grid(column=3, row=4)
wid1.mainloop()






    
    
   

