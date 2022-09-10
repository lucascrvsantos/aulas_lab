import tkinter as tk

def botao_click():
    nome = entry.get()
    nome_mod = ''
    for i, letra in enumerate(nome):
        if i % 2 == 0:
            nome_mod += letra.upper()
        else:
            nome_mod += letra.lower()
    label_result['text'] = nome_mod
            

root = tk.Tk()
root['borderwidth'] = 10
root.title('Exemplo1')

label_name = tk.Label(root, text='name: ')
entry = tk.Entry(root)
botao = tk.Button(root, text='tinfulinfular')
label_result = tk.Label(root)
botao['command'] = botao_click


label_name.pack(expand = True)
entry.pack(expand = True)
botao.pack(pady = 30)
label_result.pack(expand = True)

#tamanho minimo da janela
root.update() #desenha uma vez
x, y = root.winfo_width(), root.winfo_height()
#root.state('zoomed') #windowsOnly
root.attributes('-fullscreen', True) # All Systems


root.mainloop() #abre uma janelinha
