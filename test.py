import tkinter as tk
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
MITOCHONDRIA_COLOR = "red"
CELL_COLOR = "lightblue"
ATP_COLOR = "yellow"

# Initialize Tkinter
root = tk.Tk()
root.title("Mitochondria Energy Simulation")

# Canvas for drawing
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Cell and mitochondria properties
cell_radius = 100
mitochondria_radius = 20
num_mitochondria = 5
mitochondria_list = []

# ATP production rate per mitochondria
atp_production_rate = 1

# Energy level
energy = 100

# Functions
def init_simulation():
    global energy
    energy = 100 # Init energy
    mitochondria_list.clear()
    canvas.delete("all")

    # Create the cell
    canvas.create_oval(
        WIDTH // 2 - cell_radius,
        HEIGHT // 2 - cell_radius,
        WIDTH // 2 + cell_radius,
        HEIGHT // 2 + cell_radius,
        fill=CELL_COLOR
    )

    # Create mitochondria
    for _ in range(num_mitochondria):
        x = random.randint(
            WIDTH // 2 - cell_radius + 50,
            WIDTH // 2 + cell_radius - 50
        )
        y = random.randint(
            HEIGHT // 2 - cell_radius + 50,
            HEIGHT // 2 + cell_radius - 50
        )
        mitochondria_list.append((x, y))

        canvas.create_oval(
            x - mitochondria_radius,
            y - mitochondria_radius,
            x + mitochondria_radius,
            y + mitochondria_radius,
            fill=MITOCHONDRIA_COLOR
        )

def update_energy():
    global energy
    energy += num_mitochondria * atp_production_rate
    energy_label.config(text=f"Energy: {energy}")

def update_atp_production_rate(value):
    global atp_production_rate
    atp_production_rate = int(value)
    speed_label.config(text=f"ATP Production Speed: {atp_production_rate}")

def simulate():
    update_energy()
    canvas.delete(ATP_COLOR)
    
    for _ in range(num_mitochondria):
        for mitochondria in mitochondria_list:
            x, y = mitochondria
            theta = random.uniform(0, 2 * math.pi)
            distance = random.uniform(0, 2 * mitochondria_radius)
            atp_x = x + distance * math.cos(theta)
            atp_y = y + distance * math.sin(theta)
            canvas.create_oval(
                atp_x - 3,
                atp_y - 3,
                atp_x + 3,
                atp_y + 3,
                fill=ATP_COLOR
            )

    root.after(1000 // atp_production_rate, simulate)  # Simulate ATP production every 1000ms / ATP production rate

# GUI
energy_label = tk.Label(root, text=f"Energy: {energy}")
energy_label.pack()

speed_label = tk.Label(root, text=f"ATP Production Speed: {atp_production_rate}")
speed_label.pack()

speed_slider = tk.Scale(root, from_=1, to=10, orient="horizontal", label="Speed", command=update_atp_production_rate)
speed_slider.set(atp_production_rate)
speed_slider.pack()

start_button = tk.Button(root, text="Start Simulation", command=lambda: simulate())
start_button.pack()

reset_button = tk.Button(root, text="Reset Simulation", command=lambda: init_simulation())
reset_button.pack()

init_simulation()  # Initialize the simulation

root.mainloop()