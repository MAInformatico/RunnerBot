# RunnerBot

**RunnerBot** is a Telegram bot that analyzes weather data and recommends what sportswear to wear, based on temperature, humidity, and other conditions.

## Problem

Deciding what to wear for a run is harder than it seems. Temperature, humidity, wind, and rain all affect comfort and safety. Checking multiple apps and guessing is time-consuming.

## Solution

RunnerBot fetches real-time weather data from the OpenWeather API and uses simple logic to recommend clothing. It runs as a Telegram bot, so you can ask it directly from your phone.

## Technologies

- Python
- Telegram Bot API
- OpenWeather API
- Pandas (for processing weather data)

## How to run it

### Prerequisites

1. Get a free API token from [OpenWeather](https://openweathermap.org/api).
2. Create a `coordinates.txt` file with your location (or change the filename in `weather.py`).
3. Set up a Telegram bot and get its token.

### Run

```bash
pip install -r requirements.txt
python weather.py
```

You can also test it directly on Telegram: @MAInformaticoRunner_bot

## What I learned
- Building a Telegram bot with Python.
- Integrating a third-party API (OpenWeather).
- Processing and interpreting weather data with Pandas.

## Future work
- Add support for multiple locations.
- Add more clothing recommendations based on wind and rain.
- Deploy to a server so it runs 24/7.
