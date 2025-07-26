import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import os

# Function to extract colors from a webpage
def extract_colors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    color_list = []

    # Extract colors using regex from inline styles
    for div in soup.find_all("div", style=re.compile("background-color:")):
        match = re.search(r'background-color:\s*([^;]+)', div["style"])
        if match:
            color = match.group(1).strip()
            if color.startswith("#") and len(color) in [4, 7]:
                color_list.append(color)

    return color_list

# Base URL of the website
base_url = "https://color-hex.com/color-palettes/?page="

# Extract colors from multiple pages
all_colors = []
for page in range(1, 15):
    print(f"Scraping page {page}...")
    url = base_url + str(page)
    colors = extract_colors(url)
    all_colors.extend(colors)
    time.sleep(2)

# Remove duplicates
all_colors = list(set(all_colors))

# Save to CSV in data/
df = pd.DataFrame(all_colors, columns=["Hex Code"])
os.makedirs("data", exist_ok=True)
df.to_csv("data/color_palettes.csv", index=False)

print(f"✅ Extracted {len(all_colors)} unique colors and saved to 'data/color_palettes.csv'.")
