# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import re

from tkinter import messagebox

def show():
    root.attribtes("-topmost", True)

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


#def sizeButton_preview(event):
    #getSize = 

# rootメインウィンドウの設定
root = tk.Tk()
root.title("showTEXT")
root.geometry("300x200")


#文字表示
label = tk.Label(text='表示する文字', font=("MSゴシック", "10"))
label.place(
    relx=0.1,
    rely=0.1,
)

getinput = tk.StringVar()
inputTEXT = tk.Entry( font=("MSゴシック", "10"), textvariable=getinput)
inputTEXT.place(
    relx=0.4,
    rely=0.1,
    relwidth=0.5,
    relheight=0.1
)

# フォントを指定してボタンを作成
showPREVIEW = tk.Label(text="入力結果を表示", font=("メイリオ", "10"), relief=tk.SOLID, bd=1)
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
    relheight=0.1
)
selectCOLOR.bind('<<ComboboxSelected>>', select_color)

getSize = tk.StringVar()
inputSIZE = tk.Entry(font=("MSゴシック", "10"), textvariable=getSize)
vcmd = (inputSIZE.register(Value_check), '%s', '%P')
inputSIZE.configure(validate='key', vcmd=vcmd)
inputSIZE.place(
    relx=0.3,
    rely=0.4
)
getSize.trace("w", sizeInput_preview)





root.mainloop()