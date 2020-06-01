import tkinter as tk
import project


class Ending(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.window()

    def window(self):
        self.title('final')
        message = tk.Message(self, width=50*8, text=(f'Поздравляю! Ваш счет: {project.current_score}'))
        message.pack(side='bottom')
