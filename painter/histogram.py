# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import matplotlib.figure
import matplotlib.pyplot

import painter.utils


def render(
    data: list,
    width: float = 5.12,  # 512 pixel
    height: float = 5.12,  # 512 pixel
    title: str = None,
    xlabel: str = None,
    ylabel: str = None,
    hist: dict = None,
    **kwargs,
) -> matplotlib.figure.Figure:
    fig, _ = painter.utils.configure(
        width=width,
        height=height,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        **kwargs,
    )
    if hist is None:
        hist = dict()
    matplotlib.pyplot.hist(data, **hist)
    return fig
