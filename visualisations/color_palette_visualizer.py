import pandas as pd
import matplotlib.pyplot as plt

# Load the extracted colors
df = pd.read_csv("data/color_palettes.csv")


# Convert Hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

df["RGB"] = df["Hex Code"].apply(hex_to_rgb)

# Plot Some Random Colors
plt.figure(figsize=(15, 5))
for i, color in enumerate(df.sample(50)["Hex Code"]):  # Random 50 colors
    plt.fill_between([i, i+1], 0, 1, color=color)
plt.xticks([])  # Hide x-axis
plt.yticks([])  # Hide y-axis
plt.title("Random Sample of Extracted Colors")
plt.show()
