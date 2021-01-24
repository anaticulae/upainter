# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import painter
import tests


def test_bar_render():
    data = [0, 1, 2, 3, 4, 5, 6, 7]
    rendered = painter.bar_render(
        x=data,
        y=data,
        title='simple bar plot',
        xlabel='bottom',
        ylabel='left',
        grid=True,
    )
    assert rendered
    tests.show_figure(rendered)
