import tkinter as tk
from tkinter import ttk, messagebox

# --- Logic Classes ---
class Sentence():
    def evaluate(self, model): raise Exception("Nothing to evaluate")
    def formula(self): return ""
    def symbols(self): return set()
    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence): raise TypeError("Must be a logical sentence")
    @classmethod
    def parenthesize(cls, s):
        def balanced(s):
            count = 0
            for c in s:
                if c == "(": count += 1
                elif c == ")":
                    if count <= 0: return False
                    count -= 1
            return count == 0
        return s if not s or s.isalpha() or (s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])) else f"({s})"

class Symbol(Sentence):
    def __init__(self, name): self.name = name
    def __repr__(self): return self.name
    def evaluate(self, model): return bool(model[self.name])
    def formula(self): return self.name
    def symbols(self): return {self.name}

class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand
    def evaluate(self, model): return not self.operand.evaluate(model)
    def formula(self): return "¬" + Sentence.parenthesize(self.operand.formula())
    def symbols(self): return self.operand.symbols()

class And(Sentence):
    def __init__(self, *conjuncts):
        for c in conjuncts: Sentence.validate(c)
        self.conjuncts = list(conjuncts)
    def evaluate(self, model): return all(c.evaluate(model) for c in self.conjuncts)
    def formula(self): return " ∧ ".join(Sentence.parenthesize(c.formula()) for c in self.conjuncts)
    def symbols(self): return set.union(*[c.symbols() for c in self.conjuncts]) if self.conjuncts else set()

class Or(Sentence):
    def __init__(self, *disjuncts):
        for d in disjuncts: Sentence.validate(d)
        self.disjuncts = list(disjuncts)
    def evaluate(self, model): return any(d.evaluate(model) for d in self.disjuncts)
    def formula(self): return " ∨ ".join(Sentence.parenthesize(d.formula()) for d in self.disjuncts)
    def symbols(self): return set.union(*[d.symbols() for d in self.disjuncts]) if self.disjuncts else set()

class Implication(Sentence):
    def __init__(self, a, c):
        Sentence.validate(a); Sentence.validate(c)
        self.a = a; self.c = c
    def evaluate(self, model): return not self.a.evaluate(model) or self.c.evaluate(model)
    def formula(self): return f"{Sentence.parenthesize(self.a.formula())} => {Sentence.parenthesize(self.c.formula())}"
    def symbols(self): return self.a.symbols().union(self.c.symbols())

class Biconditional(Sentence):
    def __init__(self, l, r):
        Sentence.validate(l); Sentence.validate(r)
        self.l = l; self.r = r
    def evaluate(self, model): return self.l.evaluate(model) == self.r.evaluate(model)
    def formula(self): return f"{Sentence.parenthesize(self.l.formula())} <=> {Sentence.parenthesize(self.r.formula())}"
    def symbols(self): return self.l.symbols().union(self.r.symbols())

def model_check(knowledge, query):
    def check_all(knowledge, query, symbols, model):
        if not symbols: return not knowledge.evaluate(model) or query.evaluate(model)
        remaining = symbols.copy()
        p = remaining.pop()
        return (check_all(knowledge, query, remaining, {**model, p: True}) and
                check_all(knowledge, query, remaining, {**model, p: False}))
    return check_all(knowledge, query, knowledge.symbols().union(query.symbols()), {})

# --- Default Puzzles ---
AKnight = Symbol("A is a Knight"); AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight"); BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight"); CKnave = Symbol("C is a Knave")

puzzles = [
    ("Puzzle 0", And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave)),
        Implication(AKnight, And(AKnight, AKnave))
    )),
    ("Puzzle 1", And(
        Or(AKnight, AKnave), Or(BKnight, BKnave),
        Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)),
        Implication(AKnight, And(AKnave, BKnave)),
        Implication(AKnave, Not(And(AKnave, BKnave)))
    )),
    ("Puzzle 2", And(
        Or(AKnight, AKnave), Or(BKnight, BKnave),
        Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)),
        Implication(AKnight, Biconditional(AKnight, BKnight)),
        Implication(AKnave, Not(Biconditional(AKnight, BKnight))),
        Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
        Implication(BKnave, Biconditional(AKnight, BKnight))
    )),
    ("Puzzle 3", And(
        Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave),
        Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave)), Not(And(CKnight, CKnave)),
        Implication(BKnight, And(AKnave, CKnave)),
        Implication(BKnave, Or(AKnight, Not(CKnave))),
        Implication(CKnight, AKnight)
    ))
]

all_symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]


# --- GUI App ---
class PuzzleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Knights and Knaves Puzzle Solver")
        self.geometry("700x600")
        self.create_widgets()

    def create_widgets(self):
        # Dropdown for puzzles
        ttk.Label(self, text="Choose Puzzle:").pack()
        self.combo = ttk.Combobox(self, values=[name for name, _ in puzzles] + ["Custom Puzzle"], state="readonly")
        self.combo.current(0)
        self.combo.pack(pady=5)
        self.combo.bind("<<ComboboxSelected>>", self.toggle_custom_input)

        # Text area for custom puzzle input
        self.custom_input = tk.Text(self, height=5)
        self.custom_input.pack(fill="x", padx=10)
        self.custom_input.insert("1.0", 'And(Symbol("A is a Knight"), Not(Symbol("B is a Knight")))')
        self.custom_input.configure(state="disabled")

        # Solve button
        ttk.Button(self, text="Solve Puzzle", command=self.solve_puzzle).pack(pady=10)

        # Output area
        self.output = tk.Text(self, height=20, wrap="word")
        self.output.pack(expand=True, fill="both", padx=10, pady=5)

    def toggle_custom_input(self, event=None):
        if self.combo.get() == "Custom Puzzle":
            self.custom_input.configure(state="normal")
        else:
            self.custom_input.configure(state="disabled")

    def solve_puzzle(self):
        self.output.delete("1.0", tk.END)
        selected = self.combo.get()

        try:
            if selected == "Custom Puzzle":
                expr = self.custom_input.get("1.0", tk.END).strip()
                knowledge = eval(expr, {}, {
                    "And": And, "Or": Or, "Not": Not, "Implication": Implication, "Biconditional": Biconditional, "Symbol": Symbol
                })
            else:
                knowledge = dict(puzzles)[selected]
        except Exception as e:
            self.output.insert(tk.END, f"❌ Error in custom puzzle:\n{e}")
            return

        self.output.insert(tk.END, f"✅ Solving {selected}\n\n")
        found = False
        for symbol in all_symbols:
            try:
                if model_check(knowledge, symbol):
                    self.output.insert(tk.END, f"✔ {symbol}\n")
                    found = True
            except Exception:
                continue
        if not found:
            self.output.insert(tk.END, "No conclusions could be drawn.")

# --- Run App ---
if __name__ == "__main__":
    PuzzleApp().mainloop()
