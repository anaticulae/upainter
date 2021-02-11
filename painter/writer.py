# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import io

import matplotlib.pyplot


def save(figure, path: str, format_: str = 'png'):
    figure.savefig(path, format=format_)


def close_figure(figure):
    matplotlib.pyplot.close(figure)


def png(figure, close: bool = True) -> bytes:
    buffer = io.BytesIO()
    # write to buffer
    save(figure, buffer)
    if close:
        close_figure(figure)
    result = buffer.getvalue()
    return result
