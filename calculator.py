import tkinter as tk  # ライブラリのインポート
from tkinter import ttk

BUTTON = [
    ["", "B", "C", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

SYMBOL = ["+", "-", "*", "/"]


class CaluGui(object):  # ウィンドウ・タイトル・サイズ設定
    def __init__(self, app=None):
        self.calc_str = ""  # 計算用の文字列
        # Window Setting
        app.title('簡易的な電卓を作ってみた')  # Window のタイトル
        app.geometry('300x450')  # Window のサイズ

        # frame setting
        calc_frame = ttk.Frame(app, width=300, height=100)  # 計算式・結果用
        calc_frame.propagate(False)  # サイズ固定
        calc_frame.pack(side=tk.TOP, padx=10, pady=20)  # 余白設定
        button_frame = ttk.Frame(app, width=300, height=400)  # 計算ボタンframe
        button_frame.propagate(False)  # サイズ固定
        button_frame.pack(side=tk.BOTTOM)  # 余白設定

        # parts setting
        self.calc_var = tk.StringVar()  # 計算式用動的変数
        self.ans_var = tk.StringVar()  # 結果用動的変数
        calc_label = tk.Label(
            calc_frame, textvariable=self.calc_var, font=("", 20))  # 計算式用label
        ans_label = tk.Label(
            calc_frame, textvariable=self.ans_var, font=("", 15))  # 結果用label
        calc_label.pack(anchor=tk.E)  # 右揃え
        ans_label.pack(anchor=tk.E)


def main():
    app = tk.Tk()
    app.resizable(width=False, height=False)
    CaluGui(app)
    app.mainloop()  # Window をループで回すことでWidgetに対応できるようになる、メインループ実行


if __name__ == '__main__':  # スクリプトが直接実行された時にこれを実行する
    main()
