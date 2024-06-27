# Word Correction App

## Description

This Python application utilizes the Levenshtein distance algorithm to correct misspelled words. It is built with Streamlit, making it easy to deploy as a web app. Users can input a word, and the app will suggest the closest correct word from a predefined vocabulary list.

## Installation

To run this application, you need Python and Streamlit installed on your system. Follow these steps:

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd <project-directory>

# Install the required packages
pip install -r requirements.txt

```

Usage
To start the application, run the following command in your terminal:

```bash
streamlit run levenshtein_distance.py
```

Navigate to the provided URL to access the web interface. Enter a word you wish to correct, and press the "Correct the word" button to see the suggested corrections.

Features
Word correction using the Levenshtein distance algorithm.
Display of the top 10 closest words from the vocabulary list.
Simple and user-friendly web interface.
