""" plot.py
This script provides a command-line interface for running the simulation and visualizing the
results. It allows you to specify parameters such as grid size, deposition rate, evaporation rate,
fidelity, and turn probability. After running the simulation, it generates a heatmap to visualize
the pheromone trail formation.
"""

import argparse
import matplotlib.pyplot as plt
from grid import Grid


def simulate_ant_trail(size, deposition_rate, evaporation_rate, fidelity, turn_probability,
                       num_iterations):
    """
    Simulate the behavior of ants depositing pheromones on a grid and the ensuing trails which form.

    Args:
        size: Integer representing the size of the grid (square grid).
        deposition_rate: Float representing the rate at which the pheromone is deposited by ants.
        evaporation_rate: Float representing the rate at which the pheromone evaporates over time.
        fidelity: Float represent the probability of moving in the same direction).
        turn_probability: List of floats representing the probabilities of turning in 45°
        increments.
        num_iterations: Integer representing the number of iterations to run the simulation.

    Returns:
        grid.current_grid: List of lists representing the final state of the grid after the
        simulation is complete.
    """
    # Initializing grid
    grid = Grid(size=size, deposition_rate=deposition_rate, evaporation_rate=evaporation_rate,
                fidelity=fidelity, turn_probability=turn_probability)

    # Running num_iterations of spawning a new ant and then moving all other ants.
    for _ in range(num_iterations):
        grid.spawn_ant()
        grid.move()

    return grid.current_grid


def main():
    """
    Run the main simulation and visualization of ant trail formation.

    Args: N/A

    Returns:N/A
    """
    # Using parser to add flexibility in calling plot from terminal and adjusting various values in
    # the command line.
    # Each is set with a default but can be changed when the flag is specified.
    parser = argparse.ArgumentParser(
        description="Simulate ant trail formation and visualize the grid.")
    parser.add_argument("--size", type=int, default=256,
                        help="Grid size (default: 256)")
    parser.add_argument("--deposition_rate", type=float,
                        default=5, help="Deposition rate (default: 5)")
    parser.add_argument("--evaporation_rate", type=float,
                        default=1, help="Evaporation rate (default: 1)")
    parser.add_argument("--fidelity", type=float,
                        default=0.6, help="Fidelity (default: 0.6)")
    parser.add_argument("--turn_probability", nargs="+", type=float, default=[
                        0.3, 0.3, 0.22, 0.13, 0.05], help=
                        "Turn probability (default: [0.3, 0.3, 0.22, 0.13, 0.05])")
    parser.add_argument("--num_iterations", type=int, default=1000,
                        help="Number of iterations (default: 1000)")
    parser.add_argument("--title", type=str, default="Trail Formation by Ants",
                        help="Title for the plot (default: 'Trail Formation by Ants')")

    # Passing any user input to args (if there is none it will pass the default values).
    args = parser.parse_args()
    turn_probabilities = args.turn_probability

    # Calling simulation function to get final state of the grid.
    final_grid = simulate_ant_trail(
        size=args.size,
        deposition_rate=args.deposition_rate,
        evaporation_rate=args.evaporation_rate,
        fidelity=args.fidelity,
        turn_probability=turn_probabilities,
        num_iterations=args.num_iterations
    )

    # Plotting final state of grid with a gradient representing strength of trail with color
    # gradient.
    fig, sub = plt.subplots()
    color = sub.pcolormesh(final_grid, cmap='Greys')
    sub.set_title(args.title)
    fig.colorbar(color, ax=sub)
    fig.patch.set_facecolor('White')
    plt.show()


if __name__ == "__main__":
    main()
    plt.gcf().clear()
