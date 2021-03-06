'''This module houses the constants for the camera package'''
from enum import Enum, unique
import numpy as np

# python version
PYTHON_2 = 2


# Define Gazebo World default direction unit vectors
class GazeboWorld(object):
    forward = np.array((1.0, 0, 0))
    back = np.array((-1.0, 0, 0))
    right = np.array((0, -1.0, 0))
    left = np.array((0, 1.0, 0))
    up = np.array((0, 0, 1.0))
    down = np.array((0, 0, -1.0))


@unique
class CameraSettings(Enum):
    '''This enum is used to index into the camera settings list'''
    HORZ_FOV = 1
    PADDING_PCT = 2
    IMG_WIDTH = 3
    IMG_HEIGHT = 4

    @classmethod
    def get_empty_dict(cls):
        '''Returns dictionary with the enum as key values and None's as the values, clients
           are responsible for populating the dict accordingly
        '''
        empty_dict = dict()
        for val in cls._value2member_map_.values():
            empty_dict[val] = None
        return empty_dict
