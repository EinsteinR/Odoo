from box_sort import pack

from pytest import mark
from math import ceil


@mark.parametrize('checked_value', [i for i in range(1, 101)])
def test_used_the_smallest_boxes_amount(checked_value):
    excepted_value = ceil(checked_value/9)
    sum_number_of_boxes = sum(pack(checked_value).values())
    assert excepted_value == sum_number_of_boxes


def test_double_six_is_better_than_three_and_nine_boxes():
    for boxes in [pack(i) for i in range(1, 101)]:
        if boxes['box_s'] == 1 and boxes['box_l'] == 1:
            assert False  # "for some reason in example 2x 6 slot boxes are better than 3 and 9"
    assert True

