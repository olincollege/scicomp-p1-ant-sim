import tkinter as tk
import time
import sys  # Import sys to exit the program

class Object:
    def __init__(self, index, position):
        self.index = index
        self.position = position

def update_objects():
    # Create a new object at (0, 0)
    new_object = Object(len(objects), (0, 0))
    objects.append(new_object)

    # Move all previously existing objects
    for obj in objects:
        x, y = obj.position
        obj.position = (x + 1, y + 1)

        # Update the visit count for the current position (capped at 10)
        visit_counts[x][y] = min(visit_counts[x][y] + 1, 10)

    # Update the canvas to display the objects and gradient
    canvas.delete("all")
    for obj in objects:
        x, y = obj.position
        # Draw a colored square (rectangle) to represent the object
        count = visit_counts[x][y]
        color_value = int((count / 10) * 255)
        color = f"#{255 - color_value:02X}{255 - color_value:02X}{255 - color_value:02X}"
        canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color)

    # Update the total object count
    total_objects_label.config(text=f"Total Objects: {len(objects)}")

    # Schedule the update function to run again after 2 seconds
    root.after(2000, update_objects)

# Function to quit the program when "q" is pressed
def quit_program(event):
    root.quit()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Object Tracker")

# Bind the "q" key to the quit_program function
root.bind("q", quit_program)

# Create a canvas to display the objects and gradient
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()

# Create a label to display the total object count
total_objects_label = tk.Label(root, text="Total Objects: 0")
total_objects_label.pack()

objects = []  # List to store objects

# Initialize visit counts grid
visit_counts = [[0 for _ in range(3000)] for _ in range(3000)]

# Start the update loop
update_objects()

root.mainloop()
