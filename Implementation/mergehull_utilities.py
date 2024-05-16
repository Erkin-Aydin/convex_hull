from time import time
from grahams_scan_utilities import grahams_scan_performance, grahams_scan_with_delay, grahams_scan_without_delay
import math
import gc

def mergehull_initial_call(ConvexHullVisualization, delay):
    ConvexHullVisualization.clear_lines()
    points_copy = list(ConvexHullVisualization.points)
    lines_to_clear = []
    if len(points_copy) < 3:
        return
    if ConvexHullVisualization.current_visualization_mode_index == 1:
        convex_hull = mergehull_without_delay(ConvexHullVisualization, points_copy, lines_to_clear=lines_to_clear)
    elif ConvexHullVisualization.current_visualization_mode_index == 2:
        convex_hull = mergehull_with_delay(ConvexHullVisualization, points_copy, delay, lines_to_clear=lines_to_clear)
    else:
        convex_hull = mergehull_performance(ConvexHullVisualization, points_copy)

    print("printing convex hull:")
    for point in convex_hull:
        print(point)
    print("############################################")

def mergehull_with_delay(ConvexHullVisualization, points_copy, delay, lines_to_clear):
    length_points_copy = len(points_copy)
    if length_points_copy == 3:
        p1 = points_copy[0]
        p2 = points_copy[1]
        p3 = points_copy[2]
        p1_canvas_x, p1_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p1[0], p1[1])
        p2_canvas_x, p2_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p2[0], p2[1])
        p3_canvas_x, p3_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p3[0], p3[1])
        line1 = ConvexHullVisualization.draw_line(p1_canvas_x, p1_canvas_y, p2_canvas_x, p2_canvas_y)
        line2 = ConvexHullVisualization.draw_line(p2_canvas_x, p2_canvas_y, p3_canvas_x, p3_canvas_y)
        line3 = ConvexHullVisualization.draw_line(p3_canvas_x, p3_canvas_y, p1_canvas_x, p1_canvas_y)
        lines_to_clear.append(line1)
        lines_to_clear.append(line2)
        lines_to_clear.append(line3)
        ConvexHullVisualization.root.update()
    elif length_points_copy == 2:
        p1 = points_copy[0]
        p2 = points_copy[1]
        p1_canvas_x, p1_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p1[0], p1[1])
        p2_canvas_x, p2_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p2[0], p2[1])
        line = ConvexHullVisualization.draw_line(p1_canvas_x, p1_canvas_y, p2_canvas_x, p2_canvas_y)
        lines_to_clear.append(line)
        ConvexHullVisualization.root.update()
        return points_copy
    elif length_points_copy < 2:
        return points_copy
    
    # Sort the points based on x-coordinate

    # Find the midpoint
    midpoint_index = len(points_copy) // 2
    
    lines_to_clear_1 = []
    lines_to_clear_2 = []
    # Divide the sorted points into two partitions
    hull_1 = mergehull_with_delay(ConvexHullVisualization, points_copy[:midpoint_index], delay, lines_to_clear=lines_to_clear_1)
    hull_2 = mergehull_with_delay(ConvexHullVisualization, points_copy[midpoint_index:], delay, lines_to_clear=lines_to_clear_2)
    lines_to_clear_copy = lines_to_clear.copy()
    convex_hull = merge_with_delay(ConvexHullVisualization, hull_1, hull_2, delay, lines_to_clear=lines_to_clear)
    
    for line in lines_to_clear_1:
        ConvexHullVisualization.canvas.delete(line)
    for line in lines_to_clear_2:
        ConvexHullVisualization.canvas.delete(line)
    ConvexHullVisualization.root.update()
    
    return convex_hull

