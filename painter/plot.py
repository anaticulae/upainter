# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import matplotlib.figure
import matplotlib.pyplot
import matplotlib.ticker

import painter.__patch__
import painter.utils


def render(
        *args,
        labels=None,
        legends=None,
        **kwargs,
) -> matplotlib.figure.Figure:
    if not args:
        raise ValueError(f'empty data: {args}')
    fig, ax = painter.utils.configure(**kwargs)  # pylint:disable=C0103

    if labels:
        ax.xaxis.set_major_formatter(painter.__patch__.IndexFormatter(labels))
        ax.xaxis.set_major_locator(matplotlib.ticker.IndexLocator(1, 0))
    ncol = kwargs.get('ncol', 10)
    ncol = int(len(legends) / ncol) + 1
    frameon = kwargs.get('frameon', True)
    for line, style in zip(args, painter.utils.linestyle()):
        matplotlib.pyplot.plot(line, style)

    if legends:
        ax.legend(legends, ncol=ncol, loc='upper left', frameon=frameon)
    return fig
