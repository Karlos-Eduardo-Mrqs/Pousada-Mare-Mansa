import tkinter as tk
from tkinter import ttk, messagebox
from controllers.control_usuario import Control_Usuario

class C:
# === CONFIGURAÇÃO DO CONTROLADOR E USUÁRIO INICIAL ===
    controller_usuario = Control_Usuario()

    # Insere usuário "admin" diretamente no banco, se não existir
    if not controller_usuario.autenticar("admin", "senha123"):
        controller_usuario.adicionar_usuario("admin", "admin@pousada.com", "senha123")

    # === Funções ===
    def create_image_with_border(path, size=(120, 120), border=4, border_color="#003366"):
        try:
            img = Image.open(path).resize(size, Image.Resampling.LANCZOS).convert("RGBA")
            bordered_img = ImageOps.expand(img, border=border, fill=border_color)
            return ImageTk.PhotoImage(bordered_img)
        except FileNotFoundError:
            print("Imagem de logo não encontrada.")
            return None

    def fazer_login():
        nome = entry_username.get().strip()
        senha = entry_password.get().strip()

        if not nome or not senha:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        usuario = controller_usuario.autenticar(nome, senha)
        if usuario:
            messagebox.showinfo("Login bem-sucedido", f"Bem-vindo, {usuario.nome}!")
            # Aqui você pode abrir a próxima tela ou funcionalidade que deseja
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    # === Janela principal ===
    root = tk.Tk()
    root.title("Tela de Login")
    root.geometry("700x500")
    root.configure(bg="#FAF1E4")

    # Cabeçalho
    header = tk.Frame(root, bg="#397A7B", height=75)
    header.pack(fill="x", side="top")

    # Rodapé
    footer = tk.Frame(root, bg="#397A7B", height=75)
    footer.pack(fill="x", side="bottom")

    # Logo com borda
    logo_img = create_image_with_border("LogoPousadaMare.png", size=(140, 140), border=2, border_color="#9B9B58")
    if logo_img:
        logo_label = tk.Label(root, image=logo_img, bg="#9B9B58")
        logo_label.place(relx=0.5, y=100, anchor="center")

    # Área de login
    frame_login = tk.Frame(root, bg="#FAF1E4")
    frame_login.place(relx=0.5, rely=0.53, anchor="center")

    tk.Label(frame_login, text="Usuário", bg="#FAF1E4").pack(pady=(0, 5))
    entry_username = ttk.Entry(frame_login, width=30)
    entry_username.pack(pady=(0, 15))

    tk.Label(frame_login, text="Senha", bg="#FAF1E4").pack(pady=(0, 5))
    entry_password = ttk.Entry(frame_login, show="*", width=30)
    entry_password.pack(pady=(0, 20))

    btn_login = ttk.Button(frame_login, text="Logar", command=fazer_login)
    btn_login.pack()

    # Inicia a interface
    root.mainloop()    