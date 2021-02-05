# pylint:disable=C0102
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


def render(x, y, **kwargs) -> matplotlib.figure.Figure:  # pylint:disable=C0103
    fig, ax = painter.utils.configure(**kwargs)  # pylint:disable=C0103
    if not y:
        return None
    xlim = kwargs.get('xlim', None)
    if xlim:
        ax.set_xlim(xlim)
    ymax = max(y) * 1.1
    if ymax:
        ax.set_ylim((0, ymax))
    plt.bar(x=x, height=y, width=0.5)
    return fig
