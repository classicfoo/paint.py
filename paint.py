import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tkinter Paint')
        
        self.old_x = None
        self.old_y = None
        self.line_width = 5
        self.color = 'black'
        self.eraser_on = False
        
        self.c = tk.Canvas(self.root, bg='white', width=800, height=600)
        self.c.pack(fill="both", expand=True)
        
        self.line_size_entry = tk.Entry(self.root)
        self.line_size_entry.insert(0, str(self.line_width))
        self.line_size_entry.pack(side=tk.LEFT, padx=10)

        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=10)
        
        self.eraser_button = tk.Button(self.root, text="Eraser", command=self.activate_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=10)
        
        self.brush_button = tk.Button(self.root, text="Brush", command=self.activate_brush)
        self.brush_button.pack(side=tk.LEFT, padx=10)

        # Add a Reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_canvas)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        try:
            self.line_width = int(self.line_size_entry.get())
        except ValueError:
            self.line_width = 2

        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
    
    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        self.eraser_on = False
        self.color = colorchooser.askcolor(color=self.color)[1]

    def activate_eraser(self):
        if self.eraser_on is not True:
            self.eraser_on = True

    def activate_brush(self):
        self.eraser_on = False

    def reset_canvas(self):
        # Clear the canvas
        self.c.delete("all")

if __name__ == '__main__':
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()
