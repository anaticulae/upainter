# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import upainter


def test_bar_render_with_labels():
    data = [0, 1, 2, 3, 4, 5, 6, 7]
    rendered = upainter.bar_render(
        x=data,
        y=data,
        title='simple bar plot',
        xlabel='bottom',
        ylabel='left',
        grid=True,
    )
    assert rendered
    upainter.show_figure(rendered)


def test_bar_render_empty():
    data = []
    rendered = upainter.bar_render(
        x=data,
        y=data,
    )
    assert rendered is None


def test_bar_render_ints():
    rendered = upainter.bar_render(
        x=[1, 2, 3, 4],
        y=[1, 2, 3, 4],
        intlabel=(False, True),
    )
    assert rendered
    upainter.show_figure(rendered)
    rendered = upainter.png(rendered)
    assert len(rendered) in {6174, 6175}  # rendering changes, verify figure!
