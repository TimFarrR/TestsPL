import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return (x, y, radius)

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points

def get_point_position(circle, point):
    cx, cy, radius = circle
    px, py = point
    distance = math.sqrt((px - cx) * (px - cx) + (py - cy) * (py - cy))
    if distance < radius:
        return 1  # inside
    elif distance == radius:
        return 0  # on the circle
    else:
        return 2  # outside

def main():
    if len(sys.argv) != 3:
        print("Введите: python task2.py circle.txt points.txt")
        return
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    circle = read_circle_data(circle_file)
    points = read_points(points_file)
    
    for point in points:
        position = get_point_position(circle, point)
        print(position)

if __name__ == "__main__":
    main()
