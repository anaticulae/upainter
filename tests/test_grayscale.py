# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import upainter


def test_gray(pie_example):
    painted = pie_example
    png = upainter.png(painted)
    image = upainter.image_frombytes(png)
    before = len(image.histogram())
    # reduce amount of colors
    gray = upainter.gray(image)
    after = len(gray.histogram())
    # 1024 - 256
    diff = before - after
    assert diff == 768
