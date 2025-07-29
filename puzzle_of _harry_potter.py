import tkinter as tk
from tkinter import ttk, scrolledtext
from logic import *
from termcolor import colored

def run_house_assignment():
    people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    symbols = [Symbol(f"{person}{house}") for person in people for house in houses]
    knowledge = And()

    for person in people:
        knowledge.add(Or(*[Symbol(f"{person}{house}") for house in houses]))
        for h1 in houses:
            for h2 in houses:
                if h1 != h2:
                    knowledge.add(Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}"))))

    for house in houses:
        for p1 in people:
            for p2 in people:
                if p1 != p2:
                    knowledge.add(Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}"))))

    knowledge.add(Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw")))
    knowledge.add(Not(Symbol("PomonaSlytherin")))
    knowledge.add(Symbol("MinervaGryffindor"))

    results = []
    for symbol in symbols:
        if model_check(knowledge, symbol):
            results.append(f"{symbol}")
    return "\n".join(results)


def run_color_order():
    colors = ["red", "blue", "green", "yellow"]
    symbols = [Symbol(f"{color}{i}") for i in range(4) for color in colors]
    knowledge = And()

    for color in colors:
        knowledge.add(Or(*[Symbol(f"{color}{i}") for i in range(4)]))
        for i in range(4):
            for j in range(4):
                if i != j:
                    knowledge.add(Implication(Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))))

    for i in range(4):
        for c1 in colors:
            for c2 in colors:
                if c1 != c2:
                    knowledge.add(Implication(Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))))

    knowledge.add(Or(
        And(Symbol("red0"), Symbol("blue1"), Not(Symbol("green2")), Not(Symbol("yellow3"))),
        And(Symbol("red0"), Symbol("green2"), Not(Symbol("blue1")), Not(Symbol("yellow3"))),
        And(Symbol("red0"), Symbol("yellow3"), Not(Symbol("blue1")), Not(Symbol("green2"))),
        And(Symbol("blue1"), Symbol("green2"), Not(Symbol("red0")), Not(Symbol("yellow3"))),
        And(Symbol("blue1"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("green2"))),
        And(Symbol("green2"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("blue1")))
    ))

    knowledge.add(And(
        Not(Symbol("blue0")),
        Not(Symbol("red1")),
        Not(Symbol("green2")),
        Not(Symbol("yellow3"))
    ))

    results = []
    for symbol in symbols:
        if model_check(knowledge, symbol):
            results.append(f"{symbol}")
    return "\n".join(results)


def run_rain_logic():
    rain = Symbol("rain")
    hagrid = Symbol("hagrid")
    dumbledore = Symbol("dumbledore")

    knowledge = And(
        Implication(Not(rain), hagrid),
        Or(hagrid, dumbledore),
        Not(And(hagrid, dumbledore)),
        dumbledore
    )
    return f"Rain is {model_check(knowledge, rain)}"


def run_clue_logic():
    mustard = Symbol("ColMustard")
    plum = Symbol("ProfPlum")
    scarlet = Symbol("MsScarlet")
    characters = [mustard, plum, scarlet]

    ballroom = Symbol("ballroom")
    kitchen = Symbol("kitchen")
    library = Symbol("library")
    rooms = [ballroom, kitchen, library]

    knife = Symbol("knife")
    revolver = Symbol("revolver")
    wrench = Symbol("wrench")
    weapons = [knife, revolver, wrench]

    symbols = characters + rooms + weapons

    knowledge = And(
        Or(mustard, plum, scarlet),
        Or(ballroom, kitchen, library),
        Or(knife, revolver, wrench)
    )

    knowledge.add(And(
        Not(mustard), Not(kitchen), Not(revolver)
    ))

    knowledge.add(Or(
        Not(scarlet), Not(library), Not(wrench)
    ))

    knowledge.add(Not(plum))
    knowledge.add(Not(ballroom))

    results = []
    for symbol in symbols:
        if model_check(knowledge, symbol):
            results.append(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            results.append(f"{symbol}: MAYBE")
    return "\n".join(results)

# ---------------- Tkinter GUI ----------------

def run_selected_puzzle():
    puzzle = combo.get()
    if puzzle == "House Assignment":
        output = run_house_assignment()
    elif puzzle == "Color Order Puzzle":
        output = run_color_order()
    elif puzzle == "Rain, Hagrid, Dumbledore":
        output = run_rain_logic()
    elif puzzle == "Clue Logic Puzzle":
        output = run_clue_logic()
    else:
        output = "Please select a puzzle!"
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)

root = tk.Tk()
root.title("Logic Puzzle Solver 🧠")
root.geometry("650x550")

tk.Label(root, text="Select a Puzzle:", font=("Helvetica", 14)).pack(pady=10)
combo = ttk.Combobox(root, values=[
    "House Assignment",
    "Color Order Puzzle",
    "Rain, Hagrid, Dumbledore",
    "Clue Logic Puzzle"
])
combo.pack(pady=5)

run_button = tk.Button(root, text="Run Puzzle", command=run_selected_puzzle)
run_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25)
output_text.pack(pady=10)

root.mainloop()
