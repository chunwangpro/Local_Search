import copy

from utils import *


def get_best_successor(current_state):
    """
    Find the best successor by evaluating all possible queen moves from current state.
    """
    N = len(current_state)
    current_h = h(current_state)
    best_state = copy.deepcopy(current_state)
    best_h = current_h

    # check all possible state space
    for col in range(N):
        for row in range(N):
            if current_state[col] == row:
                continue  # Try another sampling if the queen is already in this row
            new_state = copy.deepcopy(current_state)
            new_state[col] = row
            new_h = h(new_state)
            # If this new state has fewer conflicts, update best state (steepest-ascent fashion)
            if new_h < best_h:
                best_state, best_h = new_state, new_h
    return best_state, best_h


def hill_climbing(initial_state):
    """The hill-climbing algorithm in steepest-ascent fashion."""
    current_state = initial_state
    current_h = h(initial_state)

    while True:
        next_state, next_h = get_best_successor(current_state)
        if next_h >= current_h:
            print("reached a local minimum")
            break
        current_state, current_h = next_state, next_h
        print(f"State: {current_state}, Conflicts: {current_h}")
    return current_state, current_h


if __name__ == "__main__":
    initial_state = [3, 1, 3, 1]
    print(f"\nInitial State: {initial_state}, Initial Conflicts: {h(initial_state)}\n")
    final_state, final_h = hill_climbing(initial_state)
    print(f"\nFinal State: {final_state}, Final Conflicts: {final_h}\n")
