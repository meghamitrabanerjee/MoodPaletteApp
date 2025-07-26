# 🎨 MoodPaletteApp

> An AI-powered mood-based color palette generator for creatives and developers.

---

## 🌈 Overview

**MoodPaletteApp** is a beginner-friendly, ML-powered web app that generates beautiful color palettes based on selected moods or themes. Whether you're designing a website, an illustration, or just looking for inspiration — this app helps you discover color combinations that fit your vibe.

Built using **Python, K-Means clustering**, and **Streamlit**, the app offers 20 predefined moods like "Calm", "Energetic", "Vintage", etc., each with 5–6 curated color palettes.

---

## ✨ Features

* 🎨 Select from 20 moods/themes
* 🎯 See 5–6 curated palettes per mood
* 📊 ML-based palette generation using K-Means
* 📷 Download palette as PNG
* ⚡ Fast, minimal Streamlit UI
* 📚 Clean, structured code for easy learning and extension

---

## 📁 Folder Structure

```
MoodPaletteApp/
│
├── app.py                                                      # Streamlit UI code
├── palette_generator.py                                        # ML (K-Means) palette logic
├── color_scraper.py                                            # Web scraping hex codes
├── color_palette_visualiser.py                                 # Color palette image generation
├── mood_palettes.csv                                           # Predefined mood palettes
├── mood_descriptions.csv                                       # Descriptive info per mood
├── visualise_palettes.py                                       # Optional visualizations
├── requirements.txt                                            # Python dependencies
└── README.md                                                   # This file
```

---

## 🧪 How to Run

### 🔧 Setup

1. Clone the repo

   ```bash
   git clone https://github.com/meghamitrabanerjee/MoodPaletteApp.git
   cd MoodPaletteApp
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app

   ```bash
   streamlit run app.py
   ```

---

## 📸 App Preview

> *Screenshot of the app interface.*


```
<img width="1920" height="1008" alt="moodpaletteapp" src="https://github.com/user-attachments/assets/bef6dac6-637b-4304-88df-f302ee90ea7b" />

```

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit** – UI framework
* **scikit-learn** – ML clustering
* **matplotlib / Pillow** – Image generation
* **BeautifulSoup** – Web scraping

---

## 🚀 Upcoming Features

* 💡 Upload an image and generate matching palettes
* 🔍 Mood search & filtering
* 💾 Save/download custom palettes
* 🌐 Deploy to Streamlit Cloud

---

## 👩‍💻 Made by

**Meghamitra Banerjee**
💼 [GitHub](https://github.com/meghamitrabanerjee)

---
