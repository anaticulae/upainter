# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import upainter
import utilo


def test_plot_render():
    x = [item * 0.5 for item in utilo.rlist(10)]
    y = utilo.rlist(10)
    legends = ['first', 'second']
    labels = [f'label {item}' for item in range(10)]
    rendered = upainter.plot_render(
        x,
        y,
        labels=labels,
        width=15.0,
        legends=legends,
        ncol=5,
    )
    assert rendered
    upainter.show_figure(rendered)
