# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import painter


def test_scatter_render_colored_legend():
    x, y = [10, 20, 15, 12, 50], [50, 20, 10, 33, 14]
    legend = [
        (133, 'first'),
        (6, 'second'),
        (80, 'third'),
        (33, 'fourth'),
        (99, 'fifth'),
    ]
    rendered = painter.scatter_render(
        x,
        y,
        legend=legend,
        grid=True,
    )
    assert rendered
    painter.show_figure(rendered)


def test_scatter_render_legend_no_value():
    x, y = [10, 20, 15, 12, 50], [50, 20, 10, 33, 14]
    legend = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
    ]
    rendered = painter.scatter_render(
        x,
        y,
        legend=legend,
        marker='xdoDx',
        grid=True,
    )
    assert rendered
    painter.show_figure(rendered)


def test_scatter_empty():
    x, y = [], []
    with pytest.raises(ValueError, match='require some data'):
        painter.scatter_render(
            x,
            y,
        )


def test_scatter_unequal_length():
    with pytest.raises(ValueError, match='must be the same size'):
        painter.scatter_render(
            x=[20, 30],
            y=[20, 10, 11],
        )

    with pytest.raises(ValueError, match='legend must be the same size'):
        painter.scatter_render(
            x=[20, 30],
            y=[20, 10],
            legend=['abc'],
        )
