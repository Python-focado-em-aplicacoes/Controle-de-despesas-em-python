import tkinter
from tkinter import ttk, Tk
from helpers import expenses

def on_add_expense():
    expenses.add_expense(value_input, description_input, category_input)
    expenses.update_expenses_list(expenses_list)
    expenses.calculate_expenses(total_expenses)

root = Tk()

root.title("Controle de despesas")

frame = ttk.Frame(root)
frame.grid()

value_label = ttk.Label(frame, text="Valor:")
value_label.grid(row=0, column=0)

value_input = ttk.Entry(frame)
value_input.grid(row=0, column=1)

description_label = ttk.Label(frame, text="Descrição:").grid(row=1, column=0)
description_input = ttk.Entry(frame)
description_input.grid(row=1, column=1)

category_label = ttk.Label(frame, text="Categoria:").grid(row=2, column=0)
category_input = ttk.Entry(frame)
category_input.grid(row=2, column=1)

add_expense_button = ttk.Button(frame, text="Adicionar despesa", command=on_add_expense).grid(row=3, column=0, columnspan=3)

expenses_list = tkinter.Text(frame, height=10, width=50)
expenses_list.grid(row=5, column=0, columnspan=3)

total_expenses = ttk.Label(frame, text="Total: R$ 0.00")
total_expenses.grid(row=6, column=0, columnspan=3)

root.mainloop()
