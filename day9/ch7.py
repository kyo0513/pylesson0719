import tkinter as tk

fnt1  = ("Times New Roman",20)
fnt2  = ("Times New Roman",40)
index = 0
timer = 0

key   =""
def key_down(e):
    global key
    key = e.keysym

def main():
    global index,timer
    canvas.delete("STATUS")
    timer = timer + 1
    canvas.create_text(200,30,text="index" +str(index),fill="white",font=fnt1,tag="STATUS")
    canvas.create_text(400,30,text="index" +str(index),fill="cyan",font=fnt1,tag="STATUS")

    if index == 0:
        if timer == 1:
            canvas.create_text(300,150,text="タイトル",fill="white",font=fnt2,tag="TITLE")
            canvas.create_text(300,300,text="Press[SPACE]key",fill="lime",font=fnt1,tag="TI")
        if key == "space":
            canvas.delete("TITLE")
            canvas.create_retangle(0, 0, 600, 400, fill="blue", tag="GAME")
            canvas.create_text(300, 150, text="ゲーム中", fill="white", font=fnt2, tag="GAME")
            canvas.create_text(300, 300, text="[E] 終了", fill="yellow", font=fnt1, tag="GAME")
            index = 1
            timer = 0
    if index == 1:
        if key == "e":
            canvas.delete("GAME")
            canvas.create_rectangle(0, 0, 600, 400, fill="maroon", tag="OVER")
            canvas.create_text(300, 150, text="GAME OVER", fill="red", font=fnt2, tag="OVER")
            index = 2
            timer = 0
    if index == 2:
        if timer == 30:
            canvas.delete("OVER")
            index = 0
            timer = 0

    root.after(100,main)

root = tk.Tk()
root.title("")
root.bind("<KeyPress>",key_down)
canvas = tk.Canvas(width=600,height=400,bg="black")
canvas.pack()
main()
root.mainloop()

