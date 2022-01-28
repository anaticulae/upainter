# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import PIL.ImageFilter

import painter


def entropy(image):
    return image.entropy()


def entropy_diff(image) -> float:
    grayscaled = painter.gray(image)
    before = entropy(image)
    after = entropy(grayscaled)
    diff = before - after
    return diff


def contour(image):
    image = painter.ensure_image(image)
    return image.filter(PIL.ImageFilter.CONTOUR)


def contour_diff(image):
    image = painter.ensure_image(image)
    before = contour(image)
    before = feature_count(before)
    grayscaled = image.convert('L')
    after = contour(grayscaled)
    after = feature_count(after)
    diff = before - after
    if diff > 0:
        return diff
    return 0


def feature_count(image) -> int:
    image = painter.ensure_image(image)
    image = image.convert('L')
    histo = image.histogram()[0]
    return histo
