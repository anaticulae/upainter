# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import matplotlib.ticker


# COPIED FROM MATPLOTLIB
class IndexFormatter(matplotlib.ticker.Formatter):
    """\
    Format the position x to the nearest i-th label where ``i = int(x + 0.5)``.
    Positions where ``i < 0`` or ``i > len(list)`` have no tick labels.

    Parameters
    ----------
    labels : list
        List of labels.
    """

    def __init__(self, labels):
        self.labels = labels
        self.number = len(labels)

    def __call__(self, x, pos=None):
        """\
        Return the format for tick value *x* at position pos.

        The position is ignored and the value is rounded to the nearest
        integer, which is used to look up the label.
        """
        i = int(x + 0.5)  # pylint:disable=C0103
        if i < 0 or i >= self.number:
            return ''
        return self.labels[i]
