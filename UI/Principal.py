import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from UI.Componentes.Chat import ChatComponent

#region Ventana Principal
class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Simple")
        self.root.geometry("1024x720")
        self.root.resizable(False, False)

        self.chat = ChatComponent(self.root)
        self.chat.get_frame().pack(fill='both', expand=True)

        self.chat.send_btn.config(command=self._handle_send)
        self.chat.entry.bind('<Return>', lambda e: self._handle_send())


        self.chat.add_message("Hola, ¿puedes ayudarme con mi proyecto?", "Usuario")
        self.chat.add_message("Claro, dime qué necesitas y te ayudo paso a paso.", "Respuesta")
        self.chat.add_message("Quiero que el chat se vea más moderno.", "Usuario")
        self.chat.add_message("Perfecto. Ahora los mensajes aparecen como bocadillos alineados.", "Respuesta")

    def _handle_send(self):
        msg = self.chat.entry.get().strip()
        if msg:
            self.chat.add_message(msg, "Usuario")

            self.chat.add_message("Mensaje recibido. Esta es una respuesta de ejemplo.", "Respuesta")
            self.chat.entry.delete(0, 'end')
            
    def ejecutar(self):
        self.root.mainloop()
