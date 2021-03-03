# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import itertools

import matplotlib.pyplot as plt


def configure(**kwargs):
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

    fig, ax = plt.subplots(figsize=(width, height))  # pylint:disable=C0103
    if xlabel:
        plt.xlabel(xlabel, fontsize=label_fontsize)
    if ylabel:
        plt.ylabel(ylabel, fontsize=label_fontsize)
    if title:
        plt.title(title, fontsize=title_fontsize)
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
    ax.grid(grid)
    return fig, ax


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
