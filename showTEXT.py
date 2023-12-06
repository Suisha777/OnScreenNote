# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import re
import pyautogui
import threading
from tkinter import messagebox, Toplevel

#サブウィンドウ用の変数
sub = None

movement = 0
buttonMove = None

def show():
    global sub
    sub = tk.Toplevel()
    sub.geometry("300x400+200+200")
    sub.attributes("-topmost", True)
    sub.overrideredirect(True)
    #sub.wm_attributes("-transparentcolor", "white")
    tk.Frame(sub, background="white").pack(expand=True, fill=tk.BOTH)
    print("func:show")
    global buttonMove
    buttonMove = tk.Button(sub, text="移動", font=("MSゴシック", 10))
    buttonMove.place(
        relx=0,
        rely=0
    )
    buttonMove.bind("<Button1-Motion>", move)

def update_preview(*args):
    showPREVIEW["text"] = inputTEXT.get()
    
def select_color(event):
    getCOLOR = selectCOLOR.get()
    if(getCOLOR == "赤"):
        showPREVIEW.config(foreground='red')
    elif(getCOLOR == "黄"):
        showPREVIEW.config(foreground='yellow')
    elif(getCOLOR == "緑"):
        showPREVIEW.config(foreground='green')
    elif(getCOLOR == "青"):
        showPREVIEW.config(foreground='blue')
    elif(getCOLOR == "紫"):
        showPREVIEW.config(foreground='purple')
    elif(getCOLOR == "白"):
        showPREVIEW.config(foreground='white')
    elif(getCOLOR == "灰"):
        showPREVIEW.config(foreground='grey')
    elif(getCOLOR == "黒"):
        showPREVIEW.config(foreground='black')
        
def sizeInput_preview(*args):
    getSize = inputSIZE.get()
    if(getSize == ""):
        showPREVIEW.config(font=("MSゴシック", 10))
        return
    showPREVIEW.config(font=("MSゴシック", getSize))
    
def Value_check(before, after):
    if(after == ""):
        return(True)
    elif(after.isdecimal()):
        return(True)
    else:
        return(False)

def tooltip(event):
    global tipwindow
    tipwindow = Toplevel(root)
    tipwindow.wm_overrideredirect(True)
    tipwindow.wm_geometry(f"+{event.x_root}+{event.y_root}")
    tk.Label(tipwindow, text="ボタンを押すと文字だけを表示します", font=("MSゴシック", 10)).pack()

def hidetip(event):
    global tipwindow
    if tipwindow:
        tipwindow.destroy()
        tipwindow=None

    
def move(event):
    xPosition, YPosition = pyautogui.position()
    #print(f"Pos座標: x={xPosition}, y={YPosition}")
    sub.geometry(f"+{xPosition-20}+{YPosition-20}")


# rootメインウィンドウの設定
root = tk.Tk()
root.title("showTEXT")
root.geometry("600x400")


#文字表示
label = tk.Label(text='表示する文字:', font=("MSゴシック", "10"))
label.place(
    relx=0.1,
    rely=0.1,
)

getinput = tk.StringVar()
inputTEXT = tk.Entry( font=("MSゴシック", "10"), textvariable=getinput, relief=tk.SOLID, bd=0.5)
inputTEXT.place(
    relx=0.35,
    rely=0.1,
    relwidth=0.4,
    relheight=0.07
)

# フォントを指定してボタンを作成
showPREVIEW = tk.Label(text="入力結果のプレビュー", font=("メイリオ", "10"), relief=tk.SOLID, bd=1)
showPREVIEW.place(
    relx=0.3,
    rely=0.7,
)
getinput.trace("w", update_preview)

color = ('黒','赤', '黄', '緑', '青', '紫', '白', '灰')
selectCOLOR = ttk.Combobox(font=("MSゴシック", 10), state="readonly", values=color, justify="center", )
selectCOLOR.set("黒")
selectCOLOR.place(
    relx=0.4,
    rely=0.3,
    relwidth=0.2,
    relheight=0.07
)
selectCOLOR.bind('<<ComboboxSelected>>', select_color)

textCOLOR = tk.Label(text='文字の色変更:', font=("MSゴシック", "10"))
textCOLOR.place(
    relx=0.1,
    rely=0.3,
)

getSize = tk.StringVar()
inputSIZE = tk.Entry(font=("MSゴシック", "10"), textvariable=getSize)
vcmd = (inputSIZE.register(Value_check), '%s', '%P')
inputSIZE.configure(validate='key', vcmd=vcmd, relief=tk.SOLID, bd=1)
inputSIZE.place(
    relx=0.7,
    rely=0.47,
    relwidth=0.1
)
getSize.trace("w", sizeInput_preview)

sizeTXT = tk.Label(text="文字のサイズを半角数字で入れてください:", font=("メイリオ", "10"))
sizeTXT.place(
    relx=0.02,
    rely=0.45,
)

buttonFULL = tk.Button(root, text="表示", font=("MSゴシック", 10), command=show)
buttonFULL.place(
    relx=0.85,
    rely=0.05
)
buttonFULL.bind("<Enter>", tooltip)
buttonFULL.bind("<Leave>", hidetip)






root.mainloop()