import pandas as pd
import os

# Load the color CSV
df = pd.read_csv("data/color_palettes.csv")

# Remove duplicates
df = df.drop_duplicates(subset=["Hex Code"])

# Reset index
df = df.reset_index(drop=True)

# Group into palettes of 5
df["Palette ID"] = df.index // 5 + 1

# Save back to CSV (overwriting)
df.to_csv("data/color_palettes.csv", index=False)

print(f"✅ Cleaned and grouped {len(df)} colors into {df['Palette ID'].nunique()} palettes.")
