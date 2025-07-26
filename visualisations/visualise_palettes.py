
import matplotlib.pyplot as plt
import random
import pandas as pd
df = pd.read_csv("data/color_palettes.csv")
colors = df["Hex Code"].tolist()

# Debug: Check extracted colors
print(f"Total colors extracted: {len(colors)}")
print(f"First 10 colors: {colors[:10]}")

# Shuffle colors
random.shuffle(colors)

# Ensure we have colors to plot
if not colors:
    print("Error: No colors extracted. Check JSON structure!")
    exit()

# Set figure size
plt.figure(figsize=(12, 8))

# Create horizontal bars with thicker width
bar_height = 0.8  # Makes bars more visible
for i, color in enumerate(colors[:100]):  # Display only first 100 colors
    plt.barh(i, width=10, color=color, height=bar_height)  # Add height parameter

# Remove axes
plt.xticks([])
plt.yticks([])
plt.gca().invert_yaxis()  # Ensure first palette appears at the top
plt.title("Extracted Color Palettes", fontsize=14, fontweight="bold")

# Show and save image

plt.savefig("visualisations/palettes.png", dpi=300, bbox_inches="tight")
print("Palette image saved successfully as palettes.png!")

plt.show()