def mergehull_without_delay(ConvexHullVisualization, points_copy, lines_to_clear):
    length_points_copy = len(points_copy)
    if length_points_copy == 3:
        p1 = points_copy[0]
        p2 = points_copy[1]
        p3 = points_copy[2]
        p1_canvas_x, p1_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p1[0], p1[1])
        p2_canvas_x, p2_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p2[0], p2[1])
        p3_canvas_x, p3_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p3[0], p3[1])
        line1 = ConvexHullVisualization.draw_line(p1_canvas_x, p1_canvas_y, p2_canvas_x, p2_canvas_y)
        line2 = ConvexHullVisualization.draw_line(p2_canvas_x, p2_canvas_y, p3_canvas_x, p3_canvas_y)
        line3 = ConvexHullVisualization.draw_line(p3_canvas_x, p3_canvas_y, p1_canvas_x, p1_canvas_y)
        lines_to_clear.append(line1)
        lines_to_clear.append(line2)
        lines_to_clear.append(line3)
        ConvexHullVisualization.root.update()
    elif length_points_copy == 2:
        p1 = points_copy[0]
        p2 = points_copy[1]
        p1_canvas_x, p1_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p1[0], p1[1])
        p2_canvas_x, p2_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(p2[0], p2[1])
        line = ConvexHullVisualization.draw_line(p1_canvas_x, p1_canvas_y, p2_canvas_x, p2_canvas_y)
        lines_to_clear.append(line)
        ConvexHullVisualization.root.update()
        return points_copy
    elif length_points_copy < 2:
        return points_copy
    
    # Sort the points based on x-coordinate

    # Find the midpoint
    midpoint_index = len(points_copy) // 2
    lines_to_clear_1 = []
    lines_to_clear_2 = []
    hull_1 = mergehull_without_delay(ConvexHullVisualization, points_copy[:midpoint_index], lines_to_clear=lines_to_clear_1)
    hull_2 = mergehull_without_delay(ConvexHullVisualization, points_copy[midpoint_index:], lines_to_clear=lines_to_clear_2)
    convex_hull = merge_without_delay(ConvexHullVisualization, hull_1, hull_2, lines_to_clear=lines_to_clear)
    
    for line in lines_to_clear_1:
        ConvexHullVisualization.canvas.delete(line)
    for line in lines_to_clear_2:
        ConvexHullVisualization.canvas.delete(line)
    ConvexHullVisualization.root.update()
    
    return convex_hull

def mergehull_performance(ConvexHullVisualization, points_copy):
    
    if len(points_copy) < 4:
        return points_copy
    
    # Find the midpoint
    midpoint_index = len(points_copy) // 2
    
    # Divide the sorted points into two partitions
    hull_1 = mergehull_performance(ConvexHullVisualization, points_copy[:midpoint_index])
    hull_2 = mergehull_performance(ConvexHullVisualization, points_copy[midpoint_index:])
    convex_hull = merge_performance(ConvexHullVisualization, hull_1, hull_2)
    return convex_hull

def calculate_centroid(hull, length_hull):
        avg_x = sum(point[0] for point in hull) / length_hull
        avg_y = sum(point[1] for point in hull) / length_hull
        return avg_x, avg_y

def merge_with_delay(ConvexHullVisualization, hull_1, hull_2, delay, lines_to_clear):
    length_hull_1 = len(hull_1)

    centroid_point = ( ( hull_1[0][0] + hull_1[ int(length_hull_1 / 3)][0] + hull_1[ int(2 * length_hull_1 / 3)][0]) / 3, 
                      ( hull_1[0][1] + hull_1[ int(length_hull_1  / 3)][1] + hull_1[ int(2 * length_hull_1 / 3)][1]) / 3)

    centroid_in_hull = all(ConvexHullVisualization.is_not_right_turn(p1, p2, centroid_point) for p1, p2 in zip(hull_2, hull_2[1:] + [hull_2[0]]))

    merged_points = merge_hulls_all_sorted(hull_1, hull_2, centroid_point) if centroid_in_hull else merge_hulls_without_monotone_chain(hull_1, hull_2, centroid_point)

    return grahams_scan_with_delay(ConvexHullVisualization, merged_points, delay, clear_points=False, lines_to_clear=lines_to_clear)

def merge_performance(ConvexHullVisualization, hull_1, hull_2):
    length_hull_1 = len(hull_1)
    centroid_point = ( ( hull_1[0][0] + hull_1[ int(length_hull_1 / 3)][0] + hull_1[ int(2 * length_hull_1 / 3)][0]) / 3, 
                      ( hull_1[0][1] + hull_1[ int(length_hull_1  / 3)][1] + hull_1[ int(2 * length_hull_1 / 3)][1]) / 3)

    centroid_in_hull = is_internal_to_hull(ConvexHullVisualization, hull_2, centroid_point)
    
    merged_points = merge_hulls_all_sorted(hull_1, hull_2, centroid_point) if centroid_in_hull else merge_hulls_without_monotone_chain(hull_1, hull_2, centroid_point)

    return grahams_scan_performance(ConvexHullVisualization, merged_points)


