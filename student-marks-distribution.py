import numpy as np
import matplotlib.pyplot as plt

marks = np.array([
    45, 50, 55, 60, 65,
    70, 75, 80, 85, 90,
    95, 88, 76, 69, 58,
    47, 82, 91, 73, 66
])

plt.figure(figsize=(8,5), dpi=100)

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black",
    linewidth=2,
    alpha=0.8,
    label="Marks"
)

plt.title("Student Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.grid(True)

plt.legend()

plt.show()