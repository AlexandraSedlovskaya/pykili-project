import tkinter as tk
import menu
import os

if not os.path.isfile('scores.txt'):
    score_file = open('scores.txt', 'w', encoding='utf-8')

current_score = ''
name = ''
rows = []
columns = []


def main():
    root = tk.Tk()
    root.geometry('150x150')  # Размеры окна
    app = menu.Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
