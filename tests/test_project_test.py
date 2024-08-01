import pytest

from test_project import project_test


def test_my_data(my_data):
    assert my_data == 42

@pytest.mark.parametrize("values, expected_results", [
                         (
                             [1, 2, 3, 4, 5, 6],
                             [2.0, 3.0, 4.0, 5.0],
                         ),
                         (
                             [-1, -2, -3, -4, -5, -6],
                             [-2.0, -3.0, -4.0, -5.0],
                         ),
                         ])
def test_rolling_average(values, expected_results):

    result = project_test.rolling_average(values, 3)
    assert result == expected_results
