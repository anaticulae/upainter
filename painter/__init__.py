#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import painter.__backend__
from painter.bar import render as bar_render
from painter.histogram import render as histogram_render
from painter.pie import render as pie_render
from painter.test import show_figure
from painter.utils import linestyle
from painter.writer import png
from painter.writer import save

__version__ = '0.5.2'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
