from tkinter import*
from tkcalendar import *

def dia():
    print(cal.get())

eventos = {}
strEventos = ""
def addEvento():
    nome = txtEvento.get()
    date = str(cal.get())
    if not date in eventos:
        eventos[date] = {"00:00": "", "01:00": "", "02:00": "", "03:00": "", "04:00": "", "05:00": "", "06:00": "",
                     "07:00": "", "08:00": "", "09:00": "", "010:00": "", "11:00": "",
                     "12:00": "", "13:00": "", "14:00": "", "15:00": "", "16:00": "", "17:00": "", "18:00": "",
                     "19:00": "",
                     "20:00": "", "21:00": "", "22:00": "", "23:00": ""}
        print(eventos[date])
        print(eventos)
    #eventos[date][opcao.get] = nome


mycolor = '#%02x%02x%02x' % (105,13,13)

root=Tk()
root.title("Agenda")
root.geometry("350x300")
f1=Frame(root,width=500,height=20,relief=SUNKEN,bd=4,bg=mycolor)
f1.pack(side=TOP)
f2=Frame(root,width=500,height=550,relief=SUNKEN,bd=4,bg='white')
f2.pack()
root.iconbitmap(r'15may.ico')


#Creating the date column
l4=Label(f2,text='DATA',font=('Titillium Web',20,'bold'),fg='black',anchor='w')
l4.grid(row=0,column=3)

cal=DateEntry(f2,dateformat=3,width=12,date_pattern='dd/mm/yyyy' , background=mycolor,foreground='white', borderwidth=4,Calendar =2019, command=dia)
cal.grid(row=1,column=3,sticky='nsew')


# dropdown
horas = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00",
              "08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00",
              "16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]

opcao = StringVar(root)
opcao.set(horas[0])
opt = OptionMenu(root, opcao, *horas)
opt.config(width=29, font=('Helvetica', 12))
opt.pack()
def callback(*args):
    for hora in eventos[cal.get()]:
        strEventos += "➜" + hora +"\t" + eventos[cal.get()][hora]
    texto.set(strEventos)

opcao.trace('w', callback)


txtEvento = Entry(root, width = 50)
txtEvento.pack()

btCriar = Button(root, text="Adicionar Evento", command=addEvento)
btCriar.pack()


texto = StringVar()
lbl1 = Label(root, textvariable = texto)
lbl1.pack()



root.mainloop()