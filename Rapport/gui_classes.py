import tkinter as tk
from tkinter import ttk 
import numpy as np

class GUI(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("500x400")
    
class ScrollableFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Configure scrolling
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), 'units'))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # self.bind("<Configure>", self.update_size)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame.bind("<Configure>", lambda e: self.update_scroll_region())

        # Layout
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill="both", expand=True)

        

    def update_scroll_region(self):
        self.update_idletasks()  
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

