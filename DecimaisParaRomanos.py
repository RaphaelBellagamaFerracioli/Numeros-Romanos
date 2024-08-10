
# Regras utilizadas para a construção do código

# Há repetição de letras até três vezes
    # o princípio subtrativo, e o princípio aditivo. Além disso, 
    # um traço sobre as letras indica a multiplicação do valor
    # por mil, ampliando assim a gama de números que podem ser representados.
    # Repetição de Letras: As letras I, X, C, e M podem ser repetidas até três
    # vezes consecutivas para formar números. Por exemplo, III = 3 e XXX = 30.
    # Princípio Subtrativo: Quando duas letras diferentes são colocadas em sequência
    # e a de menor valor precede a de maior valor, subtrai-se o valor da menor do
    # valor da maior. Exemplos incluem IV (4) e IX (9).
    # Princípio Aditivo: Quando letras são colocadas em sequência e a de maior
    # valor está antes da de menor valor, seus valores são somados. Exemplos incluem VI (6) e XV (15).
    # Multiplicação por 1.000: Colocar um traço sobre uma letra ou um grupo
    # de letras multiplica o valor por 1.000. Isso permite representar números grandes

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from backend.Conversor import Conversor 

class RomanApp:
    def __init__(self, root):
        self.root = root
        self.converter = Conversor()  # Instanciando o backend
        self.root.title("Conversor Decimal para Romano")
        self.root.geometry("800x600")  # Tamanho inicial da janela

        # Setup da imagem de fundo (garanta que a imagem exista no caminho especificado)
        try:
            self.original_image = Image.open('Logo-Demander.png')
            self.background_image = ImageTk.PhotoImage(self.original_image)
            self.background_label = tk.Label(root, image=self.background_image)
            self.background_label.place(relwidth=1, relheight=1)
            self.root.bind('<Configure>', self.resize_image)
        except Exception as e:
            print(e)

        # Configuração dos widgets
        self.label = tk.Label(root, text="Digite um número decimal:", bg='light blue')
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Converter", command=self.convert)
        self.button.pack(pady=10)

    def resize_image(self, event):
        new_width = self.root.winfo_width()
        new_height = self.root.winfo_height()
        image = self.original_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label.config(image=self.background_image)

    def convert(self):
        num = self.entry.get()
        try:
            num = int(num)
            if 0 < num <= 3999:
                resultado = self.converter.decimal_para_romano(num)
                messagebox.showinfo("Resultado", f"O número {num} em romano é {resultado}")
            else:
                messagebox.showwarning("Aviso", "Digite um número entre 1 e 3999.")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida. Por favor, digite um número decimal válido.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RomanApp(root)
    root.mainloop()