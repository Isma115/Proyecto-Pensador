import tkinter as tk
from tkinter import scrolledtext
import tkinter.ttk as ttk

#region Chat completo

class ChatComponent:
    
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#121212")


        self.chat_area = tk.Frame(self.frame, bg="#121212")
        self.chat_area.pack(fill="both", expand=True, padx=10, pady=10)


        self.canvas = tk.Canvas(self.chat_area, bg="#121212", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(
            self.chat_area,
            orient="vertical",
            command=self.canvas.yview,
            style="Dark.Vertical.TScrollbar"
        )
        self.messages_frame = tk.Frame(self.canvas, bg="#f4f4f4")
        self.messages_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.messages_frame,
            anchor="nw"
        )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width)
        )

        self.input_frame = tk.Frame(self.frame, bg="#121212")
        self.input_frame.pack(fill='x', padx=10, pady=(0, 10))

        self.entry = tk.Entry(
            self.input_frame,
            font=("Segoe UI", 13),
            bg="#1f1f1f",
            fg="#eeeeee",
            insertbackground="#eeeeee",
            relief="flat"
        )
        self.send_btn = tk.Button(self.input_frame, text="Enviar", font=("Segoe UI", 11))

        self.entry.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.send_btn.pack(side='right', padx=5, pady=5)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "Dark.Vertical.TScrollbar",
            background="#1f1f1f",
            darkcolor="#1f1f1f",
            lightcolor="#1f1f1f",
            troughcolor="#121212",
            bordercolor="#121212",
            arrowcolor="#eeeeee",
            relief="flat",
            borderwidth=0
        )
        self.style.map(
            "Dark.Vertical.TScrollbar",
            background=[("active", "#333333"), ("pressed", "#333333")]
        )
    def get_frame(self):
        return self.frame


    def _draw_rounded_rect(self, canvas, x1, y1, x2, y2, radius=18, **kwargs):
        fill = kwargs.get("fill", "#333333")
    
        canvas.create_rectangle(
            x1 + radius, y1,
            x2 - radius, y2,
            fill=fill,
            outline="",
            width=0
        )
        canvas.create_rectangle(
            x1, y1 + radius,
            x2, y2 - radius,
            fill=fill,
            outline="",
            width=0
        )
    
        canvas.create_oval(
            x1, y1,
            x1 + radius * 2, y1 + radius * 2,
            fill=fill,
            outline="",
            width=0
        )
        canvas.create_oval(
            x2 - radius * 2, y1,
            x2, y1 + radius * 2,
            fill=fill,
            outline="",
            width=0
        )
        canvas.create_oval(
            x1, y2 - radius * 2,
            x1 + radius * 2, y2,
            fill=fill,
            outline="",
            width=0
        )
        canvas.create_oval(
            x2 - radius * 2, y2 - radius * 2,
            x2, y2,
            fill=fill,
            outline="",
            width=0
        )

    def add_message(self, text, sender="Usuario"):

        is_user = sender.lower() == "usuario"

        row = tk.Frame(self.messages_frame, bg="#121212")
        row.pack(fill="x", padx=10, pady=8)

        bubble_color = "#3f5f5b" if is_user else "#4b425f"
        text_color = "#f2f2f2"
        anchor_side = "e" if is_user else "w"

        bubble_canvas = tk.Canvas(
            row,
            width=520,
            height=10,
            bg="#121212",
            highlightthickness=0,
            bd=0,
            borderwidth=0,
            relief="flat",
            takefocus=0
        )

        text_id = bubble_canvas.create_text(
            18,
            14,
            text=text,
            font=("Segoe UI", 14),
            fill=text_color,
            anchor="nw",
            width=440
        )

        bbox = bubble_canvas.bbox(text_id)
        bubble_width = bbox[2] - bbox[0] + 36
        bubble_height = bbox[3] - bbox[1] + 28

        bubble_canvas.config(width=bubble_width, height=bubble_height)

        self._draw_rounded_rect(
            bubble_canvas,
            2,
            2,
            bubble_width - 2,
            bubble_height - 2,
            radius=20,
            fill=bubble_color,
            outline=bubble_color
        )

        bubble_canvas.tag_raise(text_id)

        bubble_canvas.pack(
            anchor=anchor_side,
            padx=(80, 0) if is_user else (0, 80)
        )

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

#endregion