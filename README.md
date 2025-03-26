# Stay Awake

A Python script to keep your macOS screen awake by simulating keyboard activity. The script types out a specified string repeatedly with a customizable delay.

## Features

- Simulates keyboard activity to prevent the screen from sleeping.
- Customizable text and delay between typing actions.
- Easy to use and configure via command-line arguments.

## Requirements

- Python 3.10 or higher
- `pyautogui` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/stay-awake.git
    cd stay-awake
    ```

2. Install dependencies using Poetry:

    ```sh
    uv venv
    source .venv/bin/activate

    uv sync
    ```

## Usage

Run the script with the default text and delay:
```
python main.py
```