import math
from time import sleep, time
import gc

def quickhull_initial_call(ConvexHullVisualization, delay):
    points_copy = list(ConvexHullVisualization.points)
    if len(points_copy) < 3:
        return

    ConvexHullVisualization.clear_lines()
    print("starting quickhull_initial_call")
    left = min(points_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    if ConvexHullVisualization.current_visualization_mode_index == 1:
        convex_hull = quickhull_without_delay(ConvexHullVisualization, points_copy, left, right, line_to_remove=None)
    elif ConvexHullVisualization.current_visualization_mode_index == 2:
        convex_hull = quickhull_with_delay(ConvexHullVisualization, points_copy, left, right, delay, line_to_remove=None)
    else:
        convex_hull = quickhull_performance(ConvexHullVisualization, points_copy, left, right)
    print("printing convex hull:")
    for point in convex_hull:
        print(point)
    print("############################################")

def quickhull_with_delay(ConvexHullVisualization, points_copy, left, right, delay, line_to_remove):
    left_canvas_x, left_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(left[0], left[1])
    right_canvas_x, right_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(right[0], right[1])
    length_points = len(points_copy)
    if length_points == 1:
        point = points_copy[0]
        point_canvas_x, point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(point[0], point[1])
        ConvexHullVisualization.draw_line(left_canvas_x, left_canvas_y, point_canvas_x, point_canvas_y)
        ConvexHullVisualization.draw_line(point_canvas_x, point_canvas_y, right_canvas_x, right_canvas_y)
        ConvexHullVisualization.root.update()
        return points_copy
    
    if line_to_remove is not None:
        ConvexHullVisualization.canvas.delete(line_to_remove)
        ConvexHullVisualization.lines.remove(line_to_remove)
        ConvexHullVisualization.root.update()
    # Find the furthest point from the line defined by left and right points
    max_distance = -1
    furthest_point = None
    for point in points_copy:
        distance = distance_point_to_line(point, (left, right))
        if distance > max_distance:
            max_distance = distance
            furthest_point = point

    lh_list = []
    hr_list = []
    for point in points_copy:
        if point is left:
            lh_list.append(point)
        elif point is right:
            hr_list.append(point)
        elif point is furthest_point:
            lh_list.append(point)
            hr_list.append(point)
        else:
            if ConvexHullVisualization.is_not_right_turn(left, furthest_point, point):
                lh_list.append(point)
            if ConvexHullVisualization.is_not_right_turn(furthest_point, right, point):
                hr_list.append(point)
    
    furthest_point_canvas_x, furthest_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(furthest_point[0], furthest_point[1])
    lh_line = ConvexHullVisualization.draw_line(left_canvas_x, left_canvas_y, furthest_point_canvas_x, furthest_point_canvas_y)
    hr_line = ConvexHullVisualization.draw_line(furthest_point_canvas_x, furthest_point_canvas_y, right_canvas_x, right_canvas_y)
    ConvexHullVisualization.root.update()
    sleep(delay)
    hull_1 = quickhull_with_delay(ConvexHullVisualization, lh_list, left, furthest_point, delay, lh_line)
    hull_2 = quickhull_with_delay(ConvexHullVisualization, hr_list, furthest_point, right, delay, hr_line)
    for point in hull_2:
        if point[0] == right[0] and point[1] == right[1]:
            hull_2.remove(point)
            break
    hull_2.extend(hull_1)
    return hull_2

def quickhull_without_delay(ConvexHullVisualization, points_copy, left, right, line_to_remove):
    
    left_canvas_x, left_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(left[0], left[1])
    right_canvas_x, right_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(right[0], right[1])
    length_points = len(points_copy)
    if length_points == 1:
        point = points_copy[0]
        point_canvas_x, point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(point[0], point[1])
        ConvexHullVisualization.draw_line(left_canvas_x, left_canvas_y, point_canvas_x, point_canvas_y)
        ConvexHullVisualization.draw_line(point_canvas_x, point_canvas_y, right_canvas_x, right_canvas_y)
        ConvexHullVisualization.root.update()
        return points_copy
    
    if line_to_remove is not None:
        ConvexHullVisualization.canvas.delete(line_to_remove)
        ConvexHullVisualization.lines.remove(line_to_remove)
        ConvexHullVisualization.root.update()
    # Find the furthest point from the line defined by left and right points
    max_distance = -1
    furthest_point = None
    for point in points_copy:
        distance = distance_point_to_line(point, (left, right))
        if distance > max_distance:
            max_distance = distance
            furthest_point = point

    lh_list = []
    hr_list = []
    for point in points_copy:
        if point is left:
            lh_list.append(point)
        elif point is right:
            hr_list.append(point)
        elif point is furthest_point:
            lh_list.append(point)
            hr_list.append(point)
        else:
            if ConvexHullVisualization.is_not_right_turn(left, furthest_point, point):
                lh_list.append(point)
            if ConvexHullVisualization.is_not_right_turn(furthest_point, right, point):
                hr_list.append(point)
    
    furthest_point_canvas_x, furthest_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(furthest_point[0], furthest_point[1])
    lh_line = ConvexHullVisualization.draw_line(left_canvas_x, left_canvas_y, furthest_point_canvas_x, furthest_point_canvas_y)
    hr_line = ConvexHullVisualization.draw_line(furthest_point_canvas_x, furthest_point_canvas_y, right_canvas_x, right_canvas_y)
    ConvexHullVisualization.root.update()
    hull_1 = quickhull_without_delay(ConvexHullVisualization, lh_list, left, furthest_point, lh_line)
    hull_2 = quickhull_without_delay(ConvexHullVisualization, hr_list, furthest_point, right, hr_line)
    for point in hull_2:
        if point[0] == right[0] and point[1] == right[1]:
            hull_2.remove(point)
            break
    hull_2.extend(hull_1)
    return hull_2

def quickhull_performance(ConvexHullVisualization, points_copy, left, right):

    length_points = len(points_copy)
    if length_points == 1:
        return points_copy

    # Find the furthest point from the line defined by left and right points
    max_distance = -1
    furthest_point = None
    for point in points_copy:
        distance = distance_point_to_line(point, (left, right))
        if distance > max_distance:
            max_distance = distance
            furthest_point = point

    lh_list = []
    hr_list = []
    for point in points_copy:
        if point is left:
            lh_list.append(point)
        elif point is right:
            hr_list.append(point)
        elif point is furthest_point:
            lh_list.append(point)
            hr_list.append(point)
        else:
            if ConvexHullVisualization.is_not_right_turn(left, furthest_point, point):
                lh_list.append(point)
            if ConvexHullVisualization.is_not_right_turn(furthest_point, right, point):
                hr_list.append(point)

    ConvexHullVisualization.root.update()
    hull_1 = quickhull_performance(ConvexHullVisualization, lh_list, left, furthest_point )
    hull_2 = quickhull_performance(ConvexHullVisualization, hr_list, furthest_point, right)
    for point in hull_2:
        if point[0] == right[0] and point[1] == right[1]:
            hull_2.remove(point)
            break
    hull_2.extend(hull_1)
    
    return hull_2

def distance_point_to_line(p, line):
    """
    Calculate the perpendicular distance from point p to the line defined by two points.
    
    Args:
        p (tuple): The point (x, y) for which the distance is to be calculated.
        line (tuple, tuple): Two points defining the line ((x1, y1), (x2, y2)).
        
    Returns:
        float: The perpendicular distance from the point to the line.
    """
    x1, y1 = line[0]
    x2, y2 = line[1]
    numerator = abs((y2 - y1) * p[0] - (x2 - x1) * p[1] + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    if denominator == 0:
        return 0
    return numerator / denominator

def is_left_turn(p0, p1, p2):
    return p0[0] * p1[1] + p2[0] * p0[1] + p1[0] * p2[1] - p2[0] * p1[1] - p0[0] * p2[1] - p1[0] * p0[1] >= 0

def benchmark_thousands_quickhull(app,
                        gaussian_1_000,
                        gaussian_2_000,
                        gaussian_3_000,
                        gaussian_4_000,
                        gaussian_5_000,
                        gaussian_6_000,
                        gaussian_7_000,
                        gaussian_8_000,
                        gaussian_9_000,
                        uniform_1_000,
                        uniform_2_000,
                        uniform_3_000,
                        uniform_4_000,
                        uniform_5_000,
                        uniform_6_000,
                        uniform_7_000,
                        uniform_8_000,
                        uniform_9_000):
    gaussian_1_000_quickhull_copy = list(gaussian_1_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_1_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_1_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_1_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_1_000 ended!")
    del gaussian_1_000_quickhull_copy
    gc.collect()

    gaussian_2_000_quickhull_copy = list(gaussian_2_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_2_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_2_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_2_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_2_000 ended!")
    del gaussian_2_000_quickhull_copy
    gc.collect()

    gaussian_3_000_quickhull_copy = list(gaussian_3_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_3_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_3_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_3_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_3_000 ended!")
    del gaussian_3_000_quickhull_copy
    gc.collect()

    gaussian_4_000_quickhull_copy = list(gaussian_4_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_4_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_4_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_4_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_4_000 ended!")
    del gaussian_4_000_quickhull_copy
    gc.collect()

    gaussian_5_000_quickhull_copy = list(gaussian_5_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_5_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_5_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_5_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_5_000 ended!")
    del gaussian_5_000_quickhull_copy
    gc.collect()

    gaussian_6_000_quickhull_copy = list(gaussian_6_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_6_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_6_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_6_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_6_000 ended!")
    del gaussian_6_000_quickhull_copy
    gc.collect()

    gaussian_7_000_quickhull_copy = list(gaussian_7_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_7_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_7_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_7_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_7_000 ended!")
    del gaussian_7_000_quickhull_copy
    gc.collect()

    gaussian_8_000_quickhull_copy = list(gaussian_8_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_8_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_8_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_8_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_8_000 ended!")
    del gaussian_8_000_quickhull_copy
    gc.collect()

    gaussian_9_000_quickhull_copy = list(gaussian_9_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_9_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_9_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_9_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_9_000 ended!")
    del gaussian_9_000_quickhull_copy
    gc.collect()

    uniform_1_000_quickhull_copy = list(uniform_1_000)
    start_time_uniform_quickhull= time()
    left = min(uniform_1_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_1_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_1_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_1_000 ended!")
    del uniform_1_000_quickhull_copy
    gc.collect()

    uniform_2_000_quickhull_copy = list(uniform_2_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_2_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_2_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_2_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_2_000 ended!")
    del uniform_2_000_quickhull_copy
    gc.collect()

    uniform_3_000_quickhull_copy = list(uniform_3_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_3_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_3_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_3_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_3_000 ended!")
    del uniform_3_000_quickhull_copy
    gc.collect()

    uniform_4_000_quickhull_copy = list(uniform_4_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_4_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_4_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_4_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_4_000 ended!")
    del uniform_4_000_quickhull_copy
    gc.collect()

    uniform_5_000_quickhull_copy = list(uniform_5_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_5_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_5_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_5_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_5_000 ended!")
    del uniform_5_000_quickhull_copy
    gc.collect()

    uniform_6_000_quickhull_copy = list(uniform_6_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_6_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_6_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_6_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_6_000 ended!")
    del uniform_6_000_quickhull_copy
    gc.collect()

    uniform_7_000_quickhull_copy = list(uniform_7_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_7_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_7_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_7_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_7_000 ended!")
    del uniform_7_000_quickhull_copy
    gc.collect()

    uniform_8_000_quickhull_copy = list(uniform_8_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_8_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_8_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_8_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_8_000 ended!")
    del uniform_8_000_quickhull_copy
    gc.collect()

    uniform_9_000_quickhull_copy = list(uniform_9_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_9_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_9_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_9_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_9_000 ended!")
    del uniform_9_000_quickhull_copy
    gc.collect()

    return time_gaussian_quickhull_1_000, time_gaussian_quickhull_2_000, time_gaussian_quickhull_3_000, time_gaussian_quickhull_4_000, time_gaussian_quickhull_5_000, time_gaussian_quickhull_6_000, time_gaussian_quickhull_7_000, time_gaussian_quickhull_8_000, time_gaussian_quickhull_9_000, time_uniform_quickhull_1_000, time_uniform_quickhull_2_000, time_uniform_quickhull_3_000, time_uniform_quickhull_4_000, time_uniform_quickhull_5_000, time_uniform_quickhull_6_000, time_uniform_quickhull_7_000, time_uniform_quickhull_8_000, time_uniform_quickhull_9_000

def benchmark_tens_of_thousands_quickhull(app,
                                            gaussian_10_000,
                                            gaussian_20_000,
                                            gaussian_30_000,
                                            gaussian_40_000,
                                            gaussian_50_000,
                                            gaussian_60_000,
                                            gaussian_70_000,
                                            gaussian_80_000,
                                            gaussian_90_000,
                                            uniform_10_000,
                                            uniform_20_000,
                                            uniform_30_000,
                                            uniform_40_000,
                                            uniform_50_000,
                                            uniform_60_000,
                                            uniform_70_000,
                                            uniform_80_000,
                                            uniform_90_000):
    gaussian_10_000_quickhull_copy = list(gaussian_10_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_10_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_10_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_10_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_10_000 ended!")
    del gaussian_10_000_quickhull_copy
    gc.collect()

    gaussian_20_000_quickhull_copy = list(gaussian_20_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_20_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_20_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_20_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_20_000 ended!")
    del gaussian_20_000_quickhull_copy
    gc.collect()

    gaussian_30_000_quickhull_copy = list(gaussian_30_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_30_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_30_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_30_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_30_000 ended!")
    del gaussian_30_000_quickhull_copy
    gc.collect()

    gaussian_40_000_quickhull_copy = list(gaussian_40_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_40_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_40_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_40_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_40_000 ended!")
    del gaussian_40_000_quickhull_copy
    gc.collect()

    gaussian_50_000_quickhull_copy = list(gaussian_50_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_50_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_50_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_50_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_50_000 ended!")
    del gaussian_50_000_quickhull_copy
    gc.collect()

    gaussian_60_000_quickhull_copy = list(gaussian_60_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_60_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_60_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_60_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_60_000 ended!")
    del gaussian_60_000_quickhull_copy
    gc.collect()

    gaussian_70_000_quickhull_copy = list(gaussian_70_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_70_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_70_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_70_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_70_000 ended!")
    del gaussian_70_000_quickhull_copy
    gc.collect()

    gaussian_80_000_quickhull_copy = list(gaussian_80_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_80_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_80_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_80_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_80_000 ended!")
    del gaussian_80_000_quickhull_copy
    gc.collect()

    gaussian_90_000_quickhull_copy = list(gaussian_90_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_90_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_90_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_90_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_90_000 ended!")
    del gaussian_90_000_quickhull_copy
    gc.collect()

    uniform_10_000_quickhull_copy = list(uniform_10_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_10_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_10_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_10_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_10_000 ended!")
    del uniform_10_000_quickhull_copy
    gc.collect()

    uniform_20_000_quickhull_copy = list(uniform_20_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_20_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_20_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_20_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_20_000 ended!")
    del uniform_20_000_quickhull_copy
    gc.collect()

    uniform_30_000_quickhull_copy = list(uniform_30_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_30_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_30_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_30_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_30_000 ended!")
    del uniform_30_000_quickhull_copy
    gc.collect()

    uniform_40_000_quickhull_copy = list(uniform_40_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_40_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_40_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_40_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_40_000 ended!")
    del uniform_40_000_quickhull_copy
    gc.collect()

    uniform_50_000_quickhull_copy = list(uniform_50_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_50_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_50_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_50_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_50_000 ended!")
    del uniform_50_000_quickhull_copy
    gc.collect()

    uniform_60_000_quickhull_copy = list(uniform_60_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_60_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_60_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_60_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_60_000 ended!")
    del uniform_60_000_quickhull_copy
    gc.collect()

    uniform_70_000_quickhull_copy = list(uniform_70_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_70_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_70_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_70_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_70_000 ended!")
    del uniform_70_000_quickhull_copy
    gc.collect()

    uniform_80_000_quickhull_copy = list(uniform_80_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_80_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_80_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_80_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_80_000 ended!")
    del uniform_80_000_quickhull_copy
    gc.collect()

    uniform_90_000_quickhull_copy = list(uniform_90_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_90_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_90_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_90_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_90_000 ended!")
    del uniform_90_000_quickhull_copy
    gc.collect()

    return time_gaussian_quickhull_10_000, time_gaussian_quickhull_20_000, time_gaussian_quickhull_30_000, time_gaussian_quickhull_40_000, time_gaussian_quickhull_50_000, time_gaussian_quickhull_60_000, time_gaussian_quickhull_70_000, time_gaussian_quickhull_80_000, time_gaussian_quickhull_90_000, time_uniform_quickhull_10_000, time_uniform_quickhull_20_000, time_uniform_quickhull_30_000, time_uniform_quickhull_40_000, time_uniform_quickhull_50_000, time_uniform_quickhull_60_000, time_uniform_quickhull_70_000, time_uniform_quickhull_80_000, time_uniform_quickhull_90_000

def benchmark_hundreds_of_thousands_quickhull(app,
                                                gaussian_100_000,
                                                gaussian_200_000,
                                                gaussian_300_000,
                                                gaussian_400_000,
                                                gaussian_500_000,
                                                gaussian_600_000,
                                                gaussian_700_000,
                                                gaussian_800_000,
                                                gaussian_900_000,
                                                uniform_100_000,
                                                uniform_200_000,
                                                uniform_300_000,
                                                uniform_400_000,
                                                uniform_500_000,
                                                uniform_600_000,
                                                uniform_700_000,
                                                uniform_800_000,
                                                uniform_900_000):
    gaussian_100_000_quickhull_copy = list(gaussian_100_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_100_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_100_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_100_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_100_000 ended!")
    del gaussian_100_000_quickhull_copy
    gc.collect()

    gaussian_200_000_quickhull_copy = list(gaussian_200_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_200_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_200_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_200_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_200_000 ended!")
    del gaussian_200_000_quickhull_copy
    gc.collect()

    gaussian_300_000_quickhull_copy = list(gaussian_300_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_300_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_300_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_300_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_300_000 ended!")
    del gaussian_300_000_quickhull_copy
    gc.collect()

    gaussian_400_000_quickhull_copy = list(gaussian_400_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_400_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_400_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_400_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_400_000 ended!")
    del gaussian_400_000_quickhull_copy
    gc.collect()

    gaussian_500_000_quickhull_copy = list(gaussian_500_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_500_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_500_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_500_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_500_000 ended!")
    del gaussian_500_000_quickhull_copy
    gc.collect()

    gaussian_600_000_quickhull_copy = list(gaussian_600_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_600_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_600_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_600_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_600_000 ended!")
    del gaussian_600_000_quickhull_copy
    gc.collect()

    gaussian_700_000_quickhull_copy = list(gaussian_700_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_700_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_700_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_700_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_700_000 ended!")
    del gaussian_700_000_quickhull_copy
    gc.collect()

    gaussian_800_000_quickhull_copy = list(gaussian_800_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_800_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_800_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_800_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_800_000 ended!")
    del gaussian_800_000_quickhull_copy
    gc.collect()

    gaussian_900_000_quickhull_copy = list(gaussian_900_000)
    start_time_gaussian_quickhull = time()
    left = min(gaussian_900_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, gaussian_900_000_quickhull_copy, left, right)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_900_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_900_000 ended!")
    del gaussian_900_000_quickhull_copy
    gc.collect()

    uniform_100_000_quickhull_copy = list(uniform_100_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_100_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_100_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_100_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_100_000 ended!")
    del uniform_100_000_quickhull_copy
    gc.collect()

    uniform_200_000_quickhull_copy = list(uniform_200_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_200_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_200_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_200_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_200_000 ended!")
    del uniform_200_000_quickhull_copy
    gc.collect()

    uniform_300_000_quickhull_copy = list(uniform_300_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_300_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_300_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_300_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_300_000 ended!")
    del uniform_300_000_quickhull_copy
    gc.collect()

    uniform_400_000_quickhull_copy = list(uniform_400_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_400_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_400_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_400_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_400_000 ended!")
    del uniform_400_000_quickhull_copy
    gc.collect()

    uniform_500_000_quickhull_copy = list(uniform_500_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_500_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_500_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_500_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_500_000 ended!")
    del uniform_500_000_quickhull_copy
    gc.collect()

    uniform_600_000_quickhull_copy = list(uniform_600_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_600_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_600_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_600_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_600_000 ended!")
    del uniform_600_000_quickhull_copy
    gc.collect()

    uniform_700_000_quickhull_copy = list(uniform_700_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_700_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_700_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_700_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_700_000 ended!")
    del uniform_700_000_quickhull_copy
    gc.collect()

    uniform_800_000_quickhull_copy = list(uniform_800_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_800_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_800_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_800_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_800_000 ended!")
    del uniform_800_000_quickhull_copy
    gc.collect()

    uniform_900_000_quickhull_copy = list(uniform_900_000)
    start_time_uniform_quickhull = time()
    left = min(uniform_900_000_quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, uniform_900_000_quickhull_copy, left, right)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_900_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_900_000 ended!")
    del uniform_900_000_quickhull_copy
    gc.collect()

    return time_gaussian_quickhull_100_000, time_gaussian_quickhull_200_000, time_gaussian_quickhull_300_000, time_gaussian_quickhull_400_000, time_gaussian_quickhull_500_000, time_gaussian_quickhull_600_000, time_gaussian_quickhull_700_000, time_gaussian_quickhull_800_000, time_gaussian_quickhull_900_000, time_uniform_quickhull_100_000, time_uniform_quickhull_200_000, time_uniform_quickhull_300_000, time_uniform_quickhull_400_000, time_uniform_quickhull_500_000, time_uniform_quickhull_600_000, time_uniform_quickhull_700_000, time_uniform_quickhull_800_000, time_uniform_quickhull_900_000

def benchmark_millions_quickhull(app,
                                                gaussian_1_000_000,
                                                gaussian_2_000_000,
                                                gaussian_3_000_000,
                                                gaussian_4_000_000,
                                                gaussian_5_000_000,
                                                gaussian_6_000_000,
                                                gaussian_7_000_000,
                                                gaussian_8_000_000,
                                                gaussian_9_000_000,
                                                uniform_1_000_000,
                                                uniform_2_000_000,
                                                uniform_3_000_000,
                                                uniform_4_000_000,
                                                uniform_5_000_000,
                                                uniform_6_000_000,
                                                uniform_7_000_000,
                                                uniform_8_000_000,
                                                uniform_9_000_000):
    gaussian_1_000_000_quickhull_copy = list(gaussian_1_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_1_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_1_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_1_000_000 ended!")
    del gaussian_1_000_000_quickhull_copy
    gc.collect()

    gaussian_2_000_000_quickhull_copy = list(gaussian_2_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_2_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_2_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_2_000_000 ended!")
    del gaussian_2_000_000_quickhull_copy
    gc.collect()

    gaussian_3_000_000_quickhull_copy = list(gaussian_3_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_3_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_3_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_3_000_000 ended!")
    del gaussian_3_000_000_quickhull_copy
    gc.collect()

    gaussian_4_000_000_quickhull_copy = list(gaussian_4_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_4_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_4_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_4_000_000 ended!")
    del gaussian_4_000_000_quickhull_copy
    gc.collect()

    gaussian_5_000_000_quickhull_copy = list(gaussian_5_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_5_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_5_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_5_000_000 ended!")
    del gaussian_5_000_000_quickhull_copy
    gc.collect()

    gaussian_6_000_000_quickhull_copy = list(gaussian_6_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_6_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_6_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_6_000_000 ended!")
    del gaussian_6_000_000_quickhull_copy
    gc.collect()

    gaussian_7_000_000_quickhull_copy = list(gaussian_7_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_7_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_7_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_7_000_000 ended!")
    del gaussian_7_000_000_quickhull_copy
    gc.collect()

    gaussian_8_000_000_quickhull_copy = list(gaussian_8_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_8_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_8_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_8_000_000 ended!")
    del gaussian_8_000_000_quickhull_copy
    gc.collect()

    gaussian_9_000_000_quickhull_copy = list(gaussian_9_000_000)
    start_time_gaussian_quickhull = time()
    quickhull_performance(app, gaussian_9_000_000_quickhull_copy)
    end_time_gaussian_quickhull = time()
    time_gaussian_quickhull_9_000_000 = end_time_gaussian_quickhull - start_time_gaussian_quickhull
    print("gaussian_quickhull_9_000_000 ended!")
    del gaussian_9_000_000_quickhull_copy
    gc.collect()

    uniform_1_000_000_quickhull_copy = list(uniform_1_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_1_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_1_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_1_000_000 ended!")
    del uniform_1_000_000_quickhull_copy
    gc.collect()

    uniform_2_000_000_quickhull_copy = list(uniform_2_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_2_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_2_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_2_000_000 ended!")
    del uniform_2_000_000_quickhull_copy
    gc.collect()

    uniform_3_000_000_quickhull_copy = list(uniform_3_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_3_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_3_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_3_000_000 ended!")
    del uniform_3_000_000_quickhull_copy
    gc.collect()

    uniform_4_000_000_quickhull_copy = list(uniform_4_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_4_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_4_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_4_000_000 ended!")
    del uniform_4_000_000_quickhull_copy
    gc.collect()

    uniform_5_000_000_quickhull_copy = list(uniform_5_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_5_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_5_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_5_000_000 ended!")
    del uniform_5_000_000_quickhull_copy
    gc.collect()

    uniform_6_000_000_quickhull_copy = list(uniform_6_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_6_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_6_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_6_000_000 ended!")
    del uniform_6_000_000_quickhull_copy
    gc.collect()

    uniform_7_000_000_quickhull_copy = list(uniform_7_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_7_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_7_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_7_000_000 ended!")
    del uniform_7_000_000_quickhull_copy
    gc.collect()

    uniform_8_000_000_quickhull_copy = list(uniform_8_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_8_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_8_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_8_000_000 ended!")
    del uniform_8_000_000_quickhull_copy
    gc.collect()

    uniform_9_000_000_quickhull_copy = list(uniform_9_000_000)
    start_time_uniform_quickhull = time()
    quickhull_performance(app, uniform_9_000_000_quickhull_copy)
    end_time_uniform_quickhull = time()
    time_uniform_quickhull_9_000_000 = end_time_uniform_quickhull - start_time_uniform_quickhull
    print("uniform_quickhull_9_000_000 ended!")
    del uniform_9_000_000_quickhull_copy
    gc.collect()

    return time_gaussian_quickhull_1_000_000, time_gaussian_quickhull_2_000_000, time_gaussian_quickhull_3_000_000, time_gaussian_quickhull_4_000_000, time_gaussian_quickhull_5_000_000, time_gaussian_quickhull_6_000_000, time_gaussian_quickhull_7_000_000, time_gaussian_quickhull_8_000_000, time_gaussian_quickhull_9_000_000, time_uniform_quickhull_1_000_000, time_uniform_quickhull_2_000_000, time_uniform_quickhull_3_000_000, time_uniform_quickhull_4_000_000, time_uniform_quickhull_5_000_000, time_uniform_quickhull_6_000_000, time_uniform_quickhull_7_000_000, time_uniform_quickhull_8_000_000, time_uniform_quickhull_9_000_000
