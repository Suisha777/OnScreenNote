# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def show():
    root.attribtes("-topmost", True)

def update_preview(*args):
    showPREVIEW["text"] = inputTEXT.get()

# rootメインウィンドウの設定
root = tk.Tk()
root.title("showTEXT")
root.geometry("300x200")


#文字表示
label = tk.Label(text='表示する文字', font=("MSゴシック", "10"))
label.place(
    relx=0.2,
    rely=0.5,
)

getinput = tk.StringVar()
inputTEXT = tk.Entry(width=20, font=("MSゴシック", "10"), textvariable=getinput)
inputTEXT.place(
    relx=0.5,
    rely=0.5,
    relwidth=0.3,
    relheight=0.1
)

# フォントを指定してボタンを作成
showPREVIEW = tk.Label(text="入力結果を表示", font=("メイリオ", "10"))
showPREVIEW.place(
    relx=0.2,
    rely=0.7,
)
getinput.trace("w", update_preview)



root.mainloop()