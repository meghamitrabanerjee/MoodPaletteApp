import pandas as pd
import random
from sklearn.cluster import KMeans

# Load the dataset of colors
df = pd.read_csv("data/color_palettes.csv")  # Ensure you have this CSV file
print(f"Total colors loaded from CSV: {len(df)}")  # Debugging line


# Define a mood-based filtering logic
MOOD_FILTERS = {
    "Happy": lambda color: color.mean() > 150,  # Bright & Warm Colors
    "Calm": lambda color: color.mean() > 120 and color.mean() < 200,  # Soft Pastels
    "Romantic": lambda color: color[0] > 180 and color[1] < 150,  # Reddish Pinks
    "Mysterious": lambda color: color.mean() < 80,  # Dark Colors
    "Vintage": lambda color: 100 < color.mean() < 180,  # Muted Old-School Shades
    "Nature": lambda color: color[1] > 100 and color[0] < 120,  # Greens & Browns
    "Dreamy": lambda color: color[2] > 150 and color.mean() > 130,  # Soft Blues
    "Elegant": lambda color: color.mean() > 160 and color.mean() < 220,  # Soft Neutrals
    "Fresh": lambda color: color[1] > 130 and color.mean() > 120,  # Greens & Light Blues
    "Festive": lambda color: color[0] > 120 and color[1] > 100,  # Reds, Golds, Greens
    "Minimalist": lambda color: color.mean() > 180,  # Neutral & Whites
    "Sunset": lambda color: color[0] > 150 and color[2] < 100,  # Reds & Oranges
    "Ocean": lambda color: color[2] > 150 and color[0] < 100,  # Deep Blues & Teals
    "Space": lambda color: color.mean() < 60,  # Deep Dark Shades
    "Retro": lambda color: 80 < color.mean() < 160,  # Muted 80s Tones
    "Pastel": lambda color: color.mean() > 160 and color.mean() < 230,  # Soft Pastels
    "Cinematic": lambda color: color.mean() > 90 and color.mean() < 180,  # Warm Neutrals
    "Neon": lambda color: color.max() > 220,  # Super Bright Colors
    "Dark": lambda color: color.mean() < 50,  # Really Dark Colors
    "Soft": lambda color: color.mean() > 140 and color.mean() < 200,  # Warm, Gentle Hues
}

def generate_palette(mood, n_colors=5):
    """Generate a color palette based on the selected mood."""
    
    # Convert HEX colors to RGB
    df["RGB"] = df["Hex Code"].apply(lambda x: tuple(int(x[i:i+2], 16) for i in (1, 3, 5)))

    df["R"] = df["RGB"].apply(lambda x: x[0])
    df["G"] = df["RGB"].apply(lambda x: x[1])
    df["B"] = df["RGB"].apply(lambda x: x[2])

    # Filter colors based on mood
    if mood in MOOD_FILTERS:
        mood_colors = df[df[["R", "G", "B"]].apply(MOOD_FILTERS[mood], axis=1)]
    else:
        mood_colors = df

    if mood_colors.empty:
        return ["#000000"] * n_colors  # Return black if no colors match

    # Convert to numpy array for clustering
    color_array = mood_colors[["R", "G", "B"]].to_numpy()

    # Apply K-Means Clustering
    kmeans = KMeans(n_clusters=n_colors, random_state=None, n_init=10)

    kmeans.fit(color_array)
    cluster_centers = kmeans.cluster_centers_.astype(int)

    # Convert clustered colors back to HEX
    palette = ["#%02x%02x%02x" % tuple(color) for color in cluster_centers]

    return palette
