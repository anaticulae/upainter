#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import upainter.__backend__
from upainter.bar import render as bar_render
from upainter.details import contour
from upainter.details import contour_diff
from upainter.details import entropy
from upainter.details import entropy_diff
from upainter.grayscale import gray
from upainter.histogram import render as histogram_render
from upainter.pie import render as pie_render
from upainter.plot import render as plot_render
from upainter.scatter import render as scatter_render
from upainter.show import show_figure
from upainter.utils import colors
from upainter.utils import default_markers
from upainter.utils import ensure_image
from upainter.utils import figure_toimage
from upainter.utils import image_frombytes
from upainter.utils import isfigure
from upainter.utils import isimage
from upainter.utils import linestyle
from upainter.utils import markers
from upainter.writer import close_figure
from upainter.writer import png
from upainter.writer import save

__version__ = '0.13.3'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
