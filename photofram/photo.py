import tkinter as tk
from PIL import Image,ImageTk

index  = 0
def change_img():
    global index
    canvas.delete("PIC")
    #canvas.create_image(400,300,image=photos[index % len(photos)],tag="PIC")
    #canvas.create_image(400,300,image=photos,tag="PIC")

    canvas.create_image(400,300,image=photos,tag="PIC")
    index+=1
    root.after(5000,change_img)

root = tk.Tk()
root.title("デジタルフォトフレーム")
canvas = tk.Canvas(width=800,height=600)
canvas.pack()
#photos=[tk.PhotoImage(file=f'cat0{i}.png')for i in range(4)]
img = Image.open('cat04.png')
#img = img.resize(400,300)
#photos= tk.PhotoImage(photo)
photos= tk.PhotoImage('cat04.png')

#photos=tk.PhotoImage(file='cat04.png')
change_img()
root.mainloop()
