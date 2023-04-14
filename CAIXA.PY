import pygetwindow
import mysql.connector
import customtkinter as ctk
from tkinter import messagebox
from pyautogui import hotkey

# conexão com o banco de dados

conexão = mysql.connector.connect(
    user= 'root',
    host= 'localhost',
    password='1928755c',
    database='cadastro'
)

cursor = conexão.cursor()

# primeira janela (MENU)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
primeira_janela = ctk.CTk()
primeira_janela.geometry('700x500')
primeira_janela.title('MENU')
 

# criando o menu da primeira pagina 

def função(escolha):
    
    if escolha == 'Inserir Produto':
        hotkey('alt', 'space', 'n')
        segunda_janela = ctk.CTkToplevel(primeira_janela)
        segunda_janela.geometry('500x300')
        segunda_janela.title('INSERIR DADOS')
        entrada_produto = ctk.CTkEntry(segunda_janela, 
                                       fg_color='transparent', placeholder_text='Insira o produto')
        entrada_produto.pack(padx=10, pady=10)



        entrada_valor = ctk.CTkEntry(segunda_janela, 
                                     placeholder_text='Insira o valor do produto', fg_color='transparent')
        entrada_valor.pack()



        
        def ir():
            from random import randint
            lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  'I','J']
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random =[ (randint(1, 9)), (randint(1, 9)), (randint(1, 9)), (randint(1, 9)), (randint(1, 9))]
            id = []
            r1 = random[0]
            r2 = random[1]
            r3 = random[2]
            r4 = random[3]
            r5 = random[4]
            id.append([f'{lista[randint(1,9)]}', f'{num[randint(0,8)]}', f'{lista[randint(1,9)]}', f'{lista[randint(1,9)]}', f'{num[randint(1,9)]}'])
            juntar = ''.join(*id)
            juntar = str(juntar)
            
            
            comando = f'INSERT INTO açaí(produto, valor, Identificar) VALUES ("{entrada_produto.get()}", {entrada_valor.get()},"{juntar}")'
            cursor.execute(comando)
            conexão.commit()
            
            messagebox.showinfo('CONCLUÍDO', f'Seu produto foi inserido com sucesso!\nID CLIENTE: {juntar}')
            id.clear()
        def menu():
            segunda_janela.destroy()
            win = pygetwindow.getWindowsWithTitle('MENU')[0]
            win.restore()

        botão_enviar = ctk.CTkButton(segunda_janela,        
                                     text='Enviar', fg_color='transparent',hover_color='green',
                                     command= ir)
        botão_enviar.pack(padx=10, pady=10)


        botão_menu = ctk.CTkButton(segunda_janela,
        text='Menu', fg_color='transparent',hover_color='blue',
        command=menu)
        botão_menu.pack(padx=10, pady=10)







    elif escolha == 'Deletar Produto':
        hotkey('alt', 'space', 'n')
        terceira_janela = ctk.CTkToplevel()
        terceira_janela.geometry('500x300')
        terceira_janela.title('DELETAR PRODUTO')

        id_deletar = ctk.CTkEntry(terceira_janela, placeholder_text='Id do cliente', fg_color= 'transparent')
        id_deletar.pack(padx=50, pady=50)

        def dell():
            comando = f'DELETE FROM açaí WHERE Identificar = "{id_deletar.get()}"'
            cursor.execute(comando)
            conexão.commit()
            messagebox.showinfo('DELETADO', 'Seu produto foi deletado com sucesso!')

        botão_deletar = ctk.CTkButton(terceira_janela, text='OK', fg_color='transparent', hover_color='green', command=dell)
        botão_deletar.pack(padx=10, pady=10)
        

        def menu():
            titulo = 'MENU'
            terceira_janela.destroy()
            win = pygetwindow.getWindowsWithTitle(titulo)[0]
            win.restore()
        botão_menu = ctk.CTkButton(terceira_janela, text='MENU', fg_color='transparent', hover_color='blue', command=menu)
        botão_menu.pack(padx=10, pady=10)


frame = ctk.CTkFrame(primeira_janela, width=400, height=300, corner_radius=25).grid(row=0,column=0, padx=150, pady=100)
label_menu = ctk.CTkLabel(primeira_janela, text='SUAS OPÇÕES')
opção = ['Inserir Produto', 'Deletar Produto']
menu = ctk.CTkOptionMenu(frame, values= opção, button_hover_color=('green'), command=função)
menu.set('O QUE DESEJA FAZER?')
menu.grid(row=0,column=0, padx=10, pady=10)




# botão de sair da primeira pagina 

def sair():
    primeira_janela.quit()

botão = ctk.CTkButton(frame, text='Sair', command=sair, hover_color=('red') )
botão.grid(row=1, column=1, padx=20, pady=20)




# segunga página:




primeira_janela.mainloop()
conexão.close()
cursor.close()