'''
Created on 12 de set. de 2024

@author: Mescxll
'''

from tkinter import *

#Cores

cor0= "#F3F1F1" #branco
cor1= "#000000" #preto
cor2="#2F2F2F" #cinza escuro
cor3= "#BABABA" #cinza claro
cor4= "#310D66" #roxo

#Janela e Frames

janela = Tk()
janela.title("Calculadora")
janela.geometry("240x300")
janela.config(bg=cor1)

frameDaTela = Frame(janela, width=240, height=50, bg=cor2)
frameDaTela.grid(row=0, column=0)
frameDoCorpo = Frame(janela, width=240, height=250)
frameDoCorpo.grid(row=1, column=0)

#Variável auxiliar e método para mostrar valores na interface

valores = " "

# Lógica

def mostrar(Event): 
    global valores
    valores = valores + str(Event)
    textoValor.set(valores)

def calcular():
    global valores
    resultado = eval(valores)  
    textoValor.set(str(resultado))

def limpar():
    global valores
    valores = ""
    textoValor.set("")
    
#Visor

textoValor = StringVar()

visor = Label(frameDaTela, textvariable= textoValor, width=16, height=2, padx= 7, relief= FLAT, anchor= "e", justify=RIGHT, font= ('Ivy 18'), bg= cor2, fg= cor0)
visor.place(x=0, y=0)

#Botões

botao1 = Button(frameDoCorpo,command= limpar, text="AC", width=12, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao1.place(x=0, y=0)
botao2 = Button(frameDoCorpo, command= lambda: mostrar("%"), text="%", width=5, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao2.place(x=122, y=0)
botao3 = Button(frameDoCorpo, command= lambda: mostrar("/"), text="÷", width=5, height=2, bg= cor4, fg= cor0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao3.place(x=180, y=0)
botao4 = Button(frameDoCorpo, command= lambda: mostrar("7"), text="7", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao4.place(x=-2, y=50)
botao5 = Button(frameDoCorpo, command= lambda: mostrar("8"), text="8", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao5.place(x=58, y=50)
botao6 = Button(frameDoCorpo, command= lambda: mostrar("9"), text="9", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao6.place(x=122, y=50)
botao7 = Button(frameDoCorpo, command= lambda: mostrar("*"), text="x", width=5, height=2, bg= cor4, fg= cor0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=180, y=50)

botao8 = Button(frameDoCorpo, command= lambda: mostrar("4"), text="4", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=-2, y=100)
botao9 = Button(frameDoCorpo, command= lambda: mostrar("5"), text="5", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=58, y=100)
botao10 = Button(frameDoCorpo, command= lambda: mostrar("6"), text="6", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao10.place(x=122, y=100)
botao11 = Button(frameDoCorpo, command= lambda: mostrar("-"), text="-", width=5, height=2, bg= cor4, fg= cor0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao11.place(x=180, y=100)

botao12 = Button(frameDoCorpo, command= lambda: mostrar("1"), text="1", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao12.place(x=-2, y=150)
botao13 = Button(frameDoCorpo, command= lambda: mostrar("2"), text="2", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao13.place(x=58, y=150)
botao14 = Button(frameDoCorpo, command= lambda: mostrar("3"), text="3", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao14.place(x=122, y=150)
botao15 = Button(frameDoCorpo, command= lambda: mostrar("+"), text="+", width=5, height=2, bg= cor4, fg= cor0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao15.place(x=180, y=150)

botao16 = Button(frameDoCorpo, command= lambda: mostrar("0"), text="0", width=12, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao16.place(x=0, y=200)
botao17 = Button(frameDoCorpo, command= lambda: mostrar("."), text=".", width=6, height=2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao17.place(x=122, y=200)
botao18 = Button(frameDoCorpo, command= calcular, text="=", width=5, height=2, bg= cor4, fg= cor0, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao18.place(x=180, y=200)

#Fim do loop

janela.mainloop()