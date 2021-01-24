# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import pytest

import painter


def histogram_example():
    data = [1994, 1998, 2002, 2002, 2003, 2000]
    rendered = painter.histogram_render(
        data,
        width=10.0,  # 1000 pixel
        height=6.0,  # 600 pixel
        title='histogram',
        xlabel='user',
        ylabel='note',
    )
    return rendered


@pytest.mark.usefixtures('testdir')
def test_histogram_render():
    rendered = histogram_example()
    painter.save(rendered, 'figure')
    assert os.path.exists('figure')
