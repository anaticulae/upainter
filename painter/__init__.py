#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import painter.__backend__
from painter.bar import render as bar_render
from painter.details import contour
from painter.details import contour_diff
from painter.details import entropy
from painter.details import entropy_diff
from painter.grayscale import gray
from painter.histogram import render as histogram_render
from painter.pie import render as pie_render
from painter.plot import render as plot_render
from painter.scatter import render as scatter_render
from painter.show import show_figure
from painter.utils import colors
from painter.utils import default_markers
from painter.utils import ensure_image
from painter.utils import figure_toimage
from painter.utils import image_frombytes
from painter.utils import isfigure
from painter.utils import isimage
from painter.utils import linestyle
from painter.utils import markers
from painter.writer import close_figure
from painter.writer import png
from painter.writer import save

__version__ = '0.13.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
