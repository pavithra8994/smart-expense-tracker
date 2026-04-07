import tkinter as tk
from tkinter import ttk, messagebox
from storage import add_expense, load_data
from analysis import get_summary, show_chart, highest_category, suggest_reduction

root = tk.Tk()
root.title("Smart Expense Tracker")
root.geometry("500x400")
root.configure(bg="#f5f5f5")

# Center Frame
frame = tk.Frame(root, bg="#f5f5f5")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(frame, text="Expense Tracker", font=("Arial", 16, "bold"), bg="#f5f5f5").grid(row=0, column=0, columnspan=2, pady=10)

# Labels & Inputs
tk.Label(frame, text="Date", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
date_entry = tk.Entry(frame)
date_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Category", bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="e")
category_box = ttk.Combobox(frame, values=["Food", "Travel", "Bills", "Other"])
category_box.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Amount", bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(frame)
amount_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Description", bg="#f5f5f5").grid(row=4, column=0, padx=10, pady=5, sticky="e")
desc_entry = tk.Entry(frame)
desc_entry.grid(row=4, column=1, padx=10, pady=5)

# Functions
def add():
    try:
        expense = {
            "date": date_entry.get(),
            "category": category_box.get(),
            "amount": float(amount_entry.get()),
            "description": desc_entry.get()
        }

        add_expense(expense)
        messagebox.showinfo("Success", "Expense Added!")

        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid Input")

def summary():
    data = load_data()
    total = get_summary(data)
    high = highest_category(data)
    messagebox.showinfo("Summary", f"Total: ₹{total}\nHighest: {high}")

def suggest():
    data = load_data()
    suggestions = suggest_reduction(data)

    if suggestions:
        msg = "\n".join(suggestions)
    else:
        msg = "Spending is balanced "

    messagebox.showinfo("Suggestions", msg)

# Buttons
tk.Button(frame, text="Add Expense", width=15, command=add).grid(row=5, column=0, pady=10)
tk.Button(frame, text="Summary", width=15, command=summary).grid(row=5, column=1, pady=10)

tk.Button(frame, text="Show Chart", width=15, command=lambda: show_chart(load_data())).grid(row=6, column=0, pady=5)
tk.Button(frame, text="Suggestions", width=15, command=suggest).grid(row=6, column=1, pady=5)

root.mainloop()