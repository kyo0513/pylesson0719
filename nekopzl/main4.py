import tkinter as tk
import random

cursor_x = 0
cursor_y = 0
mouse_x  = 0
mouse_y  = 0
mouse_c  = 0
turn     = 1

def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = []
for i in range(10):
    neko.append([0,0,0,0,0,0,0,0])

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60,y*72+60,
                        image=img_neko[neko[y][x]],tag="NEKO")

def yoko_neko():
    for x in range(3):
        if neko[1][x] > 0:
            if neko[0][x] == neko[1][x] == neko[2][x] :
                neko[0][x] =  neko[1][x] =  neko[2][x] = 7 

    for y in range(3):
        if neko[y][1] > 0:
            if neko[y][0] == neko[y][1] == neko[y][2] :
                neko[y][0] =  neko[y][1] =  neko[y][2] = 7

        if neko[1][1] > 0:
            if neko[0][0] == neko[1][1] == neko[2][2]:
                neko[0][0] =  neko[1][1] =  neko[2][2] = 7
            if neko[2][0] == neko[1][1] == neko[0][2]:
                neko[2][0] =  neko[1][1] =  neko[0][2] = 7

def game_main():
    global cursor_x,cursor_y,mouse_c,turn
    #if 24 <= mouse_x and mouse_x < 24+72*8 and 24 <= mouse_y and mouse_y < 24+72*10:
    if 24 <= mouse_x and mouse_x < 24+72*3 and 24 <= mouse_y and mouse_y < 24+72*3:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c = 0
            if neko[cursor_y][cursor_x] > 0:
                pass
            else:
                if int(turn%2) == 1:
                    neko[cursor_y][cursor_x] = 1
                else:
                    neko[cursor_y][cursor_x] = 2

                turn += 1

    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60, cursor_y*72+60, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
    yoko_neko()
    root.after(100,game_main)

root = tk.Tk()
root.title("横に３つ並んだか")
root.resizable(False,False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tk.Canvas(root,width=912,height=768)
cvs.pack()

bg = tk.PhotoImage(file="neko_bg.png")
cursor = tk.PhotoImage(file="neko_cursor.png")
img_neko = [
        None,
        tk.PhotoImage(file="neko1.png"),
        tk.PhotoImage(file="neko2.png"),
        tk.PhotoImage(file="neko3.png"),
        tk.PhotoImage(file="neko4.png"),
        tk.PhotoImage(file="neko5.png"),
        tk.PhotoImage(file="neko6.png"),
        tk.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456,384,image=bg)
#cvs.create_rectangle(660,100,840,160,fill="white")
#cvs.create_text(750,130,text="テスト",fill="red",font=("Times New Roman",30))
game_main()
root.mainloop()
