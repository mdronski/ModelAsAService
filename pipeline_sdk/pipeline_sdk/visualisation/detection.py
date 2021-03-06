from functools import partial
from typing import List, Tuple

import numpy as np

from ..config import PEOPLE_DETECTION_COLOR, FACE_DETECTION_COLOR
from ..primitives import BoundingBox
from .utils import draw_bbox, for_each


def draw_people_detections(image: np.ndarray,
                           people_detections: List[BoundingBox]
                           ) -> np.ndarray:
    return draw_detections(
        image=image,
        detections=people_detections,
        color=PEOPLE_DETECTION_COLOR
    )


def draw_face_detections(image: np.ndarray,
                         face_detections: List[BoundingBox]
                         ) -> np.ndarray:
    return draw_detections(
        image=image,
        detections=face_detections,
        color=FACE_DETECTION_COLOR
    )


def draw_detections(image: np.ndarray,
                    detections: List[BoundingBox],
                    color: Tuple[int, int, int]
                    ) -> np.ndarray:
    image = image.copy()
    place_bbbox = partial(
        draw_bbox, input_image=image, color=color
    )
    for_each(iterable=detections, side_effect=place_bbbox)
    return image



