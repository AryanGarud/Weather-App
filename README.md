# Weather Application

## Overview

This Python-based Weather Application fetches real-time weather data from the OpenWeatherMap API. Users can input a city name to retrieve details such as temperature, humidity, and wind speed. The application features a graphical user interface (GUI) built with Tkinter and stores past weather queries in an SQLite database.

## Features

- **🌍 Real-Time Weather Data**: Get live weather updates for any city.
- **🖥️ User-Friendly GUI**: Built with Tkinter for easy interaction.
- **💾 Search History**: Saves past searches in an SQLite database.
- **📜 View Past Queries**: Fetch and display historical weather data.
- **📊 Logging & Error Handling**: Logs user actions and handles API errors gracefully.
- **📑 Generate Reports**: Uses Pandas for structured history reporting.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: GUI framework for user interaction.
- **Requests**: Fetches data from OpenWeatherMap API.
- **SQLite3**: Stores search history.
- **Pandas**: For fetching and displaying historical reports.
- **Logging**: Tracks errors and system activities.

## Installation

### Prerequisites

Ensure you have Python installed on your system. Install dependencies using:

```sh
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository:
   ```sh
   git clone https://github.com/AryanGarud/Weather-App.git
   cd Weather-App
   ```
2. Run the script:
   ```sh
   python weather_app.py
   ```

## Usage

1. Enter a city name.
2. Click **Get Weather** to retrieve data.
3. Click **View History** to check past queries.

## API Key Setup

Ensure you have an OpenWeatherMap API key and replace the `API_KEY` in the script:

```python
API_KEY = "your_api_key_here"
```

## Repository Structure

```
Weather-App/
│── weather_app.py      # Main application script
│── weather_history.db  # SQLite database (auto-generated)
│── weather_app.log     # Log file (auto-generated)
│── README.md           # Documentation
```

## Contributing

Feel free to fork the repository, create a new feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

---

Enjoy exploring the weather from anywhere in the world with this simple yet powerful application! 🌦️☀️🌍

