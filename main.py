import pyautogui
import time
import argparse

class ScreenKeeper:
    """
    A class to keep the screen alive by typing out a specified string repeatedly.

    Parameters
    ----------
    text : str
        The text to be typed repeatedly.
    delay : float
        The delay in seconds between each typing action.
    """

    def __init__(self, text: str, delay: float):
        self.text = text
        self.delay = delay

    def start_typing(self):
        """
        Start typing the specified text repeatedly with the given delay.
        """
        try:
            while True:
                pyautogui.typewrite(self.text)
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("Stopped by user")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keep the screen alive by typing out a specified string repeatedly.")
    parser.add_argument('--text', type=str, default="apple juice", help='The text to be typed repeatedly.')
    parser.add_argument('--delay', type=float, default=10.0, help='The delay in seconds between each typing action.')

    args = parser.parse_args()

    screen_keeper = ScreenKeeper(text=args.text, delay=args.delay)
    screen_keeper.start_typing()
