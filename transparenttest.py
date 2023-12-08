import tkinter as tk


root = tk.Tk()
root.geometry("640x480")

root.wm_attributes("-transparentcolor", "white")
tk.Frame(root, background="white").pack(expand=True, fill=tk.BOTH)

filler = tk.Toplevel(root)     # 別ウィンドウを作成
filler.overrideredirect(True)  # ウィンドウ枠を削除
filler.transient(root)         # タスクバーから消す
filler.wm_attributes("-alpha", 0.4)  # ウィンドウを透明にする。0にすると完全に透明になるが、クリックが背後に流れてしまう。

# 変更されるたびにサイズと位置をrootに合わせて、rootの背後に置く
def on_configure_let_filler_track(_):
    filler.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_rootx()}+{root.winfo_rooty()}")
    filler.lower(root)

root.bind("<Configure>", on_configure_let_filler_track)
buttonMove = tk.Button(filler, text="移動", font=("MSゴシック", 10))
buttonMove.place(
    relx=0,
    rely=0
)

root.mainloop()
