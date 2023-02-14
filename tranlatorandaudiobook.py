import sys
from tkinter import *
import pyttsx3
import threading
from tkinter import messagebox
import PyPDF2
import pyttsx3
from translate import Translator
from tkinter import *
from tkinter import messagebox

window = Tk()

class Speaking(threading.Thread):
    def __init__(self, sentence, **kw):
        super().__init__(**kw)
        self.words = sentence.split()
        self.paused = False

    def run(self):
        self.running = True
        while self.words and self.running:
            if not self.paused:
                pdf = open(B1.get(), "rb")
                pdf_read = PyPDF2.PdfReader(pdf)
                totalpgs = pdf_read.numPages
                b = int(totalpgs)
                for i in range(b):
                    pdf = pdf_read.getPage(i)
                    text = (pdf.extractText())
                    speak = pyttsx3.init()
                    speak.say(text)
                    speak.setProperty('rate',50)
                    speak.runAndWait()
                word = self.words.pop(0)
                print(word)
                engine.say(B1.get)
                engine.runAndWait()

        messagebox.showinfo("Zakończono","Działanie Zakończono Sukcesem")
        self.running = False

    def stop(self):
        self.running = False
        sys.exit()

    def resume(self):
        self.paused = False

speak = None

def read():
    global speak
    if speak is None or not speak.running:
        speak = Speaking(B1.get(), daemon=True)
        speak.start()

def stop():
    global speak
    if speak:
        speak.stop()
        speak = None

def pause():
    if speak:
        speak.pause()

def clear():
    B1.delete(0,END)

engine = pyttsx3.init()

l1=Label(window,text='PLEASE PASS YOUR FILE ', font=('arial',35),background='white')
l1.grid(column=1,row=0,sticky='N',padx=10,pady=20)
B1=Entry(window,font=('Arial',35),background='white')
B1.grid(column=1,row=1,sticky='N',padx=10,pady=20)

read_button = Button(window, text='CONVERT',command=read,font=('arial',20),width=20,background='green')
read_button.grid(column=1,row=2,sticky='N',padx=10,pady=20)


stop_button = Button(window, text='BREAK',command=stop,font=('arial',20),width=20,background='RED')
stop_button.grid(column=1,row=4,sticky='N',padx=10,pady=20)

b3=Button(window, text='CLEAN',command=clear,font=('arial',20),width=20,background='orange')
b3.grid(column=1,row=3,sticky='N',padx=10,pady=20)

#mainloop()


def tlumaczenie(file):
    pdf = open(file, "rb")
    pdf_read = PyPDF2.PdfReader(pdf)
    pdf = pdf_read.getPage(0)
    text = (pdf.extractText())
    while True:
        c = input('PODAJ JĘZYK WEJŚCIA(PL,DE,EN,RUS,FR: --> ')
        d = input('PODAJ JĘZYK WYJŚCIA(PL,DE,EN,RUS,FR:--> ')
        #e = input('Podaj tekst do tłumaczenia:--> ')
        translator = Translator(from_lang=c, to_lang=d)
        trans = translator.translate(text)
        print(trans)
        speak = pyttsx3.init()
        speak.setProperty('rate', 500)
        speak.say(trans)
        speak.runAndWait()
        break


def audiobook(file):
    pdf = open(file, "rb")
    pdf_read = PyPDF2.PdfReader(pdf)
    pdf = pdf_read.getPage(0)
    text = (pdf.extractText())
    speak = pyttsx3.init()
    speak.setProperty('rate', 50)
    speak.say(text)
    speak.runAndWait()

#audiobook("C:/Users/48667/Desktop/tekst.pdf")
#tlumaczenie("C:/Users/48667/Desktop/tekst.pdf")
audiobook("C:\\Users\\48667\\Desktop\\sql1.pdf")
#C:/Users/48667/Desktop/sql1.pdf