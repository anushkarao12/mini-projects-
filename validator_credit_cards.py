import tkinter as tk
from tkinter import messagebox


class CreditCard:
    def __init__(self, card_no):
        self.card_no = card_no

    @property
    def company(self):
        comp = None
        if str(self.card_no).startswith("4"):
            comp = "Visa Card"
        elif str(self.card_no).startswith("5"):
            comp = "Master Card"
        elif str(self.card_no).startswith("37"):
            comp = "American Express Card"
        else:
            comp = "RuPay Card"
        return "Company card name: " + comp

    def first_check(self):
        if 13 <= len(self.card_no) <= 19:
            return "First check: Valid in terms of length."
        else:
            return "First check: Card number must be 13 to 19 digits."

    def validate_card_information(self):
        sum_ = 0
        crd_no = self.card_no[::-1]
        for i in range(len(crd_no)):
            if i % 2 == 1:
                double_it = int(crd_no[i]) * 2
                if double_it > 9:
                    sum_ += double_it - 9
                else:
                    sum_ += double_it
            else:
                sum_ += int(crd_no[i])

        return "Valid Card" if sum_ % 10 == 0 else "Invalid Card"

    @property
    def checksum(self):
        return "CHECKSUM: " + self.card_no[-1]

    @classmethod
    def set_card(cls, card_to_check):
        return cls(card_to_check)


# GUI Functions
def validate():
    card_no = entry.get().strip()
    if not card_no.isdigit():
        messagebox.showerror("Invalid Input", "Please enter digits only.")
        return

    card = CreditCard.set_card(card_no)
    output = [
        f"Card: {card.card_no}",
        card.company,
        card.first_check(),
        card.checksum,
        card.validate_card_information()
    ]
    result.config(text="\n".join(output))


# GUI Setup
root = tk.Tk()
root.title("Credit Card Validator")

tk.Label(root, text="Enter Credit Card Number:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Validate Card", command=validate).pack(pady=5)

result = tk.Label(root, text="", justify=tk.LEFT, fg="blue")
result.pack(pady=10)

root.mainloop()
