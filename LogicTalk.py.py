from customtkinter import*
import threading















































def otprav ():
    CTkEntry.get()
    CTkEntry.delete(0, END)
    print("Mag: " + entry.get())

def otpravv ():
    CTkEntry.get()
    CTkEntry.delete(0, END)
    print("Kola: " + entry.get())




def novii ():
    CTkEntry.get()
    CTkEntry.delete(0, END)
    nov = CTk()
    nov.geometry('500x300')
    nov.title("Logic Talk 2")
    frama = CTkFrame(nov, fg_color="white")
    frama.place(relwidth=1, relheight=1)

    tex = CTkLabel(nov, text='Чат', font=('Arial', 14, 'bold'))
    tex.pack()

    textbo = CTkTextbox(nov, fg_color='white')
    textbo.place(relwidth=10, relheight=10)

    entr = CTkEntry(nov, placeholder_text='Введіть текст', font=('Arial', 14, 'bold'))
    entr.pack(padx=0, pady=0, )
    entr.place(x=90, y=240)

    butto = CTkButton(nov, text='Відправити', font=('Arial', 14, 'bold'), command=otpravv)
    butto.place(x=240, y=240)

    nov.mainloop()







av = CTk()
av.geometry('500x300')
av.title("Logic Talk")

frame = CTkFrame(av, fg_color='light blue')
frame.place(relwidth=1, relheight=1)

text = CTkLabel(av, text='Чат', font=('Arial', 14, 'bold'), text_color= 'light blue')
text.pack()

textbox = CTkTextbox(av, fg_color= 'white')
textbox.place(relwidth=10, relheight=10)

entry = CTkEntry(av, placeholder_text='Введіть текст', font = ('Arial', 14, 'bold'))
entry.pack(padx=0, pady = 0,)
entry.place(x=90, y=240)

button = CTkButton(av, text='Відправити', font = ('Arial', 14, 'bold'), command = otprav)
button.place(x=240, y=240)

pol = CTkButton(av, text='Зайти в інший аккаунт', font = ('Arial', 14, 'bold'), command = novii)
pol.place(x=320, y=5)




















av.mainloop()
