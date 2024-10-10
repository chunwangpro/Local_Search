import copy
import random

import numpy as np
from tqdm import tqdm

from utils import *

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)


def generate_random_successor(state: list) -> list:
    """
    Generate a successor from the current state by uniformly choosing a single queen in a random column and move it to a new (different) row.

    Parameters
    ----------
    state : list
        List of length N representing current queen state (positions), where row and column index start from 0. Here N is the number of queens.

    Returns
    -------
    new_state: list
        New state after randomly moving one queen to a new (different) row.
    """
    N = len(state)
    new_state = copy.deepcopy(state)
    col = np.random.randint(0, N)
    while (new_row := np.random.randint(0, N)) == state[col]:
        # Try another sampling if the queen is already in this row
        pass
    new_state[col] = new_row
    return new_state


def schedule(t: int) -> float:
    """
    Temperature scheduling function: T = 1 - t/100.

    Parameters
    ----------
    t : int
        Current iteration step.

    Returns
    -------
    float
        Temperature at time step t.
    """
    return max(1 - t / 100, 0)


def simulated_annealing(initial_state: list, schedule: callable) -> tuple[list, int]:
    """
    Simulated annealing algorithm for solving the n-queens problem.

    Parameters
    ----------
    initial_state : list
        List of length N representing initial queen state (positions), where row and column index start from 0. Here N is the number of queens.
    schedule : callable
        Monotonically decreasing function that returns the temperature at a given time step.

    Returns
    -------
    current: list
        Final state after simulated annealing.
    min_h: int
        Minimum h value (number of conflicts) encountered during the run.
    """
    current = initial_state
    min_h = current_h = h(current)
    for t in range(1, 101):  # stops at iterations 100, from t=1 to t=100
        if (T := schedule(t)) == 0:
            break
        next_state = generate_random_successor(current)
        next_h = h(next_state)
        delta_e = current_h - next_h
        if delta_e > 0 or np.random.random() < np.exp(delta_e / T):
            current, current_h = next_state, next_h
            min_h = min(min_h, current_h)
    return current, min_h


def run_experiments(N: int = 8, num_runs: int = 2000) -> list:
    """
    Run the simulated annealing algorithm on N-queen problem for multiple times and report the minimum h history.

    Parameters
    ----------
    N : int, optional
        Number of queens (default is 8).
    num_runs : int, optional
        Number of runs to perform (default is 2000).

    Returns
    -------
    min_h_history: list of int
        List of length num_runs representing the history of the minimum h value across all runs.
    """
    min_h_history = []
    for _ in tqdm(range(num_runs)):
        # Uniform sampling of initial state
        initial_state = np.random.randint(0, N, N).tolist()
        # print(f"Initial State: {initial_state}")
        _, min_h = simulated_annealing(initial_state, schedule)
        min_h_history.append(min_h)
    return min_h_history


if __name__ == "__main__":
    N = 8
    print(f"Running Simulated Annealing algorithm for {N}-Queens problem...")
    num_runs = 2000

    min_h_history = run_experiments(N, num_runs)
    # print(min_h_history)
    # print(min(min_h_history), max(min_h_history))

    avg_min_h = np.mean(min_h_history)
    print(f"Empirical average of min_h over {num_runs} runs:  {avg_min_h}")
