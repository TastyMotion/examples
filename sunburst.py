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

    clip.scissor_begin(0, 0, width, height)
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
    clip.scissor_end()

    clip.tween(Linear(phi, 0, 360, duration))

    return clip


def MyClip():
    clip = Clip2D("main", 1200, 900)

    sunburst = Sunburst2D(
        clip_size=(1200, 900),
        colors=["#90EE90", "#FFB2EF", "#87CEEB"],
        contour_color="black",
        contour_width=2,
        duration=7,
        radius=900,
        repeat=5,
    )

    clip.add(sunburst)
    clip.tween(sunburst.tween())

    return clip


if __name__ == "__main__":
    preview(__file__)
