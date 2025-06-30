import tkinter as tk

app = tk.Tk()
app.title("Rechthoek")
app.geometry("800x600")

def tick2(x):
    canvas.create_rectangle(200, 200, x * 100, 100, fill='red')

def tick(x):
    #canvas.create_rectangle(50, 0, 100, 50, fill='red')
    canvas.create_rectangle(0, 0, x * 100, 100, fill='red')
    if x < 2:
        app.after(1000, tick, x + 1), app.after(1000, tick2, x * 0)


canvas = tk.Canvas(app)
tick(1), tick2(1)

canvas.pack(expand= 1)
app.mainloop()