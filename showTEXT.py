#----------python---------
# Copyright © 2001-2023 Python Software Foundation; All Rights Reserved
#----------------------------

#------------pyautogui----------------
#Copyright (c) 2014, Al Sweigart
#All rights reserved.

#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:

#* Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.

#* Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.

#* Neither the name of the PyAutoGUI nor the names of its
#  contributors may be used to endorse or promote products derived from
#  this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#-------------------------------------



# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import pyautogui
from tkinter import Toplevel

#サブウィンドウ用の変数
sub = None
backWin = None

movement = 0
buttonMove = None
winx = 0
winy = 0

def show():
    global sub
    global backWin
    if sub == None or not sub.winfo_exists():
        geo = "no"
        submethod(geo)
    else:
        geo = sub.geometry()
        sub.destroy()
        backWin.destroy()
        submethod(geo)
        
def submethod(geo):
    global sub
    sub = tk.Toplevel()
    wid,hei=pyautogui.size()
    if(geo != "no"):
        sub.geometry(geo)
    else:
        sub.geometry(f"{wid}x{hei}+200+200")
    sub.attributes("-topmost", True)
    sub.overrideredirect(True)
    sub.wm_attributes("-transparentcolor", "snow")
    tk.Frame(sub, background="snow").pack(expand=True, fill=tk.BOTH)
    #print("func:show")
    getTEXT = None
    if(inputTEXT.get() == ""):
        getTEXT = "なにも入力されてません"
    else:
        getTEXT = inputTEXT.get()
    showSIZE = 10
    #print(f"inputsizeget:{inputSIZE.get()}")
    if(inputSIZE.get()):
        showSIZE = inputSIZE.get()
    #print(f"text:{getTEXT},size:{showSIZE}")
    showTEXT = tk.Label(sub, text=getTEXT, font=("メイリオ", showSIZE), bg="snow")
    getCOLOR = selectCOLOR.get()
    if(getCOLOR == "赤"):
        showTEXT.config(foreground='red')
    elif(getCOLOR == "黄"):
        showTEXT.config(foreground='yellow')
    elif(getCOLOR == "緑"):
        showTEXT.config(foreground='green')
    elif(getCOLOR == "青"):
        showTEXT.config(foreground='blue')
    elif(getCOLOR == "紫"):
        showTEXT.config(foreground='purple')
    elif(getCOLOR == "白"):
        showTEXT.config(foreground='white')
    elif(getCOLOR == "灰"):
        showTEXT.config(foreground='grey')
    elif(getCOLOR == "黒"):
        showTEXT.config(foreground='black')
    showTEXT.place(x=0, y=30)
    
    global backWin
    backWin = tk.Toplevel()
    backWin.overrideredirect(True)
    backWin.transient(sub)
    backWin.wm_attributes("-alpha", 0.002)
    def traceback(_):
        backX = showSIZE*2*10
        backY = showSIZE*10
        backWin.geometry(f"{backX}x{backY}+{sub.winfo_rootx()}+{sub.winfo_rooty()}")
        backWin.lower(sub)
    sub.bind("<Configure>", traceback)
    global buttonMove
    buttonMove = tk.Button(backWin, width=200, height=400)
    buttonMove.place(
        relx=0,
        rely=0
    )
    buttonMove.bind("<Button-1>", getlocation)
    buttonMove.bind("<Button1-Motion>", move)
    #ツールチップ実装
    buttonMove.bind("<Enter>", tooltipsub)
    buttonMove.bind("<Leave>", hidetipsub)
    #右クリックで消去
    buttonMove.bind("<3>", erasesub)
    
    
        

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
    
def tooltipsub(event):
    global tipwindowSub
    tipwindowSub = Toplevel(root)
    tipwindowSub.wm_overrideredirect(True)
    tipwindowSub.wm_geometry(f"+{event.x_root}+{event.y_root}")
    tk.Label(tipwindowSub, text="左クリックとドラッグで移動、右クリックで文字の消去", font=("MSゴシック", 10), background="yellow").pack()

def hidetipsub(event):
    global tipwindowSub
    if tipwindowSub:
        tipwindowSub.destroy()
        tipwindowSub=None
    
def move(event):
    global winx, winy
    xPosition, YPosition = pyautogui.position()
    #print(f"Pos座標: x={xPosition}, y={YPosition}")
    sub.geometry(f"+{xPosition-winx}+{YPosition-winy}")
    #print(f"posx:{xPosition},posy:{YPosition}")
    #print(f"x:{event.x},y:{event.y}")

def getlocation(event):
    global winx, winy
    winx = event.x
    winy = event.y
    #print("getlocation,functioned")

def erasesub(event):
    global sub
    sub.destroy()
    global backWin
    backWin.destroy()
    hidetipsub(event)


# rootメインウィンドウの設定
root = tk.Tk()
root.title("OnScreenNote")
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
    relx=0.03,
    rely=0.6,
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
    relx=0.6,
    rely=0.47,
    relwidth=0.1
)
getSize.trace("w", sizeInput_preview)

sizeTXT = tk.Label(text="文字のサイズ入力欄(半角数字):", font=("メイリオ", "10"))
sizeTXT.place(
    relx=0.1,
    rely=0.45,
)

buttonFULL = tk.Button(root, text="表示", font=("MSゴシック", 10), command=show)
buttonFULL.place(
    relx=0.85,
    rely=0.08
)
buttonFULL.bind("<Enter>", tooltip)
buttonFULL.bind("<Leave>", hidetip)






root.mainloop()