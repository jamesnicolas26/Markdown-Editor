import tkinter as tk
from tkinter import ttk
import markdown2

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Editor")

        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root, wrap="word", height=15, width=60)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text_area.bind("<KeyRelease>", self.update_preview)

        self.preview_pane = tk.Frame(self.root)
        self.preview_pane.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.preview_label = tk.Label(self.preview_pane, text="Preview", font=("Arial", 16))
        self.preview_label.pack(pady=10)

        self.preview_area = tk.Text(self.preview_pane, wrap="word", height=15, width=60, bg="white")
        self.preview_area.pack(expand=True, fill=tk.BOTH)
        self.preview_area.config(state=tk.DISABLED)

    def update_preview(self, event=None):
        markdown_text = self.text_area.get("1.0", tk.END)
        html_text = markdown2.markdown(markdown_text)
        self.preview_area.config(state=tk.NORMAL)
        self.preview_area.delete("1.0", tk.END)
        self.preview_area.insert(tk.END, html_text)
        self.preview_area.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
app = MarkdownEditor(root)
root.mainloop()
