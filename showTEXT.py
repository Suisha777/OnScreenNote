# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

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

# rootメインウィンドウの設定
root = tk.Tk()
root.title("showTEXT")
root.geometry("300x200")


#文字表示
label = tk.Label(text='表示する文字', font=("MSゴシック", "10"))
label.place(
    relx=0.2,
    rely=0.1,
)

getinput = tk.StringVar()
inputTEXT = tk.Entry(width=20, font=("MSゴシック", "10"), textvariable=getinput)
inputTEXT.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.3,
    relheight=0.1
)

# フォントを指定してボタンを作成
showPREVIEW = tk.Label(text="入力結果を表示", font=("メイリオ", "10"), relief=tk.SOLID, bd=3)
showPREVIEW.place(
    relx=0.3,
    rely=0.5,
)
getinput.trace("w", update_preview)

color = ('黒','赤', '黄', '緑', '青', '紫', '白', '灰')
selectCOLOR = ttk.Combobox(font=("MSゴシック", 10), state="readonly", values=color, justify="center", )
selectCOLOR.set("黒")
selectCOLOR.place(
    relx=0.3,
    rely=0.3
)
selectCOLOR.bind('<<ComboboxSelected>>', select_color)



root.mainloop()