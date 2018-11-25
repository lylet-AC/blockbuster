import mapgen
import os
from settings import *

def test_generate_map():

    # list may look inflated, but the output map is scaled.

    expected_list = [[(0, 0, 0)]]

    actual_list = mapgen.generate_map(os.path.join(TEST_FOLDER, "test_img.png"))

    assert repr(actual_list) == repr(expected_list)
