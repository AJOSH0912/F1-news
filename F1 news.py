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

def display_news(): # This function displays the news
    
    articles = fetch_f1_news() # Fetches the news
    
    if not articles: # This is for if there are no articles
        return
    
    for article in articles: # This is for if there are articles
        headline = article.get("title", "No Title") # This gets the title of the article
        description = article.get("description", "No Description") # This gets the description of the article
        url = article.get("url", "#") # This gets the url of the article
        
        headline_label = tk.Label(root, text=headline, font=("Helvetica", 14, "bold"), fg="blue", cursor="hand2") 
        headline_label.pack(anchor="w")
        description_label = tk.Label(root, text=description, font=("Helvetica", 12))
        description_label.pack(anchor="w", pady=(0, 10))
        
        headline_label.bind("<Button-1>", lambda e, url=url: open_article(url))

def open_article(url):
    
    import webbrowser
    webbrowser.open(url)

# Sets up the GUI window
root = tk.Tk()
root.title("F1 News")

# Runs display_news function to show the news   
display_news()

# Runs the loop
root.mainloop()