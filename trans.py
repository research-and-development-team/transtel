try:

    from textblob import TextBlob

    import textblob

    import tkinter as tk

    import sys,os

except:

    os.system("pip3 install tkinter")

    os.system("pip3 install textblob")

arka = tk.Tk() #burda ilk pencere adimlari

arka.title("Spy çeviri uygulamasî")# pencere başligi 

arka.geometry("450x400")

def cevir():

    cumle = tb1.get(1.0,tk.END)

    text = TextBlob(cumle)

    ceviri_kelime =  text.translate(to="fr")

    tb2.delete(1.0,tk.END)

    tb2.insert(tk.END,ceviri_kelime)

    

  

def temizle():

    tb1.delete(1.0,tk.END)

    tb1.delete(1.0, tk.END) 

    

def cik():

    sys.exit()

    

    

qw = tk.Label(text="TRANSTELE HOŞ GELDİNİZ!",font="Verdana 12 bold underline ",fg="green")

qw.place(x=40,y=90)

e1 = tk.Label(text="English",font="Times 9 roman ",fg="green")

e1.place(x=45,y=300)

e2 = tk.Label(text="Fransizca",font="Times 9 roman",fg="green")

e2.place(x=350,y=300)

tb1 = tk.Text(width=23,height=7)

tb1.place(x=40,y=400)

tb2 = tk.Text(width=20,height=7)

tb2.place(x=350,y=400)

btn1 = tk.Button(text="Transtel",fg="green",font="Times  9 roman ",command=cevir)

btn1.place(x=49,y=700)

btn2 = tk.Button(text="clear ",font="Times 9 roman ",fg="green",command=temizle)

btn2.place(x=300,y=700)

bu = tk.Button(text="Çık",fg="Red",font="Times 9 roman",command=cik)

bu.place(x=49,y=800)

arka.mainloop()
