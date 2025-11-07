from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os

class image_histogram_app:
    def __init__ (self, root):
        self.root = root
        self.root.title = ("Image Histogram Viewer")
        self.root.geometry("1200x900")

        self.image = None

        self.create_widgets()


    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = image_histogram_app(root)
    root.mainloop()