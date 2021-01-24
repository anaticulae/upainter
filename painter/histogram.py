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


def render(
        data: list,
        width: float = 5.12,  # 512 pixel
        height: float = 5.12,  # 512 pixel
        title: str = None,
        xlabel: str = None,
        ylabel: str = None,
) -> matplotlib.figure.Figure:
    fig = plt.figure(figsize=(width, height))
    if xlabel:
        plt.xlabel(xlabel, fontsize=20)
    if ylabel:
        plt.ylabel(ylabel, fontsize=20)
    if title:
        plt.title(title, fontsize=30)
    plt.hist(data)
    return fig
