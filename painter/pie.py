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

import painter.utils


def render(
    x,
    labels=None,
    absolute: bool = True,
    **kwargs,
) -> matplotlib.figure.Figure:
    """\
    #absolute: use values instead of percentage
    """
    fig, _ = painter.utils.configure(**kwargs)  # pylint:disable=C0103
    label_fontsize = kwargs.get('label_fontsize', 20)

    def selector(item):
        sums = sum(x)
        return '%d' % (sums * item / 100)

    matplotlib.pyplot.pie(
        x=x,
        labels=labels,
        radius=1,
        autopct=selector if absolute else '%d',
        textprops=dict(size=label_fontsize),
    )
    return fig
