import serial
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import matplotlib.pyplot as plt
import tkinter as tk


# ser = serial.Serial('COM11', 115200)
ser.flushInput()

def update_plot(frame):
    data = ser.readline().decode('utf-8').strip()  # Leitura dos dados via serial
    try:
        data = float(data)
        y_data.append(data)
        y_data.popleft()  # Remover o ponto mais antigo para manter um número constante de pontos
        line.set_ydata(y_data)
        return line,
    except ValueError:
        pass
    return line,

fig, ax = plt.subplots()
y_data = deque([0] * 500)  # Manter os últimos 100 pontos
line, = ax.plot(y_data)

root = tk.Tk()
root.title("OSCILOSCÓPIO")

# Configuração do canvas do gráfico na interface
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Configuração de um botão de saída

exit_button = tk.Button(root, text="Sair", command=root.destroy)
exit_button.pack(side=tk.BOTTOM)

ax.set_ylim(0, 4095)
# Configuração da atualização em intervalos regulares
ani = FuncAnimation(fig, update_plot, blit=True, interval=0, save_count=1)
root.mainloop()