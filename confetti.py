import random
import tkinter as tk

def show_confetti(root, duration=1500):
    canvas = tk.Canvas(root, bg="#0b0340", highlightthickness=0)
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    particles = []
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F5D142", "#FF33A6", "#00FFFF"]

    # Create confetti pieces
    for _ in range(80):
        x = random.randint(0, root.winfo_width())
        y = random.randint(-50, 0)
        size = random.randint(4, 8)
        color = random.choice(colors)
        particle = canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
        particles.append((particle, random.randint(2, 6)))  # (id, fall_speed)

    def animate():
        for i, (p, speed) in enumerate(particles):
            canvas.move(p, 0, speed)
            pos = canvas.coords(p)
            if pos[1] > root.winfo_height():
                # Reset to top
                canvas.coords(p, random.randint(0, root.winfo_width()), -10,
                              random.randint(0, root.winfo_width())+5, -5)
        root.after(30, animate)

    animate()

    # Remove confetti after duration
    root.after(duration, canvas.destroy)
