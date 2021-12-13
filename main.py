from pair_sum import TwoPairSum
from tkinter import *
from tkinter import messagebox


def search_pairs():
    input_box = input_entry.get().strip()
    try:
        # Convert it into integer
        int_input = int(input_box)
        two_pair_sum = TwoPairSum(input_number=int_input)
        pair_result_dict = two_pair_sum.two_sum_hashing()
        if not bool(pair_result_dict):
            messagebox.showinfo(title="Oops", message="No Pair of names in the input data")
        else:
            two_pair_sum.print_name(pair_result_dict)
            messagebox.showinfo(title="Congrats!", message="result.txt file is save in your root directory")
    except ValueError:
        messagebox.showerror(title="Oops", message="Please enter a valid integer")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pair Sum Search")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
title_label = Label(text="Pair Sum List App", font=("Helvetica", 14))
title_label.grid(row=0, column=0, columnspan=2)

description_label = Label(text="App to find list of pairs of a given list url, \n please enter a integer in the "
                               "field below")
description_label.grid(row=1, column=0, columnspan=2, pady=(5, 0))

input_label = Label(text="Enter a value:")
input_label.grid(row=2, column=0)

input_entry = Entry(width=17)
input_entry.grid(row=2, column=1, columnspan=2)
input_entry.insert(0, "139")

search_button = Button(text="Search Pairs", width=36, command=search_pairs)
search_button.grid(row=3, column=0, columnspan=2, pady=(5, 0))

blank_label = Label(text="")
blank_label.grid(row=4, column=0)

rights_label = Label(text="Diego Cabulo Dev", font=("Helvetica", 8, "italic"))
rights_label.grid(row=5, column=0, columnspan=2)

window.mainloop()


