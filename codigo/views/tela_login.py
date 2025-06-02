import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageOps
from controllers.control_usuario import Control_Usuario
from controllers.banco import Banco
from models.logs_json import LoggerJSON

class TelaLogin:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.logger = LoggerJSON()
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
            self.logger.registrar("Sistema", "Usuário administrador criado automaticamente", "Login.py", "AUDIT")
            self.controller_usuario.adicionar_usuario("admin", "admin@pousada.com", "senha123")

    def construir_interface(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg="#397A7B", height=75)
        header.pack(fill="x", side="top")
        
        # Logo com borda
        self.logo_img = self.create_image_with_border("codigo/LogoPousadaMare.png",
                                                    size=(160, 160), border=2,
                                                    border_color="#9B9B58")
        if self.logo_img:
            logo_label = tk.Label(self.root, image=self.logo_img, bg="#9B9B58")
            logo_label.place(relx=0.5, y=100, anchor="center")

        # Área de login
        frame_login = tk.Frame(self.root, bg="#FAF1E4")
        frame_login.place(relx=0.5, rely=0.53, anchor="center")

        tk.Label(frame_login, text="Usuário", bg="#FAF1E4", font=("Helvetica", 10)).pack(pady=(0, 5))
        self.entry_username = ttk.Entry(frame_login, width=30)
        self.entry_username.pack(pady=(0, 15))
        self.entry_username.focus()

        tk.Label(frame_login, text="Senha", bg="#FAF1E4", font=("Helvetica", 10)).pack(pady=(0, 5))
        self.entry_password = ttk.Entry(frame_login, show="*", width=30)
        self.entry_password.pack(pady=(0, 10))

        self.show_password = tk.BooleanVar()
        # Estilo para o Checkbutton
        style = ttk.Style()
        style.configure("Custom.TCheckbutton",background="#FAF1E4",foreground="#333333",font=("Helvetica", 10))

        self.show_password = tk.BooleanVar()
        show_btn = ttk.Checkbutton(frame_login,text="👁 Mostrar senha",variable=self.show_password,command=self.toggle_password,style="Custom.TCheckbutton")
        show_btn.pack(pady=(0, 12))

        # Botão de login com padding e largura fixa
        btn_login = ttk.Button(frame_login,text="🔒 Entrar",command=self.fazer_login)
        btn_login.pack(pady=(0, 15), ipadx=15, ipady=5)

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
        except Exception as erro:
            self.logger.registrar(f"Sistema", "Falha ao carregar a imagem {erro}","Login.py", "WARN")
            return None

    def fazer_login(self):
        nome = self.entry_username.get().strip()
        senha = self.entry_password.get().strip()

        if not nome or not senha:
            self.logger.registrar("Sistema", "Realizar Login com campos vazios","Login.py","ERROR")
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        usuario = self.controller_usuario.autenticar(nome, senha)
        if usuario:
            self.logger.registrar("Sistema", "login bem sucedido","Login.py" ,"INFO")
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {usuario.nome}!")
            self.app.abrir_tela_menu()
        else:
            self.logger.registrar("Sistema", "Falha ao realizar login","Login.py", "ERROR")
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")
            

# Execução direta para testes
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root, None)
    root.mainloop()