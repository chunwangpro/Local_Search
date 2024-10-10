# N-Queens Problem: Local Search Approximation Algorithms

This project implements several search algorithms to solve the N-Queens problem, including Hill Climbing, Simulated Annealing, and Genetic Algorithm. Each algorithm aims to efficiently place N queens on an N×N chessboard such that no two queens attack each other.

## Background

Suppose each queen is assigned to a particular column and constrained to move along that column alone. Each state is represented by `n` digits, with the `c`-th digit representing the row number of the queen in column `c`. The columns are counted left to right starting at `0` for the leftmost column and `0` for the topmost row. We give a utility function `h` that computes the number of conflict pairs (i.e., cost) in `utils.py`.

## Algorithms Implemented

- **Hill Climbing**: A local search algorithm that iteratively improves the solution by making small changes, hoping to reach the optimal solution.
  
- **Simulated Annealing**: An optimization algorithm inspired by the annealing process in metallurgy. It explores the solution space more broadly at the beginning, allowing worse solutions to avoid local optima, and gradually narrows down as the temperature decreases.
  
- **Genetic Algorithm**: A population-based search algorithm inspired by natural selection. It evolves a population of candidate solutions using operations like mutation, crossover, and selection to find an optimal or near-optimal solution.

## Running the Algorithms

Each algorithm is implemented in a separate Python file. To solve the N-Queens problem with a specific algorithm, simply run the corresponding Python file. The implementation uses the `if __name__ == "__main__":` construct to automatically execute the algorithm when the script is run.

### Hill Climbing

To run the Hill Climbing algorithm, use the following command:

```bash
python hill_climbing.py
```

### Simulated Annealing

To run the Simulated Annealing algorithm, use the following command:

```
python simulated_annealing.py
```

### Genetic Algorithm

To run the Genetic Algorithm, use the following command:

```
python genetic_algorithm.py
```

## Customizing the Problem Size

By default, the algorithms are set to solve an 8-Queens problem. You can modify the size of the board by editing the `N` variable at the beginning of each script. For example, to solve the 16-Queens problem, change the value of `N` to 16 in the respective Python file:

```
N = 10
```

## Results

After running each algorithm, the solution (if found) will be printed in the terminal along with a visual representation of the N-Queens board. The number of steps, iterations, or generations (depending on the algorithm) will also be displayed, giving insight into the efficiency of the solution process.

## Performance Comparison

Each algorithm has different strengths:

- **Hill Climbing** is fast but may get stuck in local optima.
- **Simulated Annealing** avoids local optima more effectively but can take longer to converge.
- **Genetic Algorithm** offers a diverse exploration of the solution space but may require tuning of parameters like population size and mutation rate.

You can experiment with different N sizes and compare the performance of each algorithm based on the time taken and the number of steps to find a solution.
