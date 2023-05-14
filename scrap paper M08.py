import tkinter as tk
from tkinter import ttk
import numpy_financial as npf
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import pandas as pd

def calculate_amortization():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get()) / (100 * 12)
        loan_term_years = int(loan_term_entry.get())
        loan_term = loan_term_years * 12
        monthly_payment = npf.pmt(.04 / 12, loan_term_years * 12,principal)
        monthly_payment = abs(monthly_payment)
        monthly_payment = round(monthly_payment, 2)
        remaining_balance = principal
        for i in range(1, loan_term + 1):
            interest_paid = remaining_balance * interest_rate
            principal_paid = monthly_payment - interest_paid
            remaining_balance -= principal_paid
            if remaining_balance < 0:
                remaining_balance = 0
            amortization_table.insert("", tk.END, values=(i, "{:.2f}".format(monthly_payment), "{:.2f}".format(interest_paid), "{:.2f}".format(principal_paid), "{:.2f}".format(remaining_balance)))
    except ValueError:
        # create a new top-level window to display the error message
        error_window = tk.Toplevel(root)
        error_window.title("Error")
        error_label = tk.Label(error_window, text="Please enter valid numbers in all fields.")
        error_label.pack(padx=10, pady=10)
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=10)
root = tk.Tk()
root.title("Loan Calculator")

principal_label = tk.Label(root, text="Principal:")
principal_label.grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

principal_label = tk.Label(root, text="Loan Amount:")
principal_label.grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0)
interest_rate_entry = tk.Entry(root)
interest_rate_entry.grid(row=1, column=1)

loan_term_label = tk.Label(root, text="Loan Term (# of years):")
loan_term_label.grid(row=2, column=0)
loan_term_entry = tk.Entry(root)
loan_term_entry.grid(row=2, column=1)

#monthly_payment_label = tk.Label(root, text="# Of Monthly Payments:")
#monthly_payment_label.grid(row=3, column=0)
#monthly_payment_entry = tk.Entry(root)
#monthly_payment_entry.grid(row=3, column=1)

# Set up the grid row and column configuration
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# creating the table columns
amortization_table = tk.ttk.Treeview(root)
amortization_table["columns"]=("Payment", "Monthly Payment","Interest Paid", "Principal Paid", "Remaining Balance")
amortization_table.column("#0", width=0, stretch=tk.NO)
amortization_table.column("Payment", anchor=tk.CENTER, width=100, stretch=tk.YES)
amortization_table.column("Monthly Payment", anchor=tk.CENTER, width=100, stretch=tk.YES)
amortization_table.column("Interest Paid", anchor=tk.CENTER, width=100, stretch=tk.YES)
amortization_table.column("Principal Paid", anchor=tk.CENTER, width=100, stretch=tk.YES)
amortization_table.column("Remaining Balance", anchor=tk.CENTER, width=100, stretch=tk.YES)

# creating the header row
amortization_table.heading("#0", text="")
amortization_table.heading("Payment", text="Payment")
amortization_table.heading("Monthly Payment", text="Monthly Payment")
amortization_table.heading("Interest Paid", text="Interest Paid")
amortization_table.heading("Principal Paid", text="Principal Paid")
amortization_table.heading("Remaining Balance", text="Remaining Balance")
amortization_table.grid(row=4, column=0, columnspan=3, sticky="nsew")

# Set the minimum size of the root window
root.minsize(500, 300)

def clear_table():
    for item in amortization_table.get_children():
        amortization_table.delete(item)

button_width = 10

# calculate button
button_width = 10

calculate_button = tk.Button(root, text="Calculate", command=calculate_amortization, width=button_width, anchor="center")
calculate_button.grid(row=7, column=0, columnspan=1, padx=5, pady=10, sticky="ew")

#Clear the treeview list items
clear_button = tk.Button(root, text="Clear", command=clear_table, width=button_width, anchor="center")
clear_button.grid(row=7, column=1, columnspan=1, padx=5, pady=10, sticky="ew")

def save_file():
    data = []
    for child in amortization_table.get_children():
        item = amortization_table.item(child)['values']
        data.append(item)
    
    df = pd.DataFrame(data, columns=["Payment", "Monthly Payment", "Interest Paid", "Principal Paid", "Remaining Balance"])
    file = filedialog.asksaveasfile(initialfile="Untitled.xlsx", defaultextension='.xlsx', 
                                  filetypes=[("Excel Workbook","*.xlsx"), ("All Files",".*")])
    if file:
        df.to_excel(file.name, index=False)


# save button
save_button = tk.Button(root, text="Save", command=save_file, width=button_width, anchor="center")
save_button.grid(row=7, column=2, columnspan=1, padx=5, pady=10, sticky="ew")

# Add another row at the bottom of the grid
root.grid_rowconfigure(7, weight=1)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=(10, 0))

# Center the frame
button_frame.grid_propagate(False)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)


# Add another row at the bottom of the grid
root.grid_rowconfigure(8, weight=1)

# Set the minimum size of the root window
root.minsize(500, 400)

root.mainloop()
