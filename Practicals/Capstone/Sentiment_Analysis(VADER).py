import tkinter as tk
from tkinter import ttk, messagebox
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Adjust these thresholds if you'd like more lenient or strict classification
POS_THRESHOLD = 0.05   # Default is 0.05
NEG_THRESHOLD = -0.05  # Default is -0.05

def analyze_sentiment():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter a sentence for analysis.")
        return

    analyzer = SentimentIntensityAnalyzer()
    
    # Example of modifying lexicon (optional):
    # If you want to reduce how negative "exhausted" is:
    # analyzer.lexicon['exhausted'] = -0.3

    score = analyzer.polarity_scores(text)

    compound = score['compound']
    if compound >= POS_THRESHOLD:
        sentiment = "Positive"
        color = "green"
    elif compound <= NEG_THRESHOLD:
        sentiment = "Negative"
        color = "red"
    else:
        sentiment = "Neutral"
        color = "blue"

    result_label.config(text=f"Sentiment: {sentiment}", foreground=color)

# ------------------ GUI SETUP ------------------ #
root = tk.Tk()
root.title("VADER Sentiment Analysis")
root.geometry("500x350")
root.configure(bg="#FAFAFA")

# Use ttk.Style to customize widget appearances
style = ttk.Style()
style.theme_use("clam")  # You can try different themes like "default", "alt", etc.
style.configure("TFrame", background="#FAFAFA")
style.configure("TLabel", background="#FAFAFA", foreground="#333333", font=("Arial", 12))
style.configure("Header.TLabel", font=("Arial", 16, "bold"), foreground="#444444")
style.configure("TButton",
                background="#4CAF50",
                foreground="white",
                font=("Arial", 12, "bold"),
                padding=6)

# Header Label
header_label = ttk.Label(root, text="Sentiment Analysis (VADER)", style="Header.TLabel")
header_label.pack(pady=10)

# Main Frame
main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input Label
input_label = ttk.Label(main_frame, text="Enter your sentence below:")
input_label.pack(anchor=tk.W, pady=5)

# Text Entry
text_entry = tk.Text(main_frame, height=5, width=50, font=("Arial", 12))
text_entry.pack(pady=5)

# Analyze Button
analyze_button = ttk.Button(main_frame, text="Analyze", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Result Label
result_label = ttk.Label(main_frame, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
