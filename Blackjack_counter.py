import tkinter as tk
from tkinter.font import BOLD, Font
import math

class blackjack_counter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.running_count = 0
        self.counter = 0
        self.Running_Count_label = None
        self.True_Count_label = None
        self.Bet_Amount_label = None
        self.unit_size_entry = None
        self.Decks_used_entry = None
        self.card_counted_label = None
        # tkinter window configuartion
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.app_width = 460
        self.app_height = 530
        self.app_adjustion_x = int((self.screen_width - self.app_width) / 2)
        self.app_adjustion_y = int((self.screen_height - self.app_height) / 2)

        self.master.title("Blackjack Counter")
        self.master.geometry(
            f"{self.app_width}x{self.app_height}+{self.app_adjustion_x}+{self.app_adjustion_y}"
        )

        self.default_font = Font(self.master, size=14)

        self.gui_system()

    def gui_system(self):

        # Menu - row 0

        menu_bar = tk.Menu(self.master)

        # Add first menu col
        file = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file)
        file.add_command(label="New File", command=None)
        file.add_command(label="Open...", command=None)
        file.add_command(label="Save", command=None)
        file.add_separator()
        file.add_command(label="Exit", command=root.destroy)

        self.master.config(menu=menu_bar)

        # Display broad- row 0
        label_1 = tk.Label(self.master, text="BJ Counter", font=self.default_font)

        # 1
        label_2 = tk.Label(self.master, text="Unit Size", font=self.default_font)
        label_3 = tk.Label(self.master, text="Decks Used", font=self.default_font)

        # 2
        label_4 = tk.Label(self.master, text="Inputs", font=self.default_font)
        self.unit_size_entry = tk.Entry(
            self.master, justify="center"
        )
        a =tk.StringVar().set("5")
        self.Decks_used_entry = tk.Entry(
            self.master, justify="center"
        )
        # 3
        label_5 = tk.Label(self.master, text="Running Count", font=self.default_font)
        label_6 = tk.Label(self.master, text="True Count", font=self.default_font)
        label_7 = tk.Label(self.master, text="Bet Amount", font=self.default_font)

        # 4
        self.Running_Count_label = tk.Label(
            self.master, text="0", font=self.default_font, bg="black", fg="white"
        )
        self.True_Count_label = tk.Label(
            self.master, text="0", font=self.default_font, bg="black", fg="white"
        )
        self.Bet_Amount_label = tk.Label(
            self.master, text="0", font=self.default_font, bg="black", fg="white"
        )

        # 5
        label_8 = tk.Label(self.master, text="Cards Counted", font=self.default_font)
        self.card_counted_label = tk.Label(self.master, text="0", font=self.default_font, bg="black",fg="white")

        # 6
        calculator_frame = tk.Frame(self.master)

        button_minus = tk.Button(
            calculator_frame,
            text="-",
            width=7,
            height=2,
            command=lambda: self.minus(1),
        ).grid(row=0, column=0, columnspan=1)
        button_plus = tk.Button(
            calculator_frame,
            text="+",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        button_reset = tk.Button(
            calculator_frame, text="Reset", width=7, height=2,command=self.reset
        ).grid(row=0, column=2, columnspan=1, padx=5, pady=5
        )

        button_7 = tk.Button(
            calculator_frame,
            text="7",
            width=7,
            height=2,
            command=lambda: self.summation(0),
        ).grid(row=1, column=0, padx=5, pady=5)
        button_8 = tk.Button(
            calculator_frame,
            text="8",
            width=7,
            height=2,
            command=lambda: self.summation(0),
        ).grid(row=1, column=1, padx=5, pady=5)
        button_9 = tk.Button(
            calculator_frame,
            text="9",
            width=7,
            height=2,
            command=lambda: self.summation(0),
        ).grid(row=1, column=2, padx=5, pady=5)

        button_4 = tk.Button(
            calculator_frame,
            text="4",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=2, column=0, padx=5, pady=5)
        button_5 = tk.Button(
            calculator_frame,
            text="5",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=2, column=1, padx=5, pady=5)
        button_6 = tk.Button(
            calculator_frame,
            text="6",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=2, column=2, padx=5, pady=5)

        button_A_1 = tk.Button(
            calculator_frame,
            text="A/1",
            width=7,
            height=2,
            command=lambda: self.minus(1),
        ).grid(row=3, column=0, padx=5, pady=5)
        button_2 = tk.Button(
            calculator_frame,
            text="2",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=3, column=1, padx=5, pady=5)
        button_3 = tk.Button(
            calculator_frame,
            text="3",
            width=7,
            height=2,
            command=lambda: self.summation(1),
        ).grid(row=3, column=2, padx=5, pady=5)

        button_10 = tk.Button(
            calculator_frame,
            text="TJQK",
            width=7,
            height=2,
            command=lambda: self.minus(1),
        ).grid(row=4, column=0, padx=5, pady=5, columnspan=3, sticky="ew")

        # Grid setting
        label_1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        label_2.grid(row=1, column=1, padx=5, pady=5)
        label_3.grid(row=1, column=2, padx=5, pady=5)

        label_4.grid(row=2, column=0, padx=5, pady=5)
        self.unit_size_entry.grid(row=2, column=1, padx=5, pady=5)
        self.Decks_used_entry.grid(row=2, column=2, padx=5, pady=5)

        label_5.grid(row=3, column=0, padx=5, pady=5)
        label_6.grid(row=3, column=1, padx=5, pady=5)
        label_7.grid(row=3, column=2, padx=5, pady=5)

        self.Running_Count_label.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.True_Count_label.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        self.Bet_Amount_label.grid(row=4, column=2, padx=5, pady=5, sticky="ew")

        label_8.grid(row=5, column=1, padx=5, pady=5)

        self.card_counted_label.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

        for i in range(3):
            calculator_frame.grid_columnconfigure(i, weight=1)
        calculator_frame.grid(row=7, column=0, columnspan=3, pady=20)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.mainloop()

    def summation(self, num):
        self.running_count += num
        self.counter += 1
        self.card_counted_label["text"] = self.counter
        self.Running_Count_label["text"] = self.running_count
        self.True_Count_label["text"] = self.set_true_count()
        self.Bet_Amount_label["text"] = int(self.unit_size_entry.get()) + math.floor(self.set_true_count()) * int(self.unit_size_entry.get())

        if self.True_Count_label["text"] <0:
            self.True_Count_label["fg"] = "red"
        else:
            self.True_Count_label["fg"] = "white"

    def minus(self,num):
        self.running_count -= num
        self.counter += 1
        self.card_counted_label["text"] = self.counter
        self.Running_Count_label["text"] = self.running_count
        self.True_Count_label["text"] = self.set_true_count()
        self.Bet_Amount_label["text"] = int(self.unit_size_entry.get()) + math.floor(
            self.set_true_count()
        ) * int(self.unit_size_entry.get())

        if self.True_Count_label["text"] <0:
            self.True_Count_label["fg"] = "red"
        else:
            self.True_Count_label["fg"] = "white"

    def set_true_count(self):
        re = self.running_count /(int(self.Decks_used_entry.get()) - (self.counter / 52))
        return round(re,2)

    def reset(self):
        self.running_count = 0
        self.counter = 0
        self.True_Count_label["fg"] = "white"
        self.card_counted_label["text"] = self.counter
        self.Running_Count_label["text"] = self.running_count
        self.True_Count_label["text"] = self.set_true_count()

root = tk.Tk()
main_win = blackjack_counter(root)
