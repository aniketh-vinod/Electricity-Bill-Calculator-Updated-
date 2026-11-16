import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        units = float(entry_units.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of units.")
        return

    if units <= 100:
        bill = 0
        slab1 = 0
        slab2 = 0
        above_200 = 0
    elif units <= 200:
        slab1 = units - 100
        slab2 = 0
        above_200 = 0
        bill = slab1 * 5
    else:
        slab1 = 100
        slab2 = units - 200
        above_200 = slab2
        bill = (slab1 * 5) + (slab2 * 10)

    result_var.set(f"Total Bill: ₹{bill:.2f}")
    breakdown_var.set(
        f"First 100 units: ₹0\n"
        f"Next {slab1:.0f} units @ ₹5: ₹{slab1 * 5:.2f}\n"
        f"Above 200 units: {above_200:.0f} × ₹10 = ₹{above_200 * 10:.2f}"
    )

root = tk.Tk()
root.title("Electricity Bill Calculator")
root.geometry("460x260")
root.resizable(False, False)

tk.Label(root, text="Electricity Bill Calculator", font=("Arial", 18, "bold")).pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Units consumed:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
entry_units = tk.Entry(frame, width=15, font=("Arial", 12))
entry_units.grid(row=0, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate Bill", command=calculate_bill, font=("Arial", 12), bg="green", fg="white").pack(pady=10)

result_var = tk.StringVar()
result_var.set("Total Bill: ₹0.00")
tk.Label(root, textvariable=result_var, font=("Arial", 14, "bold"), fg="blue").pack()

breakdown_var = tk.StringVar()
breakdown_var.set("Breakdown will appear here")
tk.Label(root, textvariable=breakdown_var, font=("Arial", 10), justify="left").pack(pady=10)

root.mainloop()