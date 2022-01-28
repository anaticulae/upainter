# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import painter


def test_png(histogram_example):
    rendered = histogram_example
    # render into bytes
    result = painter.png(rendered)
    assert isinstance(result, bytes)
    assert len(result) > 10000
