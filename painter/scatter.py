# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import matplotlib.figure
import matplotlib.pyplot as plt

import painter.utils


def render(
        x,
        y,
        legend=None,
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
    fig, _ = painter.utils.configure(**kwargs)  # pylint:disable=C0103

    color = []
    if legend:
        if len(legend[0]) == 2:
            color = [item[0] for item in legend]
        else:
            color = [idx for idx, _ in enumerate(legend)]

    scatter = plt.scatter(x, y, c=color)

    data = [item if isinstance(item, str) else item[1] for item in legend]
    legend = (scatter.legend_elements()[0], data)
    plt.legend(*legend)
    return fig
