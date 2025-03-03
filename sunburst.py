#   This file is part of TastyMotion project.
#
#   Homepage:   https://tastymotion.com
#   GitHub:     https://github.com/TastyMotion/examples
#
#   Copyright (c) 2025 <dev727@tastymotion.com>.


import math

from tastymotion import Clip2D, Knob, Linear, preview


def Sunburst2D(
    clip_size=(1280, 720),
    colors=["pink", "green", "blue"],
    contour_color="black",
    contour_width=2,
    duration=5,
    radius=200,
    repeat=3,
):
    """Create Sunburst animation.

    Parameters
    ----------
    clip_size: tuple of int, default=(1280, 720)
        Width and height of the final clip.
    colors: list of str, default=['pink', 'green', 'blue']
        Colors of the sunburst legs.
    contour_color: str, default='black'
        Color of the sunburst contour.
    contour_width: int, default=2
        Width of the sunburst contour (use 0 to have no contour).
    duration: float, default=5
        Duration of the final clip in seconds.
    radius: float, default=200
        Radius of the sunburst drawing.
    repeat: int, default=3
        Number of the repeating legs.

    Returns
    -------
    Clip2D
        Sunburst animation.
    """

    width, height = clip_size
    clip = Clip2D("sunburst", width, height)
    phi = Knob("phi")

    clip.translate(width / 2, height / 2)
    clip.rotate(phi)

    n = repeat * len(colors)
    cos_ = math.cos(math.pi / n)
    sin_ = math.sin(math.pi / n)
    for color in repeat * colors:
        clip.fill_color(color)
        clip.fill_triangle(
            0, 0, radius * cos_, radius * sin_, radius * cos_, -radius * sin_
        )
        if contour_width > 0:
            clip.line_width(contour_width)
            clip.fill_color(contour_color)
            clip.move_to(0, 0)
            clip.line_to(radius * cos_, radius * sin_)
            clip.line_to(radius * cos_, -radius * sin_)
            clip.line_to(0, 0)
        clip.rotate(360.0 / n)

    clip.tween(Linear(phi, 0, 360, duration))

    return clip


def Main2D():
    # w, h = 3840, 2160  # 2160p / 4K
    # w, h = 3200, 1800  # 1800p

    w, h = 1600, 900  # 900p

    # w, h = 1280, 720 # 720p
    # w, h = 1920, 1080  # 1080p / 2K
    # w, h = 2560, 1440  # 1440p
    clip = Clip2D("main", w, h)

    sunburst_2d = Sunburst2D(
        clip_size=(w, h),
        colors=["#90EE90", "#FFB2EF", "#87CEEB"],
        contour_color="black",
        contour_width=4,
        duration=5,
        radius=400,
        repeat=5,
    )

    clip.add(sunburst_2d)
    clip.tween(sunburst_2d.tween())

    return clip


if __name__ == "__main__":
    preview(__file__)