def merge_without_delay(ConvexHullVisualization, hull_1, hull_2, lines_to_clear):
    
    length_hull_1 = len(hull_1)
    centroid_point = ( ( hull_1[0][0] + hull_1[ int(length_hull_1 / 3)][0] + hull_1[ int(2 * length_hull_1 / 3)][0]) / 3, 
                      ( hull_1[0][1] + hull_1[ int(length_hull_1  / 3)][1] + hull_1[ int(2 * length_hull_1 / 3)][1]) / 3)

    #centroid_in_hull = all(ConvexHullVisualization.is_not_right_turn(p1, p2, centroid_point) for p1, p2 in zip(hull_2, hull_2[1:] + [hull_2[0]]))
    centroid_in_hull = is_internal_to_hull(ConvexHullVisualization, hull_2, centroid_point)

    merged_points = merge_hulls_all_sorted(hull_1, hull_2, centroid_point) if centroid_in_hull else merge_hulls_without_monotone_chain(hull_1, hull_2, centroid_point)

    return grahams_scan_without_delay(ConvexHullVisualization, merged_points, clear_points=False, lines_to_clear=lines_to_clear)

def is_internal_to_hull(ConvexHullVisualization, hull_2, centroid_point):
    centroid_in_hull_2 = True
    length_hull_2 = len(hull_2)
    for i in range(length_hull_2):
        p1 = hull_2[i % length_hull_2]
        p2 = hull_2[(i + 1) % length_hull_2]
        if ConvexHullVisualization.is_right_turn(p1, p2, centroid_point):
            centroid_in_hull_2 = False
            break
    return centroid_in_hull_2

"""
def merge_hulls_all_sorted(hull_1, hull_2, centroid_point):
    def calculate_polar_angle_and_distance(p):
        dx, dy = p[0] - centroid_point[0], p[1] - centroid_point[1]
        polar_angle = math.atan2(dy, dx)
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return polar_angle, distance

    merged_hulls = hull_1 + hull_2
    merged_hulls = sorted(merged_hulls, key=lambda p: calculate_polar_angle_and_distance(p))

    return merged_hulls
"""
def merge_hulls_all_sorted(hull_1, hull_2, centroid_point):
    # Initialize pointers for hull_1 and hull_2
    pointer_hull_1 = 0
    pointer_hull_2 = 0

    # Calculate the number of points in hull_1 and hull_2
    len_hull_1 = len(hull_1)
    len_hull_2 = len(hull_2)

    # Initialize the merged hull
    merged_hulls = []

    # Iterate over both hulls
    while pointer_hull_1 < len_hull_1 and pointer_hull_2 < len_hull_2:
        # Calculate the polar angles of the current points in hull_1 and hull_2
        angle_hull_1 = math.atan2(hull_1[pointer_hull_1][1] - centroid_point[1],
                                   hull_1[pointer_hull_1][0] - centroid_point[0])
        angle_hull_2 = math.atan2(hull_2[pointer_hull_2][1] - centroid_point[1],
                                   hull_2[pointer_hull_2][0] - centroid_point[0])

        # Compare the polar angles
        if angle_hull_1 < angle_hull_2:
            merged_hulls.append(hull_1[pointer_hull_1])
            pointer_hull_1 += 1
        else:
            merged_hulls.append(hull_2[pointer_hull_2])
            pointer_hull_2 += 1

    """
    # Add remaining points from hull_1, if any
    while pointer_hull_1 < len_hull_1:
        merged_hulls.append(hull_1[pointer_hull_1])
        pointer_hull_1 += 1

    # Add remaining points from hull_2, if any
    while pointer_hull_2 < len_hull_2:
        merged_hulls.append(hull_2[pointer_hull_2])
        pointer_hull_2 += 1
    """
    # Add remaining points from hull_1 and hull_2, if any
    merged_hulls.extend(hull_1[pointer_hull_1:])
    merged_hulls.extend(hull_2[pointer_hull_2:])
    return merged_hulls


def merge_hulls_without_monotone_chain(hull_1, hull_2, centroid_point):
    monotone_chain = [point for point in hull_2 if point_in_polygon(point, hull_1)]
    remaining_points = [point for point in hull_2 if point not in monotone_chain]
    return merge_hulls_all_sorted(hull_1, remaining_points, centroid_point)



