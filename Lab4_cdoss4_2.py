"""
Program : Lab4_cdoss4-2, Plotting Cubic numbers
Author: Christian Doss
Purpose: Generates two png files plotting the first 5 cubic and the first 5,000 cubic numbers
Date: 2026-11-21
"""


import matplotlib.pyplot as plt


def five_cubes():
    x_values = [1, 2, 3, 4 ,5]
    y_values = [1, 8, 27, 64, 125]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, linewidth = 3, marker = "o")

    ax.set_title("First 5 Cubes", fontsize = 14)
    ax.set_xlabel("Value", fontsize = 12)
    ax.set_ylabel("Cube of Value", fontsize = 12)

    plt.savefig("first_5_cubes.png")
    plt.close(fig)

def main():
    five_cubes()

if __name__ == "__main__":
    main()