# Import PrettyTable class from prettytable package
from prettytable import PrettyTable

# Create a new PrettyTable object
table = PrettyTable()

# Add columns to the table with their respective data
# First column: Pokemon names
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# Second column: Pokemon types
table.add_column("Type", ["Electric", "Water", "Fire"])

# Set left alignment for all columns
table.align = "l"

# Print the formatted table
print(table)
