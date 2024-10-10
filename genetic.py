import copy
import random

import numpy as np
from tqdm import tqdm

from utils import *

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)


def fitness(state: list) -> int:
    """
    Calculate fitness based on the number of non-conflicting pairs.

    Parameters
    ----------
    state : list
        List of length N representing current queen state (positions), where row and column index start from 0. Here N is the number of queens.

    Returns
    -------
    int
        Fitness score, i.e., the number of non-conflicting pairs.
    """
    N = len(state)
    total_pairs = (N * (N - 1)) // 2
    conflicts = h(state)
    return total_pairs - conflicts


def reproduce(parent1: list, parent2: list) -> tuple[list, list]:
    """
    Reproduce two parents by combining their genes at a random crossover point.

    Parameters
    ----------
    parent1 : list
        First parent state (list of queen positions).
    parent2 : list
        Second parent state (list of queen positions).

    Returns
    -------
    child1: list
        First child state created from parent1 and parent2.
    child2: list
        Second child state created from parent1 and parent2.
    """
    N = len(parent1)
    crossover_point = np.random.randint(1, N)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(state: list, mutation_rate: float = 0.1) -> list:
    """
    Mutate the state with a given mutation rate by randomly changing one queen's position.

    Parameters
    ----------
    state : list
        List of length N representing current queen state (positions), where row and column index start from 0. Here N is the number of queens.
    mutation_rate : float
        Probability of mutation.

    Returns
    -------
    list
        Mutated state.
    """
    if np.random.random() < mutation_rate:
        N = len(state)
        col = np.random.randint(0, N)
        # it is possible to move to the same row in mutation, so
        new_row = np.random.randint(0, N)
        state[col] = new_row
    return state


def genetic_algorithm(
    population: list, mutation_rate: float = 0.1, max_iter: int = 100
) -> tuple[list, int]:
    """
    Genetic algorithm for solving the N-queens problem.

    Parameters
    ----------
    population : list
        Initial population of states.
    mutation_rate : float
        Probability of mutation.
    max_iter : int
        Number of max_iter to run the algorithm.

    Returns
    -------
    best_state : list
        The best state found in the final round of population, measured by highest fitness score.
    min_h : int
        Minimum h value encountered during the algorithm.
    """
    N = len(population[0])  # Number of queens
    population_size = len(population)
    min_h = min(h(state) for state in population)

    for _ in range(max_iter):
        fitness_values = [fitness(state) for state in population]
        total_fitness = sum(fitness_values)
        probabilities = [f / total_fitness for f in fitness_values]

        new_population = []
        for _ in range(population_size // 2):
            parent_indices = np.random.choice(
                population_size, size=2, p=probabilities, replace=False
            )
            parent1, parent2 = population[parent_indices[0]], population[parent_indices[1]]

            child1, child2 = reproduce(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population
        # print(f"Population: {population}")
        min_h = min(min_h, min([h(state) for state in population]))

    best_state = max(population, key=fitness)
    return best_state, min_h


def run_experiments(
    N: int = 8,
    population_size: int = 4,
    mutation_rate: float = 0.1,
    max_iter: int = 100,
    num_runs: int = 2000,
) -> list:
    """
    Run the genetic algorithm for multiple times and return the average minimum h value.

    Parameters
    ----------
    N : int, optional
        Number of queens (default is 8).
    population_size : int, optional
        Size of the population (default is 4).
    num_runs : int
        Number of runs to perform (default is 2000).

    Returns
    -------
    min_h_history: list of int
        List of length num_runs representing the history of the minimum h value across all runs.
    """
    min_h_history = []

    for _ in tqdm(range(num_runs)):
        # Uniform sampling of initial population
        population = [np.random.randint(0, N, N).tolist() for _ in range(population_size)]
        # print(f"Initial population: {population}")
        _, min_h = genetic_algorithm(population, mutation_rate, max_iter)
        min_h_history.append(min_h)
    return min_h_history


if __name__ == "__main__":
    N = 8
    print(f"Running Genetic algorithm for {N}-Queens problem...")
    population_size = 4
    mutation_rate = 0.1
    max_iter = 100
    num_runs = 2000

    min_h_history = run_experiments(N, population_size, mutation_rate, max_iter, num_runs)
    # print(min_h_history)
    # print(min(min_h_history), max(min_h_history))

    avg_min_h = np.mean(min_h_history)
    print(f"Empirical average of min_h over {num_runs} runs:  {avg_min_h}")
