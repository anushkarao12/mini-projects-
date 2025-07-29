import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import logging
from typing import Callable, List

logging.basicConfig(level=logging.INFO)

def randomization(n: int) -> np.ndarray:
    """Generates a random n x 1 matrix."""
    A = np.random.rand(n, 1)
    logging.info(f"Randomized {n}x1 array: {A.flatten()}")
    return A

def operations(h: int, w: int) -> tuple:
    """Generates two random h x w matrices and returns their sum."""
    A = np.random.rand(h, w)
    B = np.random.rand(h, w)
    S = A + B
    logging.info(f"Matrix A:\n{A}\nMatrix B:\n{B}\nSum:\n{S}")
    return A, B, S

def norm(A: np.ndarray, B: np.ndarray) -> float:
    """Returns the L2 norm of the sum of two arrays."""
    result = np.linalg.norm(A + B)
    logging.info(f"L2 Norm of A + B: {result}")
    return result

def neural_network(inputs: np.ndarray, weights: np.ndarray, activation: str = 'tanh') -> np.ndarray:
    """1-layer neural network with customizable activation."""
    z = weights.T @ inputs
    if activation == 'tanh':
        output = np.tanh(z)
    elif activation == 'sigmoid':
        output = 1 / (1 + np.exp(-z))
    elif activation == 'relu':
        output = np.maximum(0, z)
    else:
        raise ValueError("Unsupported activation")
    logging.info(f"NN output with {activation}: {output}")
    return output

def gen_add_i(i: int) -> Callable[[int], int]:
    return lambda x: x + i

def get_sum_metrics(prediction: int, metrics: List[Callable[[int], int]] = None) -> int:
    if metrics is None:
        metrics = []
    for i in range(3):
        metrics.append(gen_add_i(i))
    sum_metrics = sum(metric(prediction) for metric in metrics)
    logging.info(f"Sum metrics for prediction={prediction}: {sum_metrics}")
    return sum_metrics

def plot_matrix(matrix: np.ndarray, title: str):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NumPy Neural Demo")
        self.geometry("500x300")

        ttk.Button(self, text="Random Vector", command=self.random_vector).pack(pady=10)
        ttk.Button(self, text="Matrix Operations", command=self.matrix_ops).pack(pady=10)
        ttk.Button(self, text="Neural Network", command=self.nn_demo).pack(pady=10)
        ttk.Button(self, text="Sum Metrics", command=self.metrics_demo).pack(pady=10)

    def random_vector(self):
        n = simpledialog.askinteger("Input", "Enter dimension n:")
        if n:
            vec = randomization(n)
            messagebox.showinfo("Random Vector", f"{vec.flatten()}")

    def matrix_ops(self):
        h = simpledialog.askinteger("Input", "Enter height h:")
        w = simpledialog.askinteger("Input", "Enter width w:")
        if h and w:
            A, B, S = operations(h, w)
            plot_matrix(S, "A + B")

    def nn_demo(self):
        inputs = np.random.rand(2, 1)
        weights = np.random.rand(2, 1)
        out = neural_network(inputs, weights, activation='tanh')
        messagebox.showinfo("Neural Output", f"Output: {out.flatten()[0]:.4f}")

    def metrics_demo(self):
        pred = simpledialog.askinteger("Input", "Enter prediction integer:")
        if pred is not None:
            total = get_sum_metrics(pred, [lambda x: x])
            messagebox.showinfo("Metric Sum", f"Total: {total}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
