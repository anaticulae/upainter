# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila
import utilatest

import painter


def show_figure(figure):
    if not utilatest.single_execution():
        return
    with utila.make_tmpdir(root=__file__) as temp:
        png = str(os.path.join(temp, 'painted.png'))
        # write png
        painter.save(figure, png)
        # open png
        utila.run(f'start {png}')
