def print_hi(name):

    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import math

def calculate_y(x, eps):
    """
    первая функция y(x) через ряд тейлора:
    y(x) = 2 * (q + q^3/3 + q^5/5 + ...), где q = (x-1)/(x+1)
    """
    q = (x - 1) / (x + 1)

    term = q
    total_sum = 0.0
    n = 0

    max_iterations = 100000

    while abs(term) > eps and n < max_iterations:
        total_sum += term
        n += 1
        term = term * (q ** 2) * (2 * n - 1) / (2 * n + 1)

    return 2 * total_sum

def calculate_z(x, b):
    """Вторая функция z(x) = ln(x) + b"""
    return math.log(x) + b

def plot_graphs():
    try:
        xn = float(entry_xn.get())
        xk = float(entry_xk.get())
        dx = float(entry_dx.get())
        eps = float(entry_eps.get())
        b = float(entry_b.get())

        # Проверки на корректность ввода x > 0
        if xn <= 0:
            messagebox.showerror("ошибка", "начальное значение x (xn) должно быть > 0, так как x > 0")
            return
        if xk <= xn:
            messagebox.showerror("ошибка", "конечное значение x (xk) должно быть больше начального (xn)")
            return
        if dx <= 0 or eps <= 0:
            messagebox.showerror("ошибка", "Шаг (dx) и точность (eps) должны быть больше нуля")
            return

        x_vals = []
        current_x = xn

        while current_x <= xk + 1e-9:
            x_vals.append(current_x)
            current_x += dx
        # ----------------------------------------------------

        y_vals = [calculate_y(x, eps) for x in x_vals]
        z_vals = [calculate_z(x, b) for x in x_vals]

        ax.clear()

        ax.plot(x_vals, y_vals, label='y(x) - ряд тейлора', color='blue', linewidth=2)
        ax.plot(x_vals, z_vals, label=f'z(x) = ln(x) + {b}', color='red', linestyle='--', linewidth=2)

        ax.set_title('график функций вариант 11', fontsize=14, fontweight='bold')
        ax.set_xlabel('значение x', fontsize=12)
        ax.set_ylabel('значение y и z', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(fontsize=11)

        ax.relim()
        ax.autoscale_view()

        fig.tight_layout()

        canvas.draw()

    except ValueError:
        messagebox.showerror("Ошибка", "пожалуйста, введите корректны значения.")

root = tk.Tk()
root.title("лабораторная работа N8 вариант 11")

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{int(screen_w * 0.85)}x{int(screen_h * 0.85)}")
root.minsize(800, 600)

# ввод данных
input_frame = ttk.LabelFrame(root, text=" параметры задачи ", padding=10)
input_frame.pack(fill=tk.X, padx=10, pady=5)

ttk.Label(input_frame, text="xn (начало):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_xn = ttk.Entry(input_frame, width=10)
entry_xn.insert(0, "0.1")
entry_xn.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="xk (конец):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_xk = ttk.Entry(input_frame, width=10)
entry_xk.insert(0, "5.0")
entry_xk.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(input_frame, text="dx (шаг):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
entry_dx = ttk.Entry(input_frame, width=10)
entry_dx.insert(0, "0.1")
entry_dx.grid(row=0, column=5, padx=5, pady=5)

ttk.Label(input_frame, text="eps (точность):").grid(row=0, column=6, padx=5, pady=5, sticky="e")
entry_eps = ttk.Entry(input_frame, width=10)
entry_eps.insert(0, "0.0001")
entry_eps.grid(row=0, column=7, padx=5, pady=5)

ttk.Label(input_frame, text="b (параметр):").grid(row=0, column=8, padx=5, pady=5, sticky="e")
entry_b = ttk.Entry(input_frame, width=10)
entry_b.insert(0, "1.0")
entry_b.grid(row=0, column=9, padx=5, pady=5)

# кнопка
btn_plot = ttk.Button(input_frame, text="ПОСТРОИТЬ ГРАФИКИ", command=plot_graphs)
btn_plot.grid(row=0, column=10, padx=15, pady=5)

# панель графика
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas, plot_frame)
toolbar.update()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()