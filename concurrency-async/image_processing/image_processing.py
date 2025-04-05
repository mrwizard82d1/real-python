"""
Image processing main module.
"""

import argparse
import pathlib
import tkinter as tk

import numpy as np
import PIL.Image


class AppWindow(tk.Tk):
    def __init__(self, image: PIL.Image.Image) -> None:
        super().__init__()

        # Main window
        self.title('Exposure and Gamma Correction')
        self.resizable(False, False)

        # Image pixels
        self.pixels = np.array(image)

        self.mainloop()

    def on_slide(self, *args, **kwargs):
        pass

    def show_preview(self, *args, **kwargs):
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=pathlib.Path)
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    with PIL.Image.open(args.image_path) as image:
        AppWindow(image)


if __name__ == '__main__':
    main(parse_args())
