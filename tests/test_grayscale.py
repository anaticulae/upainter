# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import painter


def test_gray(pie_example):
    painted = pie_example
    png = painter.png(painted)
    image = painter.image_frombytes(png)
    before = len(image.histogram())
    # reduce amount of colors
    gray = painter.gray(image)
    after = len(gray.histogram())
    # 1024 - 256
    diff = before - after
    assert diff == 768
