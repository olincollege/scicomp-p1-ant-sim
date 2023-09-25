# Ant Trail Formation Simulation

This project simulates the behavior of ants depositing pheromones on a grid and the formation of trails. The simulation is controlled by various parameters, including grid size, deposition rate, evaporation rate, fidelity, and turn probability. This model comes from the paper "Modelling the Formation of Trail Networks by Foraging Ants" by James Watmough and Leah Edelstein-Keshet. 

This project uses the following libraries:
- numpy
- matplotlib
- argparse
- random

For easy install, you can run the following command which will install numpy and matplotlib. Random and argparse are standard modules in python and shouldn't need to be installed.

```bash
pip install numpy matplotlib
```

The project consists of the following Python files:

## ant.py

This file defines the `Ant` class, which represents an individual ant in the simulation. It contains methods for calculating possible directions, checking pheromone levels, and determining the next direction for an ant.

## grid.py

The `Grid` class in this file represents the grid on which the ants move and deposit pheromones. It includes methods for spawning ants, moving ants, and determining their next directions based on pheromone levels and other factors.

## plot.py

This script provides a command-line interface for running the simulation and visualizing the results. It allows you to specify parameters such as grid size, deposition rate, evaporation rate, fidelity, and turn probability. After running the simulation, it generates a heatmap to visualize the pheromone trail formation.

## results.ipynb

This Jupyter Notebook contains code cells that run the simulation with different parameter values and visualize the results. It uses the `plot.py` script to conduct multiple simulations and compare the outcomes.

## How to Run the Simulation

To run the simulation and visualize the results, you can use the following command:

```bash
python plot.py [--options]
```
Replace **[--options]** with the desired command-line options to customize the simulation. Here are some examples of how to use the script:

- **size**: Specify the grid size (default: 256).
- **deposition_rate**: Set the deposition rate (default: 5).
- **evaporation_rate**: Adjust the evaporation rate (default: 1).
- **fidelity**: Define the fidelity (probability of moving in the same direction) (default: 0.6).
- **turn_probability**: Specify the probabilities of turning in 45° increments (default: [0.3, 0.3, 0.22, 0.13, 0.05]).
- **num_iterations**: Set the number of simulation iterations (default: 1000).
- **title**: Provide a title for the visualization (default: "Trail Formation by Ants").

## Example Usage

Here are some example commands to run the simulation with different parameter settings:

```bash
python plot.py --fidelity 0.4 --title "Trail Formation by Ants: Fidelity = 0.4"
python plot.py --deposition_rate 8 --title "Trail Formation by Ants: Deposition Rate = 8"
python plot.py --turn_probability 0.32 0.3 0.22 0.13 0.03 --title "Trail Formation by Ants: Narrow Turning Kernel"
```
Feel free to experiment with different parameter values to observe how they affect the formation of ant trails on the grid.

Enjoy exploring the fascinating world of ant trail formation through this simulation!
