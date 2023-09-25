# Setting coordinates for each of the 8 directions an ant could travel in.
DIRECTIONS = [
    [0, 1], [1, 1], [1, 0], [1, -1],
    [0, -1], [-1, -1], [-1, 0], [-1, 1]
]


class Ant:
    """
    Initialize an Ant instance.

    Attributes:
        x_coord: an integer representing the x-coordinate of the ant's location.
        y_coord: an integer representing the y-coordinate of the ant's location.
        current_direction: A list of two integers representing the current direction of the ant.

    """

    def __init__(self, x_coord, y_coord, current_direction):
        """
        Initialize an Ant instance.

        Args:
            x_coord: an integer representing the x-coordinate of the ant's location.
            y_coord: an integer representing the y-coordinate of the ant's location.
            current_direction: A list of two integers representing the current direction of the ant.

        Returns: N/A        
        """
        # Setting attributes of all ants.
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.current_direction = current_direction
        self.calculate_next_possible_directions()

    def calculate_next_possible_directions(self):
        """
        Calculate the next possible directions for the ant based on its current direction.

        Args: N/A

        Returns:
            self.possible_directions: A list of lists (each with two integers) representing possible directions.
        """
        # Pulling index of current direction
        current_direction_index = DIRECTIONS.index(self.current_direction)

        # The three possible directions the ant can go is straight, left, and right.
        # These can be representing in context of the index of the current direction
        # by adding offsets to the index.
        offsets = [0, 1, -1]

        # Using loop to append straight, left, and right directions to possible directions.
        self.possible_directions = [
            DIRECTIONS[(current_direction_index + offset) % 8]
            for offset in offsets
        ]
        return self.possible_directions

    def pheromone_check(self, grid):
        """
        Check pheromone levels in neighboring directions and count the number of trails.

        Args:
            grid (list of list of float): A list of lists of floats representing the pheromone levels in the grid.

        Returns:
            neighbor_pheromone_levels: A list of floats representing pheromone levels in neighboring cells.
            trail_count: An integer representing the number of neighboring cells with nonzero pheromone levels.
        """
        # Initializing variables for function.
        neighbor_pheromone_levels = []
        trail_count = 0
        grid_size = len(grid)

        # For each of the possible directions the loop looks at the point the ant would go to if they were to travel in that direction.
        for dx, dy in self.possible_directions:
            new_x, new_y = self.x_coord + dx, self.y_coord + dy

            # Ensuring point is within the grid limits.
            if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
                pheromone = grid[new_x][new_y]
            else:
                pheromone = 0

            # Adding pheromone level of each point to list.
            neighbor_pheromone_levels.append(pheromone)

            # If the pheromone level is grearter than 0, an ant has been here before.
            # This direction could be a potential trail so the trail count is increased by 1.
            if pheromone > 0:
                trail_count += 1

        return neighbor_pheromone_levels, trail_count
