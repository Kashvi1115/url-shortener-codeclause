# pip install pyshorteners
# pip install pyperclip
# pip install ttkthemes
import pyshorteners
import pyperclip
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def shorten_url():
    url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)

    # Copy the shortened URL to the clipboard
    pyperclip.copy(shortened_url)

    result_label.config(text=f'Shortened URL: {shortened_url}\n(Copied to clipboard)')

# Create the main window
window = tk.Tk()
window.title('URL Shortener')
window.geometry('400x200')

# Apply a themed style for a modern look
style = ThemedStyle(window)
style.set_theme("plastik")

# Create and place styled widgets in the window
label = ttk.Label(window, text='Enter the URL:', font=('Arial', 12))
label.pack(pady=10)

entry = ttk.Entry(window, font=('Arial', 12))
entry.pack(pady=10)

button = ttk.Button(window, text='Shorten URL', command=shorten_url)
button.pack(pady=10)

result_label = ttk.Label(window, text='', font=('Arial', 12))
result_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
