# Weather Fetcher

Weather Fetcher is a simple Python script that fetches the current weather information for a given city using the OpenWeatherMap API.

## Features

- Fetches current temperature and weather description for any city.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/weather-fetcher.git
    ```

2. Navigate to the project directory:

    ```sh
    cd weather-fetcher
    ```

3. Install the required library:

    ```sh
    pip install requests
    ```

## Usage

1. Get your OpenWeatherMap API key from [OpenWeatherMap](https://openweathermap.org/).

2. Open the `weather_fetcher.py` file and replace `'your_api_key_here'` with your actual API key.

3. Run the script:

    ```sh
    python weather_fetcher.py
    ```

4. Enter the city name when prompted.

    ```sh
    Enter city name: London
    ```

5. The script will output the current temperature and weather description for the specified city.

## Example

```sh
Enter city name: London
City: London
Temperature: 15°C
Weather: light rain