# THIS CODE HAS BEEN TAKEN AND MODIFIED FROM: https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
# Checking if a point is inside a polygon
def point_in_polygon(point, hull_1):
    num_vertices = len(hull_1)
    x, y = point[0], point[1]
    inside = False
 
    # Store the first point in the polygon and initialize the second point
    p1 = hull_1[0]
 
    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = hull_1[i % num_vertices]
 
        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p1[1], p2[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p1[1], p2[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p1[0], p2[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
 
                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside
 
        # Store the current point as the first point for the next iteration
        p1 = p2
 
    # Return the value of the inside flag
    return inside

def benchmark_thousands_mergehull(app,
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
    gaussian_1_000_mergehull_copy = list(gaussian_1_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_1_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_1_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_1_000 ended!")
    del gaussian_1_000_mergehull_copy
    gc.collect()

    gaussian_2_000_mergehull_copy = list(gaussian_2_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_2_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_2_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_2_000 ended!")
    del gaussian_2_000_mergehull_copy
    gc.collect()

    gaussian_3_000_mergehull_copy = list(gaussian_3_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_3_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_3_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_3_000 ended!")
    del gaussian_3_000_mergehull_copy
    gc.collect()

    gaussian_4_000_mergehull_copy = list(gaussian_4_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_4_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_4_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_4_000 ended!")
    del gaussian_4_000_mergehull_copy
    gc.collect()

    gaussian_5_000_mergehull_copy = list(gaussian_5_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_5_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_5_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_5_000 ended!")
    del gaussian_5_000_mergehull_copy
    gc.collect()

    gaussian_6_000_mergehull_copy = list(gaussian_6_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_6_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_6_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_6_000 ended!")
    del gaussian_6_000_mergehull_copy
    gc.collect()

    gaussian_7_000_mergehull_copy = list(gaussian_7_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_7_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_7_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_7_000 ended!")
    del gaussian_7_000_mergehull_copy
    gc.collect()

    gaussian_8_000_mergehull_copy = list(gaussian_8_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_8_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_8_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_8_000 ended!")
    del gaussian_8_000_mergehull_copy
    gc.collect()

    gaussian_9_000_mergehull_copy = list(gaussian_9_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_9_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_9_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_9_000 ended!")
    del gaussian_9_000_mergehull_copy
    gc.collect()

    uniform_1_000_mergehull_copy = list(uniform_1_000)
    start_time_uniform_mergehull= time()
    mergehull_performance(app, uniform_1_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_1_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_1_000 ended!")
    del uniform_1_000_mergehull_copy
    gc.collect()

    uniform_2_000_mergehull_copy = list(uniform_2_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_2_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_2_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_2_000 ended!")
    del uniform_2_000_mergehull_copy
    gc.collect()

    uniform_3_000_mergehull_copy = list(uniform_3_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_3_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_3_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_3_000 ended!")
    del uniform_3_000_mergehull_copy
    gc.collect()

    uniform_4_000_mergehull_copy = list(uniform_4_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_4_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_4_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_4_000 ended!")
    del uniform_4_000_mergehull_copy
    gc.collect()

    uniform_5_000_mergehull_copy = list(uniform_5_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_5_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_5_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_5_000 ended!")
    del uniform_5_000_mergehull_copy
    gc.collect()

    uniform_6_000_mergehull_copy = list(uniform_6_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_6_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_6_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_6_000 ended!")
    del uniform_6_000_mergehull_copy
    gc.collect()

    uniform_7_000_mergehull_copy = list(uniform_7_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_7_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_7_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_7_000 ended!")
    del uniform_7_000_mergehull_copy
    gc.collect()

    uniform_8_000_mergehull_copy = list(uniform_8_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_8_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_8_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_8_000 ended!")
    del uniform_8_000_mergehull_copy
    gc.collect()

    uniform_9_000_mergehull_copy = list(uniform_9_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_9_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_9_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_9_000 ended!")
    del uniform_9_000_mergehull_copy
    gc.collect()

    return time_gaussian_mergehull_1_000, time_gaussian_mergehull_2_000, time_gaussian_mergehull_3_000, time_gaussian_mergehull_4_000, time_gaussian_mergehull_5_000, time_gaussian_mergehull_6_000, time_gaussian_mergehull_7_000, time_gaussian_mergehull_8_000, time_gaussian_mergehull_9_000, time_uniform_mergehull_1_000, time_uniform_mergehull_2_000, time_uniform_mergehull_3_000, time_uniform_mergehull_4_000, time_uniform_mergehull_5_000, time_uniform_mergehull_6_000, time_uniform_mergehull_7_000, time_uniform_mergehull_8_000, time_uniform_mergehull_9_000

def benchmark_tens_of_thousands_mergehull(app,
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
    gaussian_10_000_mergehull_copy = list(gaussian_10_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_10_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_10_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_10_000 ended!")
    del gaussian_10_000_mergehull_copy
    gc.collect()

    gaussian_20_000_mergehull_copy = list(gaussian_20_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_20_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_20_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_20_000 ended!")
    del gaussian_20_000_mergehull_copy
    gc.collect()

    gaussian_30_000_mergehull_copy = list(gaussian_30_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_30_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_30_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_30_000 ended!")
    del gaussian_30_000_mergehull_copy
    gc.collect()

    gaussian_40_000_mergehull_copy = list(gaussian_40_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_40_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_40_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_40_000 ended!")
    del gaussian_40_000_mergehull_copy
    gc.collect()

    gaussian_50_000_mergehull_copy = list(gaussian_50_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_50_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_50_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_50_000 ended!")
    del gaussian_50_000_mergehull_copy
    gc.collect()

    gaussian_60_000_mergehull_copy = list(gaussian_60_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_60_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_60_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_60_000 ended!")
    del gaussian_60_000_mergehull_copy
    gc.collect()

    gaussian_70_000_mergehull_copy = list(gaussian_70_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_70_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_70_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_70_000 ended!")
    del gaussian_70_000_mergehull_copy
    gc.collect()

    gaussian_80_000_mergehull_copy = list(gaussian_80_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_80_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_80_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_80_000 ended!")
    del gaussian_80_000_mergehull_copy
    gc.collect()

    gaussian_90_000_mergehull_copy = list(gaussian_90_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_90_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_90_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_90_000 ended!")
    del gaussian_90_000_mergehull_copy
    gc.collect()

    uniform_10_000_mergehull_copy = list(uniform_10_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_10_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_10_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_10_000 ended!")
    del uniform_10_000_mergehull_copy
    gc.collect()

    uniform_20_000_mergehull_copy = list(uniform_20_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_20_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_20_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_20_000 ended!")
    del uniform_20_000_mergehull_copy
    gc.collect()

    uniform_30_000_mergehull_copy = list(uniform_30_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_30_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_30_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_30_000 ended!")
    del uniform_30_000_mergehull_copy
    gc.collect()

    uniform_40_000_mergehull_copy = list(uniform_40_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_40_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_40_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_40_000 ended!")
    del uniform_40_000_mergehull_copy
    gc.collect()

    uniform_50_000_mergehull_copy = list(uniform_50_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_50_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_50_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_50_000 ended!")
    del uniform_50_000_mergehull_copy
    gc.collect()

    uniform_60_000_mergehull_copy = list(uniform_60_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_60_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_60_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_60_000 ended!")
    del uniform_60_000_mergehull_copy
    gc.collect()

    uniform_70_000_mergehull_copy = list(uniform_70_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_70_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_70_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_70_000 ended!")
    del uniform_70_000_mergehull_copy
    gc.collect()

    uniform_80_000_mergehull_copy = list(uniform_80_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_80_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_80_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_80_000 ended!")
    del uniform_80_000_mergehull_copy
    gc.collect()

    uniform_90_000_mergehull_copy = list(uniform_90_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_90_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_90_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_90_000 ended!")
    del uniform_90_000_mergehull_copy
    gc.collect()

    return time_gaussian_mergehull_10_000, time_gaussian_mergehull_20_000, time_gaussian_mergehull_30_000, time_gaussian_mergehull_40_000, time_gaussian_mergehull_50_000, time_gaussian_mergehull_60_000, time_gaussian_mergehull_70_000, time_gaussian_mergehull_80_000, time_gaussian_mergehull_90_000, time_uniform_mergehull_10_000, time_uniform_mergehull_20_000, time_uniform_mergehull_30_000, time_uniform_mergehull_40_000, time_uniform_mergehull_50_000, time_uniform_mergehull_60_000, time_uniform_mergehull_70_000, time_uniform_mergehull_80_000, time_uniform_mergehull_90_000

def benchmark_hundreds_of_thousands_mergehull(app,
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
    gaussian_100_000_mergehull_copy = list(gaussian_100_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_100_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_100_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_100_000 ended!")
    del gaussian_100_000_mergehull_copy
    gc.collect()

    gaussian_200_000_mergehull_copy = list(gaussian_200_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_200_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_200_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_200_000 ended!")
    del gaussian_200_000_mergehull_copy
    gc.collect()

    gaussian_300_000_mergehull_copy = list(gaussian_300_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_300_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_300_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_300_000 ended!")
    del gaussian_300_000_mergehull_copy
    gc.collect()

    gaussian_400_000_mergehull_copy = list(gaussian_400_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_400_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_400_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_400_000 ended!")
    del gaussian_400_000_mergehull_copy
    gc.collect()

    gaussian_500_000_mergehull_copy = list(gaussian_500_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_500_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_500_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_500_000 ended!")
    del gaussian_500_000_mergehull_copy
    gc.collect()

    gaussian_600_000_mergehull_copy = list(gaussian_600_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_600_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_600_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_600_000 ended!")
    del gaussian_600_000_mergehull_copy
    gc.collect()

    gaussian_700_000_mergehull_copy = list(gaussian_700_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_700_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_700_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_700_000 ended!")
    del gaussian_700_000_mergehull_copy
    gc.collect()

    gaussian_800_000_mergehull_copy = list(gaussian_800_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_800_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_800_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_800_000 ended!")
    del gaussian_800_000_mergehull_copy
    gc.collect()

    gaussian_900_000_mergehull_copy = list(gaussian_900_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_900_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_900_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_900_000 ended!")
    del gaussian_900_000_mergehull_copy
    gc.collect()

    uniform_100_000_mergehull_copy = list(uniform_100_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_100_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_100_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_100_000 ended!")
    del uniform_100_000_mergehull_copy
    gc.collect()

    uniform_200_000_mergehull_copy = list(uniform_200_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_200_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_200_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_200_000 ended!")
    del uniform_200_000_mergehull_copy
    gc.collect()

    uniform_300_000_mergehull_copy = list(uniform_300_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_300_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_300_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_300_000 ended!")
    del uniform_300_000_mergehull_copy
    gc.collect()

    uniform_400_000_mergehull_copy = list(uniform_400_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_400_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_400_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_400_000 ended!")
    del uniform_400_000_mergehull_copy
    gc.collect()

    uniform_500_000_mergehull_copy = list(uniform_500_000)
    start_time_uniform_mergehull = time()

    mergehull_performance(app, uniform_500_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_500_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_500_000 ended!")
    del uniform_500_000_mergehull_copy
    gc.collect()

    uniform_600_000_mergehull_copy = list(uniform_600_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_600_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_600_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_600_000 ended!")
    del uniform_600_000_mergehull_copy
    gc.collect()

    uniform_700_000_mergehull_copy = list(uniform_700_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_700_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_700_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_700_000 ended!")
    del uniform_700_000_mergehull_copy
    gc.collect()

    uniform_800_000_mergehull_copy = list(uniform_800_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_800_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_800_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_800_000 ended!")
    del uniform_800_000_mergehull_copy
    gc.collect()

    uniform_900_000_mergehull_copy = list(uniform_900_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_900_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_900_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_900_000 ended!")
    del uniform_900_000_mergehull_copy
    gc.collect()

    return time_gaussian_mergehull_100_000, time_gaussian_mergehull_200_000, time_gaussian_mergehull_300_000, time_gaussian_mergehull_400_000, time_gaussian_mergehull_500_000, time_gaussian_mergehull_600_000, time_gaussian_mergehull_700_000, time_gaussian_mergehull_800_000, time_gaussian_mergehull_900_000, time_uniform_mergehull_100_000, time_uniform_mergehull_200_000, time_uniform_mergehull_300_000, time_uniform_mergehull_400_000, time_uniform_mergehull_500_000, time_uniform_mergehull_600_000, time_uniform_mergehull_700_000, time_uniform_mergehull_800_000, time_uniform_mergehull_900_000

def benchmark_millions_mergehull(app,
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
    gaussian_1_000_000_mergehull_copy = list(gaussian_1_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_1_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_1_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_1_000_000 ended!")
    del gaussian_1_000_000_mergehull_copy
    gc.collect()

    gaussian_2_000_000_mergehull_copy = list(gaussian_2_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_2_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_2_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_2_000_000 ended!")
    del gaussian_2_000_000_mergehull_copy
    gc.collect()

    gaussian_3_000_000_mergehull_copy = list(gaussian_3_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_3_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_3_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_3_000_000 ended!")
    del gaussian_3_000_000_mergehull_copy
    gc.collect()

    gaussian_4_000_000_mergehull_copy = list(gaussian_4_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_4_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_4_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_4_000_000 ended!")
    del gaussian_4_000_000_mergehull_copy
    gc.collect()

    gaussian_5_000_000_mergehull_copy = list(gaussian_5_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_5_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_5_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_5_000_000 ended!")
    del gaussian_5_000_000_mergehull_copy
    gc.collect()

    gaussian_6_000_000_mergehull_copy = list(gaussian_6_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_6_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_6_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_6_000_000 ended!")
    del gaussian_6_000_000_mergehull_copy
    gc.collect()

    gaussian_7_000_000_mergehull_copy = list(gaussian_7_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_7_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_7_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_7_000_000 ended!")
    del gaussian_7_000_000_mergehull_copy
    gc.collect()

    gaussian_8_000_000_mergehull_copy = list(gaussian_8_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_8_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_8_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_8_000_000 ended!")
    del gaussian_8_000_000_mergehull_copy
    gc.collect()

    gaussian_9_000_000_mergehull_copy = list(gaussian_9_000_000)
    start_time_gaussian_mergehull = time()
    mergehull_performance(app, gaussian_9_000_000_mergehull_copy)
    end_time_gaussian_mergehull = time()
    time_gaussian_mergehull_9_000_000 = end_time_gaussian_mergehull - start_time_gaussian_mergehull
    print("gaussian_mergehull_9_000_000 ended!")
    del gaussian_9_000_000_mergehull_copy
    gc.collect()

    uniform_1_000_000_mergehull_copy = list(uniform_1_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_1_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_1_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_1_000_000 ended!")
    del uniform_1_000_000_mergehull_copy
    gc.collect()

    uniform_2_000_000_mergehull_copy = list(uniform_2_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_2_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_2_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_2_000_000 ended!")
    del uniform_2_000_000_mergehull_copy
    gc.collect()

    uniform_3_000_000_mergehull_copy = list(uniform_3_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_3_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_3_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_3_000_000 ended!")
    del uniform_3_000_000_mergehull_copy
    gc.collect()

    uniform_4_000_000_mergehull_copy = list(uniform_4_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_4_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_4_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_4_000_000 ended!")
    del uniform_4_000_000_mergehull_copy
    gc.collect()

    uniform_5_000_000_mergehull_copy = list(uniform_5_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_5_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_5_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_5_000_000 ended!")
    del uniform_5_000_000_mergehull_copy
    gc.collect()

    uniform_6_000_000_mergehull_copy = list(uniform_6_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_6_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_6_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_6_000_000 ended!")
    del uniform_6_000_000_mergehull_copy
    gc.collect()

    uniform_7_000_000_mergehull_copy = list(uniform_7_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_7_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_7_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_7_000_000 ended!")
    del uniform_7_000_000_mergehull_copy
    gc.collect()

    uniform_8_000_000_mergehull_copy = list(uniform_8_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_8_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_8_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_8_000_000 ended!")
    del uniform_8_000_000_mergehull_copy
    gc.collect()

    uniform_9_000_000_mergehull_copy = list(uniform_9_000_000)
    start_time_uniform_mergehull = time()
    mergehull_performance(app, uniform_9_000_000_mergehull_copy)
    end_time_uniform_mergehull = time()
    time_uniform_mergehull_9_000_000 = end_time_uniform_mergehull - start_time_uniform_mergehull
    print("uniform_mergehull_9_000_000 ended!")
    del uniform_9_000_000_mergehull_copy
    gc.collect()

    return time_gaussian_mergehull_1_000_000, time_gaussian_mergehull_2_000_000, time_gaussian_mergehull_3_000_000, time_gaussian_mergehull_4_000_000, time_gaussian_mergehull_5_000_000, time_gaussian_mergehull_6_000_000, time_gaussian_mergehull_7_000_000, time_gaussian_mergehull_8_000_000, time_gaussian_mergehull_9_000_000, time_uniform_mergehull_1_000_000, time_uniform_mergehull_2_000_000, time_uniform_mergehull_3_000_000, time_uniform_mergehull_4_000_000, time_uniform_mergehull_5_000_000, time_uniform_mergehull_6_000_000, time_uniform_mergehull_7_000_000, time_uniform_mergehull_8_000_000, time_uniform_mergehull_9_000_000
