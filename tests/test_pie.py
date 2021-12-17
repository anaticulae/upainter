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


@pytest.fixture
def pie_example():
    data = [1, 1, 2, 3, 4]
    labels = [
        'Alf',
        'Bounus',
        'Conrad',
        'Dome',
        'Erni',
    ]
    rendered = painter.pie_render(
        x=data,
        labels=labels,
    )
    return rendered


def test_pie_render(pie_example):  # pylint:disable=W0621
    rendered = pie_example
    assert rendered
    painter.show_figure(rendered)
