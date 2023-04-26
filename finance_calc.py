from tkinter import*
import tkinter as tk



class FinanceManager:
    def __init__(self, master):
        self.master = master
        master.title("Finance Calculator")
        master.geometry('{}x{}'.format(1000, 600))  # Set window size
        master.attributes('-fullscreen', False)  # Maximize window
        master.configure(background='#eee')  # Set background color


        # Create widgets
        self.income_label = tk.Label(master, text="Income:", font=("Arial", 16), bg="#eee")
        self.income_entry = tk.Entry(master, font=("Arial", 14))
        self.expenses_label = tk.Label(master, text="Expenses:", font=("Arial", 16), bg="#eee")
        self.expenses_entry = tk.Entry(master, font=("Arial", 14))
        self.savings_label = tk.Label(master, text="Savings:", font=("Arial", 16), bg="#eee")
        self.savings_entry = tk.Entry(master, font=("Arial", 14))

        self.calculate_button = tk.Button(master, text="Calculate", font=("Arial", 16), command=self.calculate)
        self.clear_button = tk.Button(master, text="Clear", font=("Arial", 16), command=self.clear)

        self.result_label = tk.Label(master, text="", font=("Arial", 14), bg="#eee")

        # Grid layout
        self.income_label.grid(row=0, column=0, padx=20, pady=20)
        self.income_entry.grid(row=0, column=1, padx=20, pady=20)
        self.expenses_label.grid(row=1, column=0, padx=20, pady=20)
        self.expenses_entry.grid(row=1, column=1, padx=20, pady=20)
        self.savings_label.grid(row=2, column=0, padx=20, pady=20)
        self.savings_entry.grid(row=2, column=1, padx=20, pady=20)

        self.calculate_button.grid(row=3, column=0, padx=20, pady=20)
        self.clear_button.grid(row=3, column=1, padx=20, pady=20)

        self.result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    def calculate(self):
        try:
            income = float(self.income_entry.get())
            expenses = float(self.expenses_entry.get())
            savings = float(self.savings_entry.get())

            total = income - expenses - savings

            result = f"Your total monthly budget is: {total:.2f}"
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid!")

    def clear(self):
        self.income_entry.delete(0, tk.END)
        self.expenses_entry.delete(0, tk.END)
        self.savings_entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceManager(root)
    root.mainloop()
