import tkinter
from PIL import Image, ImageTk
# --- 基本的な表示準備 ----------------                                         
window = tkinter.Tk()
window.geometry("800x600") # 画面サイズを1000 x 1000 とする                     
window.title("Welcome to the Tkinter")
# 画像を指定                                                                    
img = Image.open('cat04.png')
w = img.width # 横幅を取得                                                      
h = img.height # 縦幅を取得                                                     
img = img.resize((800,600))
#img = img.resize(( int(w * (800/h)), int(h * (600/h)) ))
print(( int(w * (800/h)), int(h * (600/h)) ))
img = ImageTk.PhotoImage(img)
# canvasサイズも画面サイズと同じにして描画                                      
canvas = tkinter.Canvas(width=800, height=600)
canvas.place(x=0, y=0)
# -------------------------------------                                         
# キャンバスに画像を表示する                                                    
canvas.create_image(250-(w*(600/h)/2), 0, image=img, anchor=tkinter.NW)
window.mainloop()