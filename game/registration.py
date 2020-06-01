import tkinter as tk
import project
import game


class Reg(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.name = tk.Text(self, height=2, width=7, font='Arial 14')
        self.window()

    def window(self):
        label = tk.Label(self, text='Представьтесь: ')
        label.grid(row=1, column=1)
        self.name.grid(row=1, column=2)
        ok_button = tk.Button(self, text='OK', command=self.get_name)
        ok_button.grid(row=1, column=3)

    def get_name(self):
        name = (self.name.get(1.0, tk.END))
        project.name = name[:-1]
        game.Game()
        self.destroy()
