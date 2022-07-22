import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, bg="#fff", width=500, height=300)
canvas.pack()

#変数に図形を代入
rect = canvas.create_rectangle(10,10,50,50, fill="#f0f0f0")
#図形にタグ付け
canvas.create_oval(10,70,50,110, fill="#0fffff", tag="cir")

def move():
    canvas.move(rect, 10, 0)
    canvas.move("cir", 5, 0)
    canvas.after(100, move)

def clk():
    move()

button = tk.Button(root, text="GO", command=clk)
button.pack()


root.mainloop()