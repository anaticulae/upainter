# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import matplotlib.pyplot as plt


def configure(**kwargs):
    width = kwargs.get('width', 5.12)  # 512 pixel
    height = kwargs.get('height', 5.12)  # 512 pixel
    xlabel = kwargs.get('xlabel', None)
    ylabel = kwargs.get('ylabel', None)
    title = kwargs.get('title', None)

    fig, ax = plt.subplots(figsize=(width, height))
    if xlabel:
        plt.xlabel(xlabel, fontsize=20)
    if ylabel:
        plt.ylabel(ylabel, fontsize=20)
    if title:
        plt.title(title, fontsize=30)
    return fig, ax
