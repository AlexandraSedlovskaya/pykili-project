import tkinter as tk
from collections import defaultdict as dd
from functools import partial


class Records(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.all_records = tk.Label(self, text='Все рекорды')
        self.window()

    def window(self):
        self.title('records')
        quit_button = tk.Button(self, text='Quit', command=self.destroy)
        quit_button.grid(row=0, column=0, sticky='nw')
        if len(self.all()) != 0:
            scores = self.all()
            records, keys = self.best_score(scores)
            best = keys[0]
            names = records[best]
            winners = ', '.join(names)
            best_label = tk.Label(self, text=f'У {winners} минимальное количество ходов - {best}')
            best_label.grid()
            self.all_records.grid()
            list_of_names = []
            for score in keys:
                gamers = []
                for name in records[score]:
                    if name not in list_of_names:
                        list_of_names.append(name)
                        gamers.append(name)
                if gamers:
                    gamers = ', '.join(gamers)
                    score_label = tk.Label(self, text=f'{gamers}: {str(score)}')
                    score_label.grid()
            history_label = tk.Label(self, text='Историю игр какого игрока вы хотите посмотреть?')
            history_label.grid()
            gamer_name = tk.Text(self, height=2, width=7, font='Arial 14')
            gamer_name.grid()
            ok_button = tk.Button(self, text='OK', command=partial(self.find_history, gamer_name, scores))
            ok_button.grid()
        else:
            label = tk.Label(self, text='У вас еще нет достижений')
            label.grid(row=1, column=1)

    @staticmethod
    def best_score(all_scores):
        reversed_all_scores = {}
        for name, score in all_scores.items():
            for i in score:
                if i in reversed_all_scores.keys():
                    if name not in reversed_all_scores[i]:
                        reversed_all_scores[i] = reversed_all_scores.get(i, []) + [name]
                else:
                    reversed_all_scores[i] = [name]
        keys = list(reversed_all_scores.keys())
        keys.sort()
        return reversed_all_scores, keys

    @staticmethod
    def all():
        prev_scores = dd(list)
        with open('scores.txt', encoding='utf-8') as file:
            for line in file:
                key, value = line.split('\t')
                prev_scores[key].append(int(value))
        return prev_scores

    @staticmethod
    def add_in_file(name, score):
        with open('scores.txt', 'a', encoding='utf-8') as file:
            file.write(name + '\t' + str(score) + '\n')

    def find_history(self, gamer_name, scores):
        name = (gamer_name.get(1.0, tk.END))[:-1]
        if name in scores:
            label = tk.Label(self, text=f'Вот история игр игрока {name}: {str(scores[name])[1:-1]}')
            label.grid()
        else:
            label = tk.Label(self, text='Этот игрок еще не играл')
            label.grid()