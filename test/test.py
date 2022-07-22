#ライブラリのインポート
import tkinter as tk
import tkinter.filedialog
import os

#ファイルパス、ファイル名を取得し表示する関数
#f_pathにはファイルパスを代入
#nameにはファイル名を代入
#画像ファイルはbmp,png,jpg,jpeg,tifの読み込みに対応
#initialdirには初期ディレクトリを入力
def getfilename():
    f_path = tk.filedialog.askopenfilename(title="ファイル選択", initialdir="ディレクトリを入力", filetypes=[("Image file", ".bmp .png .jpg .jpeg .tif")])
    name = os.path.basename(f_path) 
    var1.set(f_path)
    var2.set(name)
    l_1 = tk.Label(root,textvariable=var1, relief="flat")
    l_1.place(x=30, y=40)
    l_2 = tk.Label(root,textvariable=var2, relief="flat")
    l_2.place(x=30, y=60)
    print(f_path)
    print(name)
    
#ウインドウ作成
root = tk.Tk()
#ウインドウのタイトル
root.title("ウインドウ")
#ウインドウサイズと位置指定 幅,高さ,x座標,y座標 
root.geometry("500x200+50+50")

#ラベルテキスト更新
var1 = tk.StringVar()
var2 = tk.StringVar()

#ボタン作成
button = tk.Button(root, text="ファイル選択", command=getfilename)
button.pack()

#イベントループ
root.mainloop()