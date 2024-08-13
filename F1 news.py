import requests
import tkinter as tk
from tkinter import messagebox

# PERSONAL API key for NewsAPI (PLEASE DONT USE THIS KEY FOR YOUR OWN PROJECTS)
API_KEY = "2fcff62f7450495c9bb8056bc42203c0"

NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_f1_news():
    
    query_parameters = {
        "q": "Formula 1 OR F1", #This searches for the keyword of f1 oor Formular 1
        "apiKey": API_KEY,
        "language": "en",
        "sortBy": "publishedAt"  # This code here sorts it by the time it was published so we get the latest news
    }
    
    response = requests.get(NEWS_API_URL, params=query_parameters)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        messagebox.showerror("Error", f"Failed to fetch news: {response.status_code}")
        return []

