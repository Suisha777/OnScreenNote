# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def show():
    root.attribtes("-topmost", True)
    

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

inputTEXT = tk.Entry(width=20)
inputTEXT.place(
    relx=0.5,
    rely=0.5,
    relwidth=0.3,
    relheight=0.1
)



root.mainloop()