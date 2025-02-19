import tkinter as tk
import threading
from playsound import playsound
from PIL import Image, ImageTk
import keyboard  # Importar a biblioteca keyboard

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(1)  # Remove as bordas da janela
        self.root.geometry("75x75")  # Tamanho reduzido

        # Define o fundo como uma cor específica para torná-lo transparente
        self.root.config(bg="#000001")
        self.root.wm_attributes("-transparentcolor", "#000001")  # Torna o fundo transparente

        # Carregar e redimensionar a imagem do relógio
        self.image = Image.open("relogio.png").resize((48, 48), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        # Label para a imagem do relógio
        self.label = tk.Label(root, image=self.photo, bg="#000001")
        self.label.pack()

        # Label para o timer com contorno preto
        self.timer_label = tk.Label(root, text="2:00", font=("Helvetica", 12, "bold"), fg="white", bg="#000001")
        self.timer_label.place(relx=0.5, rely=0.9, anchor="center")

        # Variáveis de controle do tempo
        self.time_left = 120  # 2 minutos em segundos
        self.running = False

        # Atalhos de teclado funcionam mesmo se a janela não estiver selecionada
        keyboard.add_hotkey('space', self.toggle_timer)
        keyboard.add_hotkey('p', self.pause_timer)
        keyboard.add_hotkey('esc', self.close_timer)

        # Bind do mouse para arrastar
        self.root.bind("<B1-Motion>", self.move_window)  # Movimento com o mouse
        self.root.bind("<Control-B1-Motion>", self.move_window)  # Ctrl + arrastar

        # Iniciar o loop de atualização do timer
        self.update_timer()

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                mins, secs = divmod(self.time_left, 60)
                self.timer_label.config(text=f"{mins}:{secs:02}")

                # Reproduzir alerta sempre que o timer estiver em 10 segundos
                if self.time_left == 10:
                    threading.Thread(target=lambda: playsound("alerta.mp3")).start()  # Tocar som de alerta

                self.time_left -= 1  # Contagem regressiva
            else:
                self.time_left = 120  # Reinicia o timer para 2 minutos

        self.root.after(1000, self.update_timer)

    def toggle_timer(self):
        if not self.running:
            self.running = True
        else:
            self.pause_timer()

    def pause_timer(self):
        self.running = False

    def close_timer(self):
        self.root.quit()

    def move_window(self, event):
        if event.state & 0x4:  # Checa se a tecla Ctrl está pressionada
            x = self.root.winfo_pointerx() - 20  # Ajuste do posicionamento
            y = self.root.winfo_pointery() - 20
            self.root.geometry(f"+{x}+{y}")

# Configuração da janela principal
root = tk.Tk()
app = TimerApp(root)
root.mainloop()
