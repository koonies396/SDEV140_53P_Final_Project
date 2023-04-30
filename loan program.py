import tkinter as tk
from tkinter import ttk

def calculate_amortization():
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100 / 12
    loan_term = int(loan_term_entry.get()) * 12
    monthly_payment = float(monthly_payment_entry.get())
    remaining_balance = principal
    for i in range(1, loan_term + 1):
        interest_paid = remaining_balance * interest_rate
        principal_paid = monthly_payment - interest_paid
        remaining_balance -= principal_paid
        if remaining_balance < 0:
            remaining_balance = 0
        amortization_table.insert("", tk.END, values=(i, "{:.2f}".format(interest_paid), "{:.2f}".format(principal_paid), "{:.2f}".format(remaining_balance)))
        
root = tk.Tk()
root.title("Loan Amortization Schedule")

principal_label = tk.Label(root, text="Principal:")
principal_label.grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

interest_rate_label = tk.Label(root, text="Interest Rate (%):")
interest_rate_label.grid(row=1, column=0)
interest_rate_entry = tk.Entry(root)
interest_rate_entry.grid(row=1, column=1)

loan_term_label = tk.Label(root, text="Loan Term (years):")
loan_term_label.grid(row=2, column=0)
loan_term_entry = tk.Entry(root)
loan_term_entry.grid(row=2, column=1)

monthly_payment_label = tk.Label(root, text="# Of Monthly Payments:")
monthly_payment_label.grid(row=3, column=0)
monthly_payment_entry = tk.Entry(root)
monthly_payment_entry.grid(row=3, column=1)

# table generated
amortization_table = tk.ttk.Treeview(root)
amortization_table["columns"]=("Payment", "Interest Paid", "Principal Paid", "Remaining Balance")
amortization_table.column("#0", width=0, stretch=tk.NO)
amortization_table.column("Payment", anchor=tk.CENTER, width=100)
amortization_table.column("Interest Paid", anchor=tk.CENTER, width=150)
amortization_table.column("Principal Paid", anchor=tk.CENTER, width=150)
amortization_table.column("Remaining Balance", anchor=tk.CENTER, width=200)
amortization_table.heading("Payment", text="Payment")
amortization_table.heading("Interest Paid", text="Interest Paid")
amortization_table.heading("Principal Paid", text="Principal Paid")
amortization_table.heading("Remaining Balance", text="Remaining Balance")
amortization_table.grid(row=4, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate_amortization)
calculate_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
