import tkinter
from tkinter import Entry, Text, Label

expenses_array = []

def add_expense(value_input: Entry, description_input: Entry, category_input: Entry):
    expenses_array.append({
        "value": float(value_input.get()),
        "description": description_input.get(),
        "category": category_input.get()
    })
    
    
def update_expenses_list(element: Text):
    element.delete("1.0", "end")
    for item in expenses_array:
        element.insert("end", f"Valor: {item['value']}\n")
        element.insert("end", f"Descrição: {item['description']}\n")
        element.insert("end", f"Categoria: {item['category']}\n")
        element.insert("end", "\n")
        
    
def calculate_expenses(element: Label):
    total = sum(item['value'] for item in expenses_array)
    element.config(text=f"Total: R$ {total:.2f}")