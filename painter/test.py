# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila
import utilatest

import painter


def show_figure(figure, always: bool = False, filename: str = 'painted.png'):
    if not always and not utilatest.single_execution():
        return
    if not utila.exists(figure):
        with utila.make_tmpdir(root=__file__) as temp:
            png = os.path.join(temp, filename)
            # write png
            if painter.isimage(figure):
                figure.save(png)
            elif isinstance(figure, bytes):
                utila.file_create_binary(png, figure)
            else:
                painter.save(figure, png)
    else:
        png = figure
    # open png
    utila.run(f'start {png}')
