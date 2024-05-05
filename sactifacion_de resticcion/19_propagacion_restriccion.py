#codigo 19 propagacion
from constraint import Problem

# List of regions
letras = ["A", "B", "C", "D"]

# List of available colors
colors = ["Rojo", "Verde", "Azul"]

# Create a new problem
problem = Problem()

# Add variables to the problem
for region in letras:
    problem.addVariable(region, colors)

# Define the propagation function
def propagar(region1, region2):
    # If the two regions are adjacent
    if region1 in ["A", "B"] and region2 in ["B", "C"]:
        # They cannot have the same color
        problem.addConstraint(lambda c1, c2: c1 != c2, [region1, region2])

# Add the propagation function to the problem
for region1 in letras:
    for region2 in letras:
        if region1 != region2 and propagar(region1, region2):
            problem.addConstraint(lambda c1, c2: c1 != c2, [region1, region2])

# Find all solutions
soluciones = problem.getSolutions()

# Print the solutions
for i, solucion in enumerate(soluciones):
    print(f"\nSolución {i+1}:")
    for region, color in solucion.items():
        print(f"  La leta {region} es de color {color}")