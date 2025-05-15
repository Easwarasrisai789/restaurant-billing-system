from tkinter import *
import random
import os
from tkinter import messagebox

root = Tk()
root.geometry("1350x700+0+0")
root.title("Restaurant Billing System")

bg_color = "#074463"
fg_color = "white"

title = Label(root, text="Restaurant Billing System", bd=12, relief=GROOVE, bg=bg_color, fg=fg_color,
              font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

# ================= Customer Details ===================
F1 = LabelFrame(root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                fg="gold", bg=bg_color)
F1.place(x=0, y=80, relwidth=1)

c_name = StringVar()
c_phone = StringVar()
bill_no = StringVar()
bill_no.set(str(random.randint(1000, 9999)))
search_bill = StringVar()

lbl_name = Label(F1, text="Customer Name", bg=bg_color, fg=fg_color, font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
txt_name = Entry(F1, width=15, textvariable=c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

lbl_phone = Label(F1, text="Phone No.", bg=bg_color, fg=fg_color, font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
txt_phone = Entry(F1, width=15, textvariable=c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

lbl_bill = Label(F1, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
txt_bill = Entry(F1, width=15, textvariable=search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)
btn_search = Button(F1, text="Search", command=lambda: find_bill(), width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)

# ======================= Food ========================
F2 = LabelFrame(root, text="Food", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
F2.place(x=5, y=180, width=325, height=380)

item_vars = {
    "burger": IntVar(),
    "pizza": IntVar(),
    "fries": IntVar(),
    "noodles": IntVar(),
    "sandwich": IntVar(),
    "wrap": IntVar()
}

foods = list(item_vars.keys())
for i, item in enumerate(foods):
    Label(F2, text=item.capitalize(), font=("times new roman", 16, "bold"), bg=bg_color, fg=fg_color).grid(row=i, column=0, padx=10, pady=10, sticky="w")
    Entry(F2, width=10, textvariable=item_vars[item], font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=i, column=1, padx=10, pady=10)

# ======================= Drinks ========================
F3 = LabelFrame(root, text="Drinks", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
F3.place(x=340, y=180, width=325, height=380)

drink_vars = {
    "coke": IntVar(),
    "pepsi": IntVar(),
    "frooti": IntVar(),
    "sprite": IntVar(),
    "limca": IntVar(),
    "thumbsup": IntVar()
}

drinks = list(drink_vars.keys())
for i, drink in enumerate(drinks):
    Label(F3, text=drink.capitalize(), font=("times new roman", 16, "bold"), bg=bg_color, fg=fg_color).grid(row=i, column=0, padx=10, pady=10, sticky="w")
    Entry(F3, width=10, textvariable=drink_vars[drink], font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=i, column=1, padx=10, pady=10)

# ======================= Bill Area ========================
F4 = Frame(root, bd=10, relief=GROOVE)
F4.place(x=680, y=180, width=660, height=380)
bill_title = Label(F4, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
scroll_y = Scrollbar(F4, orient=VERTICAL)
txtarea = Text(F4, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH, expand=1)

# ==================== Button Frame ========================
F5 = LabelFrame(root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
F5.place(x=0, y=560, relwidth=1, height=140)

total_food = StringVar()
total_drinks = StringVar()
tax = StringVar()

Label(F5, text="Total Food", bg=bg_color, fg=fg_color, font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
Entry(F5, width=18, textvariable=total_food, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

Label(F5, text="Total Drinks", bg=bg_color, fg=fg_color, font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
Entry(F5, width=18, textvariable=total_drinks, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

Label(F5, text="Tax", bg=bg_color, fg=fg_color, font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
Entry(F5, width=18, textvariable=tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

btn_total = Button(F5, text="Total", command=lambda: total(), bg="cadetblue", fg="white", bd=7, pady=15, width=10, font="arial 12 bold").grid(row=1, column=2, padx=10, pady=5)
btn_bill = Button(F5, text="Generate Bill", command=lambda: bill_area(), bg="cadetblue", fg="white", bd=7, pady=15, width=12, font="arial 12 bold").grid(row=1, column=3, padx=10, pady=5)
btn_clear = Button(F5, text="Clear", command=lambda: clear_data(), bg="cadetblue", fg="white", bd=7, pady=15, width=10, font="arial 12 bold").grid(row=1, column=4, padx=10, pady=5)
btn_exit = Button(F5, text="Exit", command=lambda: exit_app(), bg="cadetblue", fg="white", bd=7, pady=15, width=10, font="arial 12 bold").grid(row=1, column=5, padx=10, pady=5)

# ==================== Functions ========================

def total():
    f_total = sum([item_vars[item].get() * 40 for item in item_vars])
    d_total = sum([drink_vars[drink].get() * 30 for drink in drink_vars])
    t_tax = round((f_total + d_total) * 0.05, 2)
    total_food.set(f"₹ {f_total}")
    total_drinks.set(f"₹ {d_total}")
    tax.set(f"₹ {t_tax}")

def bill_area():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer details are required")
        return
    txtarea.delete('1.0', END)
    txtarea.insert(END, f"\tWelcome to XYZ Restaurant\n")
    txtarea.insert(END, f"\nBill No: {bill_no.get()}")
    txtarea.insert(END, f"\nCustomer Name: {c_name.get()}")
    txtarea.insert(END, f"\nPhone No: {c_phone.get()}")
    txtarea.insert(END, f"\n==============================")
    txtarea.insert(END, f"\nItems\t\tQty\tPrice")

    total_price = 0
    for item in item_vars:
        qty = item_vars[item].get()
        if qty > 0:
            price = qty * 40
            txtarea.insert(END, f"\n{item.capitalize()}\t\t{qty}\t{price}")
            total_price += price

    for drink in drink_vars:
        qty = drink_vars[drink].get()
        if qty > 0:
            price = qty * 30
            txtarea.insert(END, f"\n{drink.capitalize()}\t\t{qty}\t{price}")
            total_price += price

    total_tax = round(total_price * 0.05, 2)
    txtarea.insert(END, f"\n------------------------------")
    txtarea.insert(END, f"\nTax\t\t\t{total_tax}")
    txtarea.insert(END, f"\nTotal\t\t\t{total_price + total_tax}")
    txtarea.insert(END, f"\n==============================")
    save_bill()

def save_bill():
    op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
    if op > 0:
        bill_data = txtarea.get('1.0', END)
        with open(f"bills/{bill_no.get()}.txt", "w") as f:
            f.write(bill_data)
        messagebox.showinfo("Saved", f"Bill No. {bill_no.get()} saved successfully")

def find_bill():
    found = False
    try:
        with open(f"bills/{search_bill.get()}.txt", "r") as f:
            txtarea.delete('1.0', END)
            txtarea.insert(END, f.read())
            found = True
    except FileNotFoundError:
        messagebox.showerror("Error", "Bill not found")

def clear_data():
    c_name.set("")
    c_phone.set("")
    bill_no.set(str(random.randint(1000, 9999)))
    search_bill.set("")
    for var in item_vars.values():
        var.set(0)
    for var in drink_vars.values():
        var.set(0)
    total_food.set("")
    total_drinks.set("")
    tax.set("")
    txtarea.delete('1.0', END)

def exit_app():
    root.destroy()


if not os.path.exists('bills'):
    os.makedirs('bills')

root.mainloop()
