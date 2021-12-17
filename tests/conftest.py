# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

# pylint:disable=W0611,C0413
from tests.test_histogram import histogram_example
from tests.test_pie import pie_example
