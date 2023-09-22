from ant import Grid
import matplotlib.pyplot as plt

# Initialize grid
grid = Grid(s=256, 
            deposition_rate = 5, 
            evaporation_rate = 1,
            fidelity = 0.6,
            turnProbability = [0.3, 0.3, 0.22, 0.13, 0.05])

# Simulate ant trail formation
for _ in range(1500):
    grid.ant_spawn()
    grid.move()
    
# Visualize grid
fig, ax = plt.subplots()
c = ax.pcolormesh(grid.z, cmap='Greys')
ax.set_title("Ant Trail Formation")
fig.colorbar(c, ax=ax)
fig.patch.set_facecolor('White')
plt.show()