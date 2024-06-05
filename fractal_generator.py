import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FractalGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Fractal Generator")
        self.master.geometry("800x600")
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("TLabel", font=("Helvetica", 14))
        
        self.create_widgets()
        
        # Initial fractal parameters
        self.fractal_type = None
        self.x_min, self.x_max, self.y_min, self.y_max = -2.0, 1.5, -2.0, 1.5
        self.width, self.height = 800, 600
        self.max_iter = 100
        self.zoom_factor = 0.6
        self.move_factor = 0.3

        self.master.bind("<KeyPress>", self.on_key_press)

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label
        self.label = ttk.Label(main_frame, text="Wähle ein Fraktal:")
        self.label.pack(pady=10)

        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        # Buttons
        self.mandelbrot_button = ttk.Button(button_frame, text="Mandelbrot",
                                             command=lambda: self.generate_fractal("Mandelbrot"))
        self.mandelbrot_button.grid(row=0, column=0, padx=10)

        self.julia_button = ttk.Button(button_frame, text="Julia-Menge",
                                       command=lambda: self.generate_fractal("Julia"))
        self.julia_button.grid(row=0, column=1, padx=10)

        self.burning_ship_button = ttk.Button(button_frame, text="Burning Ship Fractal",
                                        command=lambda: self.generate_fractal("Burning Ship"))
        self.burning_ship_button.grid(row=0, column=2, padx=10)

        # Canvas for displaying fractals
        self.figure = plt.Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=main_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def generate_fractal(self, fractal_type):
        self.fractal_type = fractal_type
        self.x_min, self.x_max, self.y_min, self.y_max = -2.0, 1.5, -2.0, 1.5  # Reset zoom and position
        self.draw_fractal()

    def draw_fractal(self):
        # Clear previous fractal
        self.ax.clear()

        # Generate fractal
        if self.fractal_type == "Mandelbrot":
            self.draw_mandelbrot()
        elif self.fractal_type == "Julia":
            self.draw_julia()
        elif self.fractal_type == "Burning Ship":
            self.draw_burning_ship()

        self.canvas.draw()

    def draw_mandelbrot(self):
        # Parameters for Mandelbrot set
        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        Z = np.zeros_like(C)
        img = np.zeros(C.shape, dtype=int)

        for i in range(self.max_iter):
            Z = Z**2 + C
            mask = (abs(Z) > 2) & (img == 0)
            img[mask] = i

        self.ax.imshow(img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')

    def draw_julia(self):
        # Parameters for Julia set
        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        c = complex(-0.7, 0.27015)
        img = np.zeros(Z.shape, dtype=int)

        for i in range(self.max_iter):
            Z = Z**2 + c
            mask = (abs(Z) > 2) & (img == 0)
            img[mask] = i

        self.ax.imshow(img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')

    def draw_burning_ship(self):
        # Parameters for Burning Ship fractal
        x = np.linspace(self.x_min, self.x_max, self.width)
        y = np.linspace(self.y_min, self.y_max, self.height)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        Z = np.zeros_like(C)
        img = np.zeros(C.shape, dtype=int)

        for i in range(self.max_iter):
            Z = (np.abs(Z.real) + 1j * np.abs(Z.imag))**2 + C
            mask = (abs(Z) > 2) & (img == 0)
            img[mask] = i

        self.ax.imshow(img, extent=[self.x_min, self.x_max, self.y_min, self.y_max], cmap='inferno')

    def on_key_press(self, event):
        if event.keysym == "plus" or event.keysym == "KP_Add":
            self.zoom_in()
        elif event.keysym == "minus" or event.keysym == "KP_Subtract":
            self.zoom_out()
        elif event.keysym == "Left":
            self.move_left()
        elif event.keysym == "Right":
            self.move_right()
        elif event.keysym == "Down":
            self.move_up()
        elif event.keysym == "Up":
            self.move_down()

    def zoom_in(self):
        x_center = (self.x_min + self.x_max) / 2
        y_center = (self.y_min + self.y_max) / 2
        x_range = (self.x_max - self.x_min) * self.zoom_factor
        y_range = (self.y_max - self.y_min) * self.zoom_factor
        self.x_min, self.x_max = x_center - x_range / 2, x_center + x_range / 2
        self.y_min, self.y_max = y_center - y_range / 2, y_center + y_range / 2
        self.draw_fractal()

    def zoom_out(self):
        x_center = (self.x_min + self.x_max) / 2
        y_center = (self.y_min + self.y_max) / 2
        x_range = (self.x_max - self.x_min) / self.zoom_factor
        y_range = (self.y_max - self.y_min) / self.zoom_factor
        self.x_min, self.x_max = x_center - x_range / 2, x_center + x_range / 2
        self.y_min, self.y_max = y_center - y_range / 2, y_center + y_range / 2
        self.draw_fractal()

    def move_left(self):
        x_range = self.x_max - self.x_min
        self.x_min -= x_range * self.move_factor
        self.x_max -= x_range * self.move_factor
        self.draw_fractal()

    def move_right(self):
        x_range = self.x_max - self.x_min
        self.x_min += x_range * self.move_factor
        self.x_max += x_range * self.move_factor
        self.draw_fractal()

    def move_up(self):
        y_range = self.y_max - self.y_min
        self.y_min += y_range * self.move_factor
        self.y_max += y_range * self.move_factor
        self.draw_fractal()

    def move_down(self):
        y_range = self.y_max - self.y_min
        self.y_min -= y_range * self.move_factor
        self.y_max -= y_range * self.move_factor
        self.draw_fractal()

def main():
    root = tk.Tk()
    fractal_app = FractalGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
