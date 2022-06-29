#region CÓDIGO
from tkinter import *

jan = Tk()                      # PROPRIEDADES DA JANELA ----
jan.title('SomaValores')
jan.geometry('300x200')
jan.resizable(False, False)

val1 = IntVar()                 # DECLARAÇÃO DAS VARIÁVEIS NUMÉRICAS(MODIFICÁVEIS) ----
val2 = IntVar()
result = IntVar()

ent1 = Entry(jan)               # FIXAÇÃO DAS 'Entrys' NA JANELA PRINCIPAL ----
ent1.place(x=75, y=25)

ent2 = Entry(jan)
ent2.place(x=75, y=60)


def update():                  # FUNÇÃO RESPONSÁVEL POR REDECLARAR AS VARIÁVEIS DE INTEIROS 'IntVar()' ----
    if ent1.get().removeprefix('-').removeprefix('+').isnumeric() is True\
     and ent2.get().removeprefix('-').removeprefix('+').isnumeric() is True:
        val1.set(int(ent1.get()))
        val2.set(int(ent2.get()))
        result.set((val1.get()) + (val2.get()))


update_btn = Button(text='Somar', command=update)     # BOTÕES, TEXTO E FECHAMENTO DO CÓDIGO ('jan.mainloop()')
update_btn.place(x=75, y=100)

lbl = Label(jan, textvariable=result, bg='#ADD8E6', fg='white')
lbl.place(x=190, y=100, width=50, height=40)

jan.mainloop()
#endregion
