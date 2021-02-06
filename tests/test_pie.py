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


def test_pie_render():
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
    assert rendered
    tests.show_figure(rendered)
