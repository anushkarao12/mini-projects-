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
            message = "First check : Valid in terms of length."

        else:
            message = "First check : Check Card number once again it must be of 13 or 16 digits long."
        return message

    def validate_card_information(self):
        # double every second digit from right to left
        sum_ = 0
        crd_no = self.card_no[::-1]
        for i in range(len(crd_no)):
            if i % 2 == 1:
                double_it = int(crd_no[i]) * 2

                if len(str(double_it)) == 2:
                    sum_ += sum([eval(i) for i in str(double_it)])

                else:
                    sum_ += double_it

            else:
                sum_ += int(crd_no[i])

        if sum_ % 10 == 0:
            response = "Valid Card"
        else:
            response = "Invalid Card"

        return response

    @property
    def checksum(self):
        return "CHECKSUM : " + self.card_no[-1]

    @classmethod
    def set_card(cls, card_to_check):
        return cls(card_to_check)


card_number = input('Enter a card number: ')
card = CreditCard.set_card(card_number)
print(card.company)
print("Card : ", card.card_no)
print(card.first_check())
print(card.checksum)
print(card.validate_card_information())
