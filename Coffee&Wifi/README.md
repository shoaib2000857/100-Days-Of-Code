# Coffee & Wifi

A Flask web application to add and view cafes with their details such as location, opening and closing times, coffee rating, wifi rating, and power outlet rating.

## Features

- Add new cafes with details
- View a list of all cafes
- Ratings for coffee, wifi, and power outlets

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/coffee-wifi.git
    cd coffee-wifi
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

1. Navigate to `http://127.0.0.1:5000/` in your web browser.
2. Use the "/Add" route to access the hidden form to add new cafes.
3. View the list of cafes by navigating to `http://127.0.0.1:5000/cafes`.

## Project Structure
