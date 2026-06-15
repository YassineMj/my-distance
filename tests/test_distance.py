from services.distance_service import calculate_distance

def test_distance():
    assert calculate_distance((0,0), (3,4)) == 5