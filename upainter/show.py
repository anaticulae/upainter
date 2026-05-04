# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import os

import upainter
import utilo


def show_figure(figure, always: bool = False, filename: str = 'painted.png'):
    if not always and not single_execution():
        return
    if not utilo.exists(figure):
        root = utilo.path_parent(__file__)
        with utilo.make_tmpdir(root=root) as temp:
            png = os.path.join(temp, filename)
            # write png
            if upainter.isimage(figure):
                figure.save(png)
            elif isinstance(figure, bytes):
                utilo.file_create_binary(png, figure)
            else:
                upainter.save(figure, png)
    else:
        png = figure
    # open png
    utilo.run(f'start {png}')


def single_execution() -> bool:
    with contextlib.suppress(ModuleNotFoundError):
        import utilotest
        return utilotest.single_execution()
    return False
