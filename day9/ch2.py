import tkinter as tk

root = tk.Tk()
root.title("Canvasに画像を描画する")
canvas = tk.Canvas(width=480,heigh=300)
canvas.pack()
img_bg = tk.PhotoImage(file="park.png")
canvas.create_image(240,150,image=img_bg)
root.mainloop()
