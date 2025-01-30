import os
import typer
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from dotenv import load_dotenv
from datetime import datetime

# Initialize typer app and rich console
app = typer.Typer()
console = Console()

# Load environment variables
load_dotenv()

def get_weather(city: str, units: str = "celsius") -> dict:
    """Fetch weather data from OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("OpenWeatherMap API key not found in .env file")

    unit_param = "metric" if units == "celsius" else "imperial"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit_param}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        console.print(f"[red]Error fetching weather data: {str(e)}[/red]")
        raise typer.Exit(1)

def display_weather(weather_data: dict, units: str):
    """Display weather information in a formatted table."""
    temp_unit = "°C" if units == "celsius" else "°F"
    speed_unit = "m/s" if units == "celsius" else "mph"

    # Create weather info table
    table = Table(show_header=False, border_style="blue")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="yellow")

    # Add weather information rows
    table.add_row("Temperature", f"{weather_data['main']['temp']}{temp_unit}")
    table.add_row("Feels Like", f"{weather_data['main']['feels_like']}{temp_unit}")
    table.add_row("Humidity", f"{weather_data['main']['humidity']}%")
    table.add_row("Wind Speed", f"{weather_data['wind']['speed']} {speed_unit}")
    table.add_row("Weather", weather_data['weather'][0]['description'].capitalize())

    # Create and display the panel with the table
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    panel = Panel(
        table,
        title=f"[bold green]Weather in {weather_data['name']}, {weather_data['sys']['country']}[/bold green]",
        subtitle=f"[italic]Last updated: {current_time}[/italic]"
    )
    
    console.print(panel)

@app.command()
def main(
    city: str = typer.Argument(..., help="City name to get weather information for"),
    units: str = typer.Option(
        "celsius",
        help="Temperature units (celsius/fahrenheit)",
        callback=lambda x: x.lower()
    )
):
    """
    Get current weather information for any city.
    """
    if units not in ["celsius", "fahrenheit"]:
        console.print("[red]Error: Units must be either 'celsius' or 'fahrenheit'[/red]")
        raise typer.Exit(1)

    with console.status("[bold green]Fetching weather data..."):
        try:
            weather_data = get_weather(city, units)
            display_weather(weather_data, units)
        except Exception as e:
            console.print(f"[red]An error occurred: {str(e)}[/red]")
            raise typer.Exit(1)

if __name__ == "__main__":
    app.run()