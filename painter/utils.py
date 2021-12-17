# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import io
import itertools

import matplotlib.pyplot
import matplotlib.ticker
import PIL.Image

import painter


def configure(**kwargs):  # pylint:disable=R1260
    width = kwargs.get('width', 5.12)  # 512 pixel
    height = kwargs.get('height', 5.12)  # 512 pixel
    xlabel = kwargs.get('xlabel', None)
    ylabel = kwargs.get('ylabel', None)
    title = kwargs.get('title', None)
    grid = kwargs.get('grid', False)
    title_fontsize = kwargs.get('title_fontsize', 30)
    label_fontsize = kwargs.get('label_fontsize', 20)
    xlim = kwargs.get('xlim', None)
    ylim = kwargs.get('ylim', None)
    intlabel = kwargs.get('intlabel', None)
    if 'intlabel' in kwargs:
        del kwargs['intlabel']
    fig, ax = matplotlib.pyplot.subplots(figsize=(width, height))  # pylint:disable=C0103
    if xlabel:
        matplotlib.pyplot.xlabel(xlabel, fontsize=label_fontsize)
    if ylabel:
        matplotlib.pyplot.ylabel(ylabel, fontsize=label_fontsize)
    if title:
        matplotlib.pyplot.title(title, fontsize=title_fontsize)
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    if intlabel:
        if isinstance(intlabel, bool):
            intlabel = True, True
        if intlabel[0]:
            ax.xaxis.set_major_formatter(IntFormatter())
        if intlabel[1]:
            ax.yaxis.set_major_formatter(IntFormatter())
    ax.grid(grid)
    return fig, ax


class IntFormatter(matplotlib.ticker.FuncFormatter):
    """Round every label element."""

    def __init__(self):
        super().__init__(func=IntFormatter.equal)

    @staticmethod
    def equal(item, _):  # pylint:disable=W0613
        return '%d' % item if int(item) == item else ''


# ``'b'``          blue
# ``'g'``          green
# ``'r'``          red
# ``'c'``          cyan
# ``'m'``          magenta
# ``'y'``          yellow
# ``'k'``          black
# ``'w'``          white

COLOR = [
    'b',
    'g',
    'r',
    'c',
    'm',
    'y',
    'k',
]

# ``'-'``          solid line style
# ``'--'``         dashed line style
# ``'-.'``         dash-dot line style
# ``':'``          dotted line style

STYLE = [
    '-',
    '--',
    '-.',
    ':',
]


def linestyle():
    for color in COLOR:
        for style in STYLE:
            yield f'{color}{style}'


def colors():
    return itertools.cycle(COLOR)


MARKERS = 'ov<>1234s'


def markers():
    return itertools.cycle(MARKERS)


def default_markers():
    return itertools.cycle('o')


def image_frombytes(png):
    assert isinstance(png, bytes), type(png)
    return PIL.Image.open(io.BytesIO(png))


def figure_toimage(figure):
    png = painter.png(figure)
    result = image_frombytes(png)
    return result


def entropy(image):
    return image.entropy()


def entropy_diff(image) -> float:
    grayscaled = painter.gray(image)
    before = entropy(image)
    after = entropy(grayscaled)
    diff = before - after
    return diff
