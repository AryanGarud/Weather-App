import requests
import sqlite3
import logging
import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
from PIL import Image, ImageTk

# API Key (Replace with your actual API key)
API_KEY = "089e9061eb568e0a637bae49d7679e90"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Configure Logging
logging.basicConfig(filename="weather_app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect("weather_history.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city TEXT,
                        temperature REAL,
                        humidity INTEGER,
                        wind_speed REAL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Fetch weather data from API
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code != 200:
            error_message = data.get('message', 'Unknown error')
            logging.error(f"API request failed: {error_message}")
            messagebox.showerror("Error", f"Failed to fetch data: {error_message}")
            return None
        
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        
        save_to_db(weather_info)
        logging.info(f"Weather data fetched successfully for {city}")
        return weather_info
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        messagebox.showerror("Error", "Failed to connect to API")
        return None

# Save weather data to SQLite database
def save_to_db(weather_info):
    conn = sqlite3.connect("weather_history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (city, temperature, humidity, wind_speed) VALUES (?, ?, ?, ?)",
                   (weather_info["city"], weather_info["temperature"], weather_info["humidity"], weather_info["wind_speed"]))
    conn.commit()
    conn.close()

# Retrieve and display past weather queries
def view_history():
    conn = sqlite3.connect("weather_history.db")
    df = pd.read_sql_query("SELECT * FROM history ORDER BY timestamp DESC LIMIT 10", conn)
    conn.close()
    
    history_window = tk.Toplevel()
    history_window.title("Weather History")
    history_window.geometry("500x300")
    history_window.configure(bg="#f0f8ff")
    
    text_area = scrolledtext.ScrolledText(history_window, wrap=tk.WORD, width=60, height=15, font=("Arial", 12), bg="#ffffff", fg="#333")
    text_area.pack(pady=10)
    
    if df.empty:
        text_area.insert(tk.END, "No past weather data found.")
    else:
        text_area.insert(tk.END, df.to_string(index=False))
    text_area.config(state=tk.DISABLED)

# Fetch weather and display in GUI
def fetch_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    weather_info = get_weather(city)
    if weather_info:
        result_label.config(text=f"\n🌡 Temperature: {weather_info['temperature']}°C\n💨 Wind Speed: {weather_info['wind_speed']} m/s\n💧 Humidity: {weather_info['humidity']}%\n", font=("Arial", 14))
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data")

# GUI Application
def create_gui():
    global city_entry, result_label
    root = tk.Tk()
    root.title("Weather Application")
    root.geometry("400x450")
    root.configure(bg="#e3f2fd")
    
    ttk.Label(root, text="🌤 Weather App", font=("Arial", 18, "bold"), background="#e3f2fd").pack(pady=10)
    
    tk.Label(root, text="Enter City:", font=("Arial", 14), bg="#e3f2fd").pack(pady=5)
    city_entry = ttk.Entry(root, font=("Arial", 12), width=30)
    city_entry.pack(pady=5)
    
    btn_get = ttk.Button(root, text="🔍 Get Weather", command=fetch_weather)
    btn_get.pack(pady=5)
    
    btn_history = ttk.Button(root, text="📜 View History", command=view_history)
    btn_history.pack(pady=5)
    
    result_label = ttk.Label(root, text="", font=("Arial", 12), background="#e3f2fd", justify=tk.LEFT)
    result_label.pack(pady=10)
    
    root.mainloop()

# Run application
if __name__ == "__main__":
    init_db()
    create_gui()
