import tkinter as tk

x   = 0
ani = 0
count = 0

def animation():
    global x,ani,count
    count +=1
    x = x + 4
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240,150,image=img_bg,tag="BG")
    canvas.create_image(x+240,150,image=img_bg,tag="BG")
    if count % 4 == 0:
        ani = (ani+1)%4
    canvas.create_image(240,200,image=img_dog[ani],tag="BG")
    root.after(200,animation)

root = tk.Tk()
root.title("")
canvas = tk.Canvas(width=480,height=300)
canvas.pack()
img_bg= tk.PhotoImage(file="park.png")
img_dog =[
        tk.PhotoImage(file="dog0.png"),
        tk.PhotoImage(file="dog1.png"),
        tk.PhotoImage(file="dog2.png"),
        tk.PhotoImage(file="dog3.png"),
]
animation()
root.mainloop()
