import tkinter as tk  # ライブラリのインポート


class CaluGui(object):  # ウィンドウ・タイトル・サイズ設定
    def __init__(self, app=None):
        # Window Setting
        app.title('簡易的な電卓を作ってみた')  # Window のタイトル
        app.geometry('400x600')  # Window のサイズ


def main():
    app = tk.Tk()
    CaluGui(app)
    app.mainloop()  # Window をループで回すことで Widgit に対応できるようになる、メインループ実行


if __name__ == '__main__':  # スクリプトが直接実行された時にこれを実行する
    main()
