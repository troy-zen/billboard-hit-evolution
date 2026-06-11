# Billboard Hit Evolution: Audio Archetypes and Changing Chart Dynamics (2005–2025)

## Overview

This project investigates how successful Billboard Hot 100 songs have changed over time by combining chart performance data, Apple Music metadata, computational audio features, and unsupervised machine learning.

Using over 4,000 Billboard Top-40 songs from 2005–2025, a multi-stage pipeline was developed to:

1. Processes weekly Billboard chart data into song-level lifecycle records.
2. Matches songs to Apple Music metadata and preview clips.
3. Extracts computational audio features using Essentia machine learning models.
4. Applies PCA and clustering to identify interpretable audio archetypes.
5. Examines how the composition of successful songs has evolved across different eras of music consumption.

---

## Research Question

How have the audio characteristics and chart dynamics of successful Billboard songs changed over time, particularly during the transition from the streaming era to the TikTok era?

---

## Key Findings

### Billboard Chart Dynamics

Analysis of Billboard lifecycle metrics revealed several long-term trends:

* Songs reach peak popularity more quickly than they did in the mid-2000s.
* Chart turnover has increased substantially over time.
* Song lifespans on the Billboard Hot 100 have generally declined.
* Successful songs experience shorter and faster chart cycles than in previous eras.

### Principal Components Analysis (PCA)

PCA revealed two major dimensions of variation among Billboard hits:

**PC1 — Brightness and Emotional Energy**

* Strongly associated with spectral brightness, valence, and arousal.
* Separates brighter, more energetic songs from darker and less emotionally intense recordings.

**PC2 — Rhythmic Intensity and Production Momentum**

* Driven primarily by loudness and tempo.
* Captures differences in production intensity, rhythmic drive, and dance-oriented characteristics.

### Audio Archetypes

K-means clustering identified three interpretable audio archetypes:

#### Energetic Crossover Hits

Commercially oriented songs blending pop, dance, electronic, and contemporary hip-hop influences. Characterized by high energy, bright production, and broad mainstream appeal.

#### Hip-Hop Dominant

Rhythm-driven songs centered on hip-hop and rap influences. Distinguished by strong beat-oriented production and genre-specific stylistic characteristics.

#### Mellow / Alternative

Songs emphasizing melody, atmosphere, and traditional instrumentation. Includes stronger representation from alternative, rock, folk, and singer-songwriter styles.

### Evolution of Successful Songs

The relative prevalence of these archetypes changed substantially across eras, suggesting that changes in chart behavior are accompanied by shifts in the types of songs achieving commercial success.

---

## Project Pipeline

```text
Billboard Hot 100 Weekly Data
            │
            ▼
Song Lifecycle Engineering
            │
            ▼
Top-40 Song Selection
            │
            ▼
Apple Music Metadata Matching
            │
            ▼
Preview Clip Collection
            │
            ▼
Essentia Audio Feature Extraction
            │
            ▼
Feature Engineering & Validation
            │
            ▼
PCA
            │
            ▼
K-Means Clustering
            │
            ▼
Audio Archetype Analysis
```

---

## Repository Structure

```text
notebooks/
├── 001_billboard_lifecycle_engineering.ipynb
├── 002_apple_music_matching.ipynb
├── 003_audio_feature_extraction.ipynb
└── 004_clustering.ipynb

data/
├── raw/
├── intermediate/
├── final/
└── review/

figures/
poster/
essentia_models/
```

---

## Data Sources

### Billboard Hot 100

Kaggle Dataset:

https://www.kaggle.com/datasets/ludmin/billboard/data?select=hot100.csv

### Apple Music / iTunes Search API

Used for song metadata retrieval and preview clip acquisition.

---

## Computational Audio Features

Audio features were extracted using Essentia machine learning models and included:

* Tempo
* Loudness (RMS)
* Spectral Centroid
* Spectral Rolloff
* Valence
* Arousal
* Mode
* Genre-family predictions

Danceability was evaluated but excluded from the final analysis due to poor reliability on preview-length clips.

---

## Methods

### Feature Engineering

Song-level lifecycle metrics were engineered from weekly Billboard chart records, including:

* Lifespan
* Peak rank
* Time-to-peak
* Top-10 persistence
* Top-40 persistence

### Dimensionality Reduction

Principal Components Analysis (PCA) was used to summarize major dimensions of variation among songs.

### Clustering

K-means clustering was applied to standardized audio features to identify recurring audio archetypes.

---

## Poster

The final project poster is available in:

```text
poster/
```

---

## Reproducibility

The project is organized as a sequential pipeline:

```text
001 → 002 → 003 → 004
```

Running the notebooks in order reproduces the complete workflow from raw Billboard data through final clustering and visualization.
