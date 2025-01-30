# weather-dashboard-cli
A CLI tool for fetching weather information

# Weather Dashboard CLI

A command-line interface (CLI) tool that fetches and displays weather information for any city using the OpenWeatherMap API.

## Features

- Get current weather conditions for any city
- Display temperature in Celsius or Fahrenheit
- Show humidity, wind speed, and weather description
- Beautiful command-line formatting with rich text and colors
- Easy-to-use CLI interface

## Installation

1. Clone this repository:-
```bash
git clone https://github.com/yourusername/weather-dashboard-cli.git
cd weather-dashboard-cli
```
2. Create a virtual environment and activate it:-
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install the required packages:-
```bash
pip install -r requirements.txt
```
4. Get an API key from OpenWeatherMap and add it to .env file:-
```bash
OPENWEATHER_API_KEY=your_api_key_here
```
5. Usage:-
```bash
python weather_dashboard.py --city "London" --units celsius
python weather_dashboard.py --city "New York" --units fahrenheit
```
## Requirements

- Python 3.8+
- See requirements.txt for package dependencies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
