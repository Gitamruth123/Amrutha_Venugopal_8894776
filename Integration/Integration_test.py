import rectanglearea
def test_rectangle_area_pass():
    length = 5
    width = 3
    expected_area = 15
    calculated_area = rectanglearea.rectanglearea(length, width)
    assert calculated_area == expected_area, f"Expected area {expected_area}, but got {calculated_area}"

# Test Case 2: Failing Test Case
def test_rectangle_area_fail():
    length = 5
    width = -3  # This will fail as width must be positive
    expected_area = 15
    calculated_area = rectanglearea.rectanglearea(length, width)
    assert calculated_area == expected_area, f"Expected area {expected_area}, but got {calculated_area}"