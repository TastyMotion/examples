import math

from   tastymotion import Clip2D, Knob, Linear, preview


def sunburst_clip(
        clip_size=(1280, 720),
        colors=['pink', 'green', 'blue'],
        contour_color='white',
        contour_width=2,
        duration=5,
        radius=900,
        repeat=2,
):
    # Initialize animation clip
    width, height = clip_size
    clip = Clip2D("sunburst", width, height)
    phi  = Knob('phi')

    clip.translate(width/2, height/2)
    clip.rotate(phi)
    n = repeat * len(colors)
    cos_ = math.cos(math.pi / n)
    sin_ = math.sin(math.pi / n)
    for color in repeat * colors:
        clip.fill_color(color)
        clip.fill_triangle(0, 0, radius * cos_, radius * sin_, radius * cos_, -radius * sin_)
        if contour_width > 0:
            clip.line_width(contour_width)
            clip.fill_color(contour_color)
            clip.move_to(0, 0)
            clip.line_to(radius * cos_, radius * sin_)
            clip.line_to(radius * cos_, -radius * sin_)
            clip.line_to(0, 0)
        clip.rotate(360. / n)

    clip.tween(
        Linear(phi, 0, 360, duration)
    )

    return clip


def MyClip():
    return sunburst_clip(
        contour_color='black',
        contour_width=2,
        duration=4,
        radius=200,
        repeat=5,
    )


if __name__ == '__main__':
    preview(__file__)
