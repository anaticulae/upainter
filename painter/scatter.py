# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import itertools

import matplotlib.figure

import painter
import painter.utils


def render(
    x,
    y,
    legend=None,
    marker=None,
    **kwargs,
) -> matplotlib.figure.Figure:
    """\
    #absolute: use values instead of percentage
    """
    if not x or not y:
        raise ValueError('require some data: x,y are empty')
    if len(x) != len(y):
        raise ValueError('x and y must be the same size')
    legend = legend if legend else []
    if legend and len(legend) != len(x):
        raise ValueError('legend must be the same size')
    fig, ax = painter.utils.configure(**kwargs)  # pylint:disable=C0103

    marker = marker if marker else painter.default_markers()
    legend = legend if legend else itertools.cycle([None])

    for xx, yy, cc, mm, ll in zip(x, y, painter.colors(), marker, legend):  # pylint:disable=C0103
        if ll and not isinstance(ll, str):
            cc, ll = ll  # pylint:disable=C0103
        if ll:
            ax.scatter(xx, yy, c=cc, marker=mm, label=ll)
        else:
            ax.scatter(xx, yy, c=cc, marker=mm)
    # check that iter is not None-Iter
    if isinstance(legend, list):
        ax.legend()
    return fig
