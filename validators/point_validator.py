def parse_point(point_str):
    parts = point_str.split(',')

    if len(parts) != 2:
        raise ValueError("Format attendu: x,y")

    return int(parts[0]), int(parts[1])