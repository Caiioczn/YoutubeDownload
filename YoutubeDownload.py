from tkinter.ttk import *
from tkinter import *
from pytube import YouTube

window = Tk()
window.title('YoutubeDownload')
window.geometry('350x380')
window.config(bg='#15171a')
window.resizable(width=False,height=False)

# LABEL-YOUTUBE 
labelYoutube = Label(window,width=20,height=1,text='YoutubeDownloader',bg='#a80f0f',font='Arial 18',fg='white')
labelYoutube.place(x=25,y=10)

# LABEL-URL
labelURL = Label(window,width=5,height=1,text='URL:',bg='#15171a',fg='white',font=('Aial 10 '))
labelURL.place(x=50,y=70)

# URL-INPUT
inputURL = Entry(window,width=30,relief=GROOVE)
inputURL.place(x=90,y=73)

# COMBOBOX
labelCombo = Label(window,width=6,height=1,text='Formato:',bg='#15171a',fg='white',font=('Aial 10 '))
labelCombo.place(x=70,y=107)
select = Combobox(window)
select['values'] = ('Video','MP4')
# DEFAULT VALUE
select.current(0)
select.place(x=131,y=107)

window.mainloop()