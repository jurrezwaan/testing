from main import get_none
from main import flatten_dict


def test_get_none():
    assert get_none() is None


def test_flatten_dict():
    test_1 = flatten_dict({'a': 1, 'b': 2})
    test_2 = flatten_dict({'a': 1, 'b': 2, 'c': [1, 2, 3, 4]})
    test_3 = flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
    assert type(test_1) == list
    assert type(test_2) == list
    assert type(test_3) == list
