# Projeto: Criando uma calculadora de idade funcional com Python

# importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk

# importando tkcalendar
from tkcalendar import Calendar, DateEntry

# importanto relativedelta
from dateutil.relativedelta import relativedelta

# importando datetime
from datetime import date

# criando a janela
janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry('310x400')

# cores que usaremos
cor1 = '#000000' # preto
cor2 = '#474343' # cinza
cor3 = '#ffffff' # branco
cor4 = '#fa8b02' # laranja

# criando frames (dividindo a janela em duas partes)
frame_cima = Frame(janela, width=310, height= 140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height= 260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1, column=0)

# criando labels para frame cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor1, fg=cor4)
l_idade.place(x=0, y=70)


# criando labels para frame baixo
l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivy 11'), bg=cor2, fg=cor3)
l_data_inicial.place(x=40, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg='white', borderwidth=2, date_pattern='dd/mm/yyyy', y=2025)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de Nascimento", height=1, padx=0, pady=0, relief='flat', anchor='nw', font=('Ivy 11'), bg=cor2, fg=cor3)
l_data_nascimento.place(x=40, y=60)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg='white', borderwidth=2, date_pattern='dd/mm/yyyy')
cal_2.place(x=180, y=60)

# label para os anos
l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Ano(s)", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_app_anos_nome.place(x=55, y=175)

# label para os meses
l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Mes(es)", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_app_meses_nome.place(x=130, y=175)

# label para os dias
l_app_dias = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="Dia(s)", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=cor2, fg=cor3)
l_app_dias_nome.place(x=220, y=175)

# criando funcao para calcular a idade
def calcular():
    inicial=cal_1.get()
    termino=cal_2.get()
    
    # separando os valores
    dia_1, mes_1, ano_1 = [ int(f) for f in inicial.split('/')]
    
    # convertendo os valores em formato date/datetime
    data_inicial = date(ano_1, mes_1, dia_1)

    # separando os valores
    dia_2, mes_2, ano_2 = [ int(f) for f in termino.split('/')]

    # convertendo os valores em formato date/datetime
    data_nascimento = date(ano_2, mes_2, dia_2)

    # years para diferença entre anos, months para mes e days para dias
    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days
    
    # imprimindo na tela
    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias

    # imprimindo no terminal
    print(anos, "ano(s),", meses, "mes(es),", dias, "dia(s).")

# criando botao para calcular
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', font=('Ivy 10 bold'), bg=cor2, fg=cor3)
b_calcular.place(x=70, y=225)


janela.mainloop()