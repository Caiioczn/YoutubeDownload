from tkinter.ttk import *
from tkinter import *
from pytube import YouTube

# FUNCTION
def buttonSee():
    link = inputURL.get()
    yt = YouTube(link)
    
    titulo = yt.title
    views = yt.views
    
    labelTitulo1 = Label(window,width=6,height=2,text='Titulo:',bg='#15171a',fg='white',font=('Aial 10 '))
    labelTitulo1.place(x=30,y=210)
    labelTitulo2 = Label(window,width=50,height=1,text=titulo,bg='#15171a',anchor=SW,fg='white',font=('Aial 10 '))
    labelTitulo2.place(x=75,y=218)
    
    labelViews1 = Label(window,width=6,height=2,text='Views:',bg='#15171a',fg='white',font=('Aial 10 '))
    labelViews1.place(x=30,y=240)
    labelViews2 = Label(window,width=50,height=1,text=views,bg='#15171a',anchor=SW,fg='white',font=('Aial 10 '))
    labelViews2.place(x=75,y=248)


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

# STATUS
labelInfo = Label(window,width=20,height=1,text='INFORMAÇÃO',bg='#a80f0f',font='Arial 18',fg='white')
labelInfo.place(x=30,y=170)

# BUTTON SEE
see = Button(window,width=3,height=1,command=buttonSee,text='Ver',relief=RAISED)
see.place(x=290,y=89)

window.mainloop()