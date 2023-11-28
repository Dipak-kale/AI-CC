def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def nearest_neighbor_algorithm(points):
    num_points = len(points)
    unvisited = set(range(1, num_points))
    current_point = 0
    tour = [current_point]

    while unvisited:
        nearest_point = min(unvisited, key=lambda x: calculate_distance(points[current_point], points[x]))
        tour.append(nearest_point)
        unvisited.remove(nearest_point)
        current_point = nearest_point

    return tour

if __name__ == "__main__":
    # Example points (replace with your own coordinates)
    points = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

    # Find a tour using the nearest neighbor algorithm
    tour = nearest_neighbor_algorithm(points)

    # Print the result
    print(f"Optimal Tour: {tour}")
    print(f"Total Distance: {sum(calculate_distance(points[tour[i]], points[tour[i + 1]]) for i in range(len(tour) - 1)) + calculate_distance(points[tour[-1]], points[tour[0]])}")
