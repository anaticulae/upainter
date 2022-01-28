# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import painter


def test_entropy_diff(pie_example):
    image = painter.figure_toimage(pie_example)
    diff = painter.entropy_diff(image)
    assert diff > 1.2


def test_entropy_second(histogram_example):
    image = painter.figure_toimage(histogram_example)
    diff = painter.entropy_diff(image)
    assert diff > 1.7


def test_contour_diff(histogram_example):
    """Histogram does not loses feature while grayscaling."""
    diff = painter.contour_diff(histogram_example)
    assert not diff
