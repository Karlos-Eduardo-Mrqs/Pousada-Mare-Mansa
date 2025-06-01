import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageOps
from controllers.control_usuario import Control_Usuario
from controllers.banco import Banco

class TelaLogin:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Tela de Login - Pousada Maré Mansa")
        self.root.geometry("700x500")
        self.root.configure(bg="#FAF1E4")

        self.conn = Banco()
        self.conn.conectar()  # conecta explicitamente, já que o Banco ainda não foi usado
        self.controller_usuario = Control_Usuario(self.conn.conn)
        self.garantir_admin()
        self.construir_interface()

    def garantir_admin(self):
        if not self.controller_usuario.autenticar("admin", "senha123"):
            self.controller_usuario.adicionar_usuario("admin", "admin@pousada.com", "senha123")

    def construir_interface(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg="#397A7B", height=60)
        header.pack(fill="x", side="top")
        tk.Label(header, text="Pousada Maré Mansa", font=("Helvetica", 20, "bold"), bg="#397A7B", fg="white").pack(pady=10)

        # Logo com borda
        self.logo_img = self.create_image_with_border("codigo/LogoPousadaMare.png", size=(120, 120), border=3, border_color="#9B9B58")
        if self.logo_img:
            logo_label = tk.Label(self.root, image=self.logo_img, bg="#FAF1E4")
            logo_label.place(relx=0.5, rely=0.25, anchor="center")

        # Área de login centralizada
        frame_login = tk.Frame(self.root, bg="#FFFFFF", bd=2, relief="groove")
        frame_login.place(relx=0.5, rely=0.6, anchor="center")

        tk.Label(frame_login, text="Usuário", bg="#FFFFFF", font=("Helvetica", 10)).pack(pady=(15, 5))
        self.entry_username = ttk.Entry(frame_login, width=30)
        self.entry_username.pack(pady=(0, 10))
        self.entry_username.focus()

        tk.Label(frame_login, text="Senha", bg="#FFFFFF", font=("Helvetica", 10)).pack(pady=(0, 5))
        self.entry_password = ttk.Entry(frame_login, show="*", width=30)
        self.entry_password.pack(pady=(0, 10))

        self.show_password = tk.BooleanVar()
        show_btn = ttk.Checkbutton(frame_login, text="Mostrar senha", variable=self.show_password, command=self.toggle_password)
        show_btn.pack(pady=(0, 10))

        ttk.Button(frame_login, text="Entrar", command=self.fazer_login).pack(pady=(0, 15))

        # Rodapé
        footer = tk.Frame(self.root, bg="#397A7B", height=40)
        footer.pack(fill="x", side="bottom")
        tk.Label(footer, text="© 2025 Pousada Maré Mansa", bg="#397A7B", fg="white", font=("Helvetica", 9)).pack(pady=10)

    def toggle_password(self):
        self.entry_password.config(show="" if self.show_password.get() else "*")

    def create_image_with_border(self, path, size=(120, 120), border=4, border_color="#003366"):
        try:
            img = Image.open(path).resize(size, Image.Resampling.LANCZOS).convert("RGBA")
            bordered_img = ImageOps.expand(img, border=border, fill=border_color)
            return ImageTk.PhotoImage(bordered_img)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            return None

    def fazer_login(self):
        nome = self.entry_username.get().strip()
        senha = self.entry_password.get().strip()

        if not nome or not senha:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        usuario = self.controller_usuario.autenticar(nome, senha)
        if usuario:
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {usuario.nome}!")
            self.app.abrir_tela_menu()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

# Execução direta para testes
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root, None)
    root.mainloop()