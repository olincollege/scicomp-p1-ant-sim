""" grid.py
The Grid class in this file represents the grid on which the ants move and deposit pheromones. It
includes methods for spawning ants, moving ants, and determining their next directions based on
pheromone levels and other factors.
"""

import random
import numpy as np
from ant import Ant
from ant import DIRECTIONS


class Grid:
    """
    Grid class for simulating ant trail formation.

    Attributes:
        size: Integer representing the size of the grid (square grid).
        deposition_rate: Float representing the rate at which the pheromone is deposited by ants.
        evaporation_rate: Float representing the rate at which the pheromone evaporates over time.
        fidelity: Float represent the probability of moving in the same direction).
        turn_probability: List of floats representing probabilities of turning in 45° increments.
    """

    def __init__(self, size, deposition_rate, evaporation_rate, fidelity, turn_probability):
        """
        Initialize a Grid instance.

        Args:
            size: Integer representing the size of the grid (square grid).
            deposition_rate: Float representing the rate at which the pheromone is deposited by 
            ants.
            evaporation_rate: Float representing the rate at which the pheromone evaporates over 
            time.
            fidelity: Float represent the probability of moving in the same direction).
            turn_probability: List of floats representing the probabilities of turning in 45° 
            increments.

        Returns: N/A        
        """
        # Setting attributes of grid.
        self.size = size
        self.current_grid = np.zeros((size, size))
        self.next_grid = np.zeros((size, size))
        self.deposition_rate = deposition_rate
        self.evaporation_rate = evaporation_rate
        self.fidelity = fidelity
        self.directions = DIRECTIONS
        self.current_ants = []
        self.next_ants = []
        self.turn_probability = turn_probability
        self.spawn_point = self.size // 2

    def spawn_ant(self):
        """
        Spawn a new ant on the grid.

        Args: N/A

        Returns: N/A
        """
        # Randomly setting direction of newly spawned ant.
        current_direction = random.choice(self.directions)

        # Setting x and y coordinates based on center of grid plus direction the ant is going.
        x_coord = self.spawn_point + current_direction[0]
        y_coord = self.spawn_point + current_direction[1]

        # Creating ant with calculated attributes.
        ant = Ant(x_coord=x_coord, y_coord=y_coord,
                  current_direction=current_direction)

        # Adding new ant to list of current ants.
        self.current_ants.append(ant)

    def exploring_ant(self, ant_direction):
        """
        Determine next direction when ant is in exploration mode.

        Args:
            ant_direction: A list of two integers representing the current direction of the ant.

        Returns:
            next_direction: A list of two integers representing the next direction of the ant.
        """
        # Selecting a random increment based on the turning kernel.
        # This increment represents the number of 45° increments the ant will move in.
        random_increment = int(np.random.choice(5, 1, p=self.turn_probability))

        # Getting index of current direction.
        current_direction_index = self.directions.index(ant_direction)
        # Randomly generating left or right based on whether the random number is less than 0.5
        if random.random() < 0.5:

            # Represents taking a left turn
            next_direction = self.directions[(
                current_direction_index + random_increment) % 8]

        else:
            # Represents taking a right turn
            next_direction = self.directions[(
                current_direction_index - random_increment + 8) % 8]

        return next_direction

    def trail_following_ant(self, possible_directions, neighbor_pheromone_levels, ant_direction):
        """
        Determine next direction when ant is in trail following mode.

        Args:
            possible_directions: A list of lists (each with two integers) representing possible
            directions.
            neighbor_pheromone_levels: A list of floats representing pheromone levels in
            neighboring cells.
            ant_direction: A list of two integers representing the current direction of the ant.            

        Returns:
            next_direction: A list of two integers representing the next direction of the ant.
        """
        # Checking fidelity if the number is less than the threshold the ant will follow the trail.
        if random.random() < self.fidelity:

            # Taking the value and index of the maximum pheromone level surrounding the ant.
            max_pheromone = max(neighbor_pheromone_levels)
            max_pheromone_index = neighbor_pheromone_levels.index(
                max_pheromone)

            # Picking corresponding direction of the index of the max pheromone.
            next_direction = possible_directions[max_pheromone_index]
        else:
            # If the fidelity threshold is crossed, the ant stops following a trail and starts
            # exploring.
            next_direction = self.exploring_ant(ant_direction)

        return next_direction

    def choose_forking_direction(self, possible_directions, neighbor_pheromone_levels,
                                 ant_direction):
        """
        Determine next direction when ant is in trail following mode and there are multiple trails
        available.

        Args:
            possible_directions: A list of lists (each with two integers) representing possible
            directions.
            neighbor_pheromone_levels: A list of floats representing pheromone levels in
            neighboring cells.
            ant_direction: A list of two integers representing the current direction of the ant.

        Returns:
            next_direction: A list of two integers representing the next direction of the ant.
        """
        # If there is a pheromone trail in the 0th index (which represents going straight) then go
        # straight.
        if neighbor_pheromone_levels[0] > 0:
            next_direction = possible_directions[0]

        # If the pheromone trail of the left fork is greater then go left.
        elif neighbor_pheromone_levels[1] > neighbor_pheromone_levels[2]:
            next_direction = possible_directions[1]

        # If the pheromone trail of the right fork is greater then go left.
        elif neighbor_pheromone_levels[2] > neighbor_pheromone_levels[1]:
            next_direction = possible_directions[2]

        # If there is no straight path and the left and right are equal, the ant stops following a
        # trail and starts exploring.
        else:
            next_direction = self.exploring_ant(ant_direction)

        return next_direction

    def choose_direction(self, ant):
        """
        Choose the next direction for an ant based on pheromone levels and trail count.

        Args:
            ant (Ant): An object of the Ant class representing the ant for which to choose the next
            direction.

        Returns:
            next_direction: A list of two integers representing the next direction of the ant.
        """
        # Finding possible directions based on the ant's current position.
        possible_directions = ant.calculate_next_possible_directions()

        # Checking pheromone levels and trail count in the current cell.
        neighbor_pheromone_levels, trail_count = ant.pheromone_check(
            self.current_grid)

        # Determining the direction for the ant based on trail count.
        # If there are no trails, explore a new direction.
        if trail_count == 0:
            next_direction = self.exploring_ant(ant.current_direction)

        # If there is only one trail, follow it.
        elif trail_count == 1:
            next_direction = self.trail_following_ant(
                possible_directions, neighbor_pheromone_levels, ant.current_direction)

        # If there are multiple trails, use the forking algorithm.
        else:
            next_direction = self.choose_forking_direction(
                possible_directions, neighbor_pheromone_levels, ant.current_direction)

        return next_direction

    def move(self):
        """
        Move ants on the grid according to the ant simulation rules.

        Args: N/A

        Returns: N/A        
        """
        # Going through all ants currenting in grid and updating the pheromone level of their
        # coordinates with the deposition rate.
        for ant in self.current_ants:
            self.next_grid[ant.x_coord][ant.y_coord] = (
                self.current_grid[ant.x_coord][ant.y_coord] +
                self.deposition_rate
                )

            # Determining next direction for the ant.
            next_direction = self.choose_direction(ant)

            # Updating coorindates and current direction based on selected next direction.
            ant.x_coord += next_direction[0]
            ant.y_coord += next_direction[1]
            ant.current_direction = next_direction

            # Checking is ant is still on the grid before appending to list of where ants will end
            # up next.
            if 0 <= ant.x_coord < self.size and 0 <= ant.y_coord < self.size:
                self.next_ants.append(ant)

        # Updating grid based on evaporation over time.
        np.subtract(self.next_grid, self.evaporation_rate)

        # Preventing any out of bound errors in next grid and automatically updating it.
        np.clip(self.next_grid, 0, None, out=self.next_grid)

        # Updating current grid and ants list to next state and resetting next ants list.
        self.current_grid = self.next_grid
        self.current_ants = self.next_ants
        self.next_ants = []
