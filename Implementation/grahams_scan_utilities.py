from dlcl import DoublyLinkedList
from time import sleep, time
import gc

def grahams_scan_initial_call(ConvexHullVisualization, delay):
    points_copy = list(ConvexHullVisualization.points)
    if len(points_copy) < 3:
        return
    if ConvexHullVisualization.current_visualization_mode_index == 1:
        convex_hull = grahams_scan_without_delay(ConvexHullVisualization, points_copy, clear_points=True, lines_to_clear=[])
    elif ConvexHullVisualization.current_visualization_mode_index == 2:
        convex_hull = grahams_scan_with_delay(ConvexHullVisualization, points_copy, delay, clear_points=True, lines_to_clear=[])
    else:
        convex_hull = grahams_scan_performance(ConvexHullVisualization, points_copy)

    for point in convex_hull:
        print(point)
    print("############################################")

def grahams_scan_with_delay(ConvexHullVisualization, points_copy, delay, clear_points, lines_to_clear):

    if clear_points:
        ConvexHullVisualization.clear_lines()

    p_min_y = min(points_copy, key=lambda p: (p[1], p[0]))
    min_y = p_min_y[1]
    min_x = p_min_y[0]

    # Add min_x and min_y to each point's x and y coordinates
    for i, point in enumerate(points_copy):
        points_copy[i] = (point[0] - min_x, point[1] - min_y)

    # Sort points_copy using the custom sorting function
    points_copy.sort(key=lambda point: ConvexHullVisualization.sort_by_polar_angle_and_distance(point, 0.0, 0.0))
    sorted_dlcl = DoublyLinkedList()
    start = None
    for point in points_copy:
        sorted_dlcl.add_node(point)
        if point == (0, 0):
            start = sorted_dlcl.last
    v = start
    w = v.prev
    f = False
    while v.next != start or not f:
        v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
        v_next_x, v_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.point[0] + min_x, v.next.point[1] + min_y)
        v_next_next_x, v_next_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.next.point[0] + min_x, v.next.next.point[1] + min_y)
        v_tag = "grahams_scan_v"
        v_next_tag = "grahams_scan_v_next"
        v_next_next_tag = "grahams_scan_v_next_next"
        ConvexHullVisualization.draw_circle(v_x, v_y, "v", v_tag)
        ConvexHullVisualization.draw_circle(v_next_x, v_next_y, "v_next", v_next_tag)
        ConvexHullVisualization.draw_circle(v_next_next_x, v_next_next_y, "v_next_next", v_next_next_tag)
        
        if v.next == w:
            f = True
        if ConvexHullVisualization.is_left_turn(v.point, v.next.point, v.next.next.point):
            v = v.next
        else :
            line_to_delete = ConvexHullVisualization.lines.pop()
            ConvexHullVisualization.canvas.delete(line_to_delete)
            lines_to_clear.remove(line_to_delete)
            sorted_dlcl.delete_node(v.next)
            v = v.prev                
            ConvexHullVisualization.root.update()  # Update the canvas to show the line
            sleep(delay)  # Introduce a delay for visualization
            ConvexHullVisualization.canvas.delete(v_tag)
            ConvexHullVisualization.canvas.delete(v_next_tag)
            ConvexHullVisualization.canvas.delete(v_next_next_tag)
            continue

        v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
        v_prev_x, v_prev_y = ConvexHullVisualization.calculate_canvas_coordinates(v.prev.point[0] + min_x, v.prev.point[1] + min_y)
        
        # Visualize the decision point by drawing a line
        line = ConvexHullVisualization.draw_line(v_prev_x, v_prev_y, v_x, v_y)
        lines_to_clear.append(line)
        ConvexHullVisualization.root.update()  # Update the canvas to show the line
        sleep(delay)  # Introduce a delay for visualization
        
        ConvexHullVisualization.canvas.delete(v_tag)
        ConvexHullVisualization.canvas.delete(v_next_tag)
        ConvexHullVisualization.canvas.delete(v_next_next_tag)

    v_next_x, v_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.point[0] + min_x, v.next.point[1] + min_y)
    v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
    # Visualize the decision point by drawing a line
    line = ConvexHullVisualization.draw_line(v_next_x, v_next_y, v_x, v_y)
    lines_to_clear.append(line)
    ConvexHullVisualization.root.update()  # Update the canvas to show the line
    sleep(delay)  # Introduce a delay for visualization
    
    convex_hull = []
    convex_hull.append((start.point[0] + min_x, start.point[1] + min_y))
    v = start.next
    while v != start:
        convex_hull.append((v.point[0] + min_x, v.point[1] + min_y))
        v = v.next

    return convex_hull

def grahams_scan_without_delay(ConvexHullVisualization, points_copy, clear_points, lines_to_clear):

    if clear_points:
        ConvexHullVisualization.clear_lines()

    p_min_y = min(points_copy, key=lambda p: (p[1], p[0]))
    min_y = p_min_y[1]
    min_x = p_min_y[0]

    # Add min_x and min_y to each point's x and y coordinates
    for i, point in enumerate(points_copy):
        points_copy[i] = (point[0] - min_x, point[1] - min_y)

    # Sort points_copy using the custom sorting function
    points_copy.sort(key=lambda point: ConvexHullVisualization.sort_by_polar_angle_and_distance(point, 0.0, 0.0))
    sorted_dlcl = DoublyLinkedList()
    start = None
    for point in points_copy:
        sorted_dlcl.add_node(point)
        if point == (0, 0):
            start = sorted_dlcl.last
    v = start
    w = v.prev
    f = False
    while v.next != start or not f:
        
        v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
        v_next_x, v_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.point[0] + min_x, v.next.point[1] + min_y)
        v_next_next_x, v_next_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.next.point[0] + min_x, v.next.next.point[1] + min_y)
        v_tag = "grahams_scan_v"
        v_next_tag = "grahams_scan_v_next"
        v_next_next_tag = "grahams_scan_v_next_next"
        ConvexHullVisualization.draw_circle(v_x, v_y, "v", v_tag)
        ConvexHullVisualization.draw_circle(v_next_x, v_next_y, "v_next", v_next_tag)
        ConvexHullVisualization.draw_circle(v_next_next_x, v_next_next_y, "v_next_next", v_next_next_tag)
        
        if v.next == w:
            f = True
        if ConvexHullVisualization.is_left_turn(v.point, v.next.point, v.next.next.point):
            v = v.next
        else :
            line_to_delete = ConvexHullVisualization.lines.pop()
            ConvexHullVisualization.canvas.delete(line_to_delete)
            lines_to_clear.remove(line_to_delete)

            sorted_dlcl.delete_node(v.next)
            v = v.prev                
            ConvexHullVisualization.root.update()  # Update the canvas to show the line

            ConvexHullVisualization.canvas.delete(v_tag)
            ConvexHullVisualization.canvas.delete(v_next_tag)
            ConvexHullVisualization.canvas.delete(v_next_next_tag)
            continue

        v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
        v_prev_x, v_prev_y = ConvexHullVisualization.calculate_canvas_coordinates(v.prev.point[0] + min_x, v.prev.point[1] + min_y)
        
        # Visualize the decision point by drawing a line
        line = ConvexHullVisualization.draw_line(v_prev_x, v_prev_y, v_x, v_y)
        lines_to_clear.append(line)
        ConvexHullVisualization.root.update()  # Update the canvas to show the line
        
        ConvexHullVisualization.canvas.delete(v_tag)
        ConvexHullVisualization.canvas.delete(v_next_tag)
        ConvexHullVisualization.canvas.delete(v_next_next_tag)

    v_next_x, v_next_y = ConvexHullVisualization.calculate_canvas_coordinates(v.next.point[0] + min_x, v.next.point[1] + min_y)
    v_x, v_y = ConvexHullVisualization.calculate_canvas_coordinates(v.point[0] + min_x, v.point[1] + min_y)
    # Visualize the decision point by drawing a line
    line = ConvexHullVisualization.draw_line(v_next_x, v_next_y, v_x, v_y)
    lines_to_clear.append(line)

    convex_hull = []
    convex_hull.append((start.point[0] + min_x, start.point[1] + min_y))
    v = start.next
    while v != start:
        convex_hull.append((v.point[0] + min_x, v.point[1] + min_y))
        v = v.next

    return convex_hull

def grahams_scan_performance(ConvexHullVisualization, points_copy):

    p_min_y = min(points_copy, key=lambda p: (p[1], p[0]))
    min_y = p_min_y[1]
    min_x = p_min_y[0]

    # Add min_x and min_y to each point's x and y coordinates
    for i, point in enumerate(points_copy):
        points_copy[i] = (point[0] - min_x, point[1] - min_y)

    # Sort points_copy using the custom sorting function
    points_copy.sort(key=lambda point: ConvexHullVisualization.sort_by_polar_angle_and_distance(point, 0.0, 0.0))
    sorted_dlcl = DoublyLinkedList()
    start = None
    for point in points_copy:
        sorted_dlcl.add_node(point)
        if point == (0, 0):
            start = sorted_dlcl.last
    v = start
    w = v.prev
    f = False
    while v.next != start or not f:
        
        if v.next == w:
            f = True
        if ConvexHullVisualization.is_left_turn(v.point, v.next.point, v.next.next.point):
            v = v.next
        else :
            sorted_dlcl.delete_node(v.next)
            v = v.prev

    convex_hull = []
    convex_hull.append((start.point[0] + min_x, start.point[1] + min_y))
    v = start.next
    while v != start:
        convex_hull.append((v.point[0] + min_x, v.point[1] + min_y))
        v = v.next

    return convex_hull

def benchmark_thousands_grahams_scan(app,
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
    gaussian_1_000_grahams_scan_copy = list(gaussian_1_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_1_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_1_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_1_000 ended!")
    del gaussian_1_000_grahams_scan_copy
    gc.collect()

    gaussian_2_000_grahams_scan_copy = list(gaussian_2_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_2_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_2_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_2_000 ended!")
    del gaussian_2_000_grahams_scan_copy
    gc.collect()

    gaussian_3_000_grahams_scan_copy = list(gaussian_3_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_3_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_3_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_3_000 ended!")
    del gaussian_3_000_grahams_scan_copy
    gc.collect()

    gaussian_4_000_grahams_scan_copy = list(gaussian_4_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_4_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_4_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_4_000 ended!")
    del gaussian_4_000_grahams_scan_copy
    gc.collect()

    gaussian_5_000_grahams_scan_copy = list(gaussian_5_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_5_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_5_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_5_000 ended!")
    del gaussian_5_000_grahams_scan_copy
    gc.collect()

    gaussian_6_000_grahams_scan_copy = list(gaussian_6_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_6_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_6_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_6_000 ended!")
    del gaussian_6_000_grahams_scan_copy
    gc.collect()

    gaussian_7_000_grahams_scan_copy = list(gaussian_7_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_7_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_7_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_7_000 ended!")
    del gaussian_7_000_grahams_scan_copy
    gc.collect()

    gaussian_8_000_grahams_scan_copy = list(gaussian_8_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_8_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_8_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_8_000 ended!")
    del gaussian_8_000_grahams_scan_copy
    gc.collect()

    gaussian_9_000_grahams_scan_copy = list(gaussian_9_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_9_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_9_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_9_000 ended!")
    del gaussian_9_000_grahams_scan_copy
    gc.collect()

    uniform_1_000_grahams_scan_copy = list(uniform_1_000)
    start_time_uniform_grahams_scan= time()
    grahams_scan_performance(app, uniform_1_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_1_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_1_000 ended!")
    del uniform_1_000_grahams_scan_copy
    gc.collect()

    uniform_2_000_grahams_scan_copy = list(uniform_2_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_2_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_2_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_2_000 ended!")
    del uniform_2_000_grahams_scan_copy
    gc.collect()

    uniform_3_000_grahams_scan_copy = list(uniform_3_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_3_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_3_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_3_000 ended!")
    del uniform_3_000_grahams_scan_copy
    gc.collect()

    uniform_4_000_grahams_scan_copy = list(uniform_4_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_4_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_4_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_4_000 ended!")
    del uniform_4_000_grahams_scan_copy
    gc.collect()

    uniform_5_000_grahams_scan_copy = list(uniform_5_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_5_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_5_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_5_000 ended!")
    del uniform_5_000_grahams_scan_copy
    gc.collect()

    uniform_6_000_grahams_scan_copy = list(uniform_6_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_6_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_6_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_6_000 ended!")
    del uniform_6_000_grahams_scan_copy
    gc.collect()

    uniform_7_000_grahams_scan_copy = list(uniform_7_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_7_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_7_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_7_000 ended!")
    del uniform_7_000_grahams_scan_copy
    gc.collect()

    uniform_8_000_grahams_scan_copy = list(uniform_8_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_8_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_8_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_8_000 ended!")
    del uniform_8_000_grahams_scan_copy
    gc.collect()

    uniform_9_000_grahams_scan_copy = list(uniform_9_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_9_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_9_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_9_000 ended!")
    del uniform_9_000_grahams_scan_copy
    gc.collect()

    return time_gaussian_grahams_scan_1_000, time_gaussian_grahams_scan_2_000, time_gaussian_grahams_scan_3_000, time_gaussian_grahams_scan_4_000, time_gaussian_grahams_scan_5_000, time_gaussian_grahams_scan_6_000, time_gaussian_grahams_scan_7_000, time_gaussian_grahams_scan_8_000, time_gaussian_grahams_scan_9_000, time_uniform_grahams_scan_1_000, time_uniform_grahams_scan_2_000, time_uniform_grahams_scan_3_000, time_uniform_grahams_scan_4_000, time_uniform_grahams_scan_5_000, time_uniform_grahams_scan_6_000, time_uniform_grahams_scan_7_000, time_uniform_grahams_scan_8_000, time_uniform_grahams_scan_9_000

def benchmark_tens_of_thousands_grahams_scan(app,
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
    gaussian_10_000_grahams_scan_copy = list(gaussian_10_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_10_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_10_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_10_000 ended!")
    del gaussian_10_000_grahams_scan_copy
    gc.collect()

    gaussian_20_000_grahams_scan_copy = list(gaussian_20_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_20_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_20_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_20_000 ended!")
    del gaussian_20_000_grahams_scan_copy
    gc.collect()

    gaussian_30_000_grahams_scan_copy = list(gaussian_30_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_30_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_30_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_30_000 ended!")
    del gaussian_30_000_grahams_scan_copy
    gc.collect()

    gaussian_40_000_grahams_scan_copy = list(gaussian_40_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_40_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_40_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_40_000 ended!")
    del gaussian_40_000_grahams_scan_copy
    gc.collect()

    gaussian_50_000_grahams_scan_copy = list(gaussian_50_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_50_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_50_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_50_000 ended!")
    del gaussian_50_000_grahams_scan_copy
    gc.collect()

    gaussian_60_000_grahams_scan_copy = list(gaussian_60_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_60_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_60_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_60_000 ended!")
    del gaussian_60_000_grahams_scan_copy
    gc.collect()

    gaussian_70_000_grahams_scan_copy = list(gaussian_70_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_70_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_70_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_70_000 ended!")
    del gaussian_70_000_grahams_scan_copy
    gc.collect()

    gaussian_80_000_grahams_scan_copy = list(gaussian_80_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_80_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_80_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_80_000 ended!")
    del gaussian_80_000_grahams_scan_copy
    gc.collect()

    gaussian_90_000_grahams_scan_copy = list(gaussian_90_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_90_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_90_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_90_000 ended!")
    del gaussian_90_000_grahams_scan_copy
    gc.collect()

    uniform_10_000_grahams_scan_copy = list(uniform_10_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_10_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_10_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_10_000 ended!")
    del uniform_10_000_grahams_scan_copy
    gc.collect()

    uniform_20_000_grahams_scan_copy = list(uniform_20_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_20_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_20_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_20_000 ended!")
    del uniform_20_000_grahams_scan_copy
    gc.collect()

    uniform_30_000_grahams_scan_copy = list(uniform_30_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_30_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_30_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_30_000 ended!")
    del uniform_30_000_grahams_scan_copy
    gc.collect()

    uniform_40_000_grahams_scan_copy = list(uniform_40_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_40_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_40_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_40_000 ended!")
    del uniform_40_000_grahams_scan_copy
    gc.collect()

    uniform_50_000_grahams_scan_copy = list(uniform_50_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_50_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_50_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_50_000 ended!")
    del uniform_50_000_grahams_scan_copy
    gc.collect()

    uniform_60_000_grahams_scan_copy = list(uniform_60_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_60_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_60_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_60_000 ended!")
    del uniform_60_000_grahams_scan_copy
    gc.collect()

    uniform_70_000_grahams_scan_copy = list(uniform_70_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_70_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_70_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_70_000 ended!")
    del uniform_70_000_grahams_scan_copy
    gc.collect()

    uniform_80_000_grahams_scan_copy = list(uniform_80_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_80_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_80_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_80_000 ended!")
    del uniform_80_000_grahams_scan_copy
    gc.collect()

    uniform_90_000_grahams_scan_copy = list(uniform_90_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_90_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_90_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_90_000 ended!")
    del uniform_90_000_grahams_scan_copy
    gc.collect()

    return time_gaussian_grahams_scan_10_000, time_gaussian_grahams_scan_20_000, time_gaussian_grahams_scan_30_000, time_gaussian_grahams_scan_40_000, time_gaussian_grahams_scan_50_000, time_gaussian_grahams_scan_60_000, time_gaussian_grahams_scan_70_000, time_gaussian_grahams_scan_80_000, time_gaussian_grahams_scan_90_000, time_uniform_grahams_scan_10_000, time_uniform_grahams_scan_20_000, time_uniform_grahams_scan_30_000, time_uniform_grahams_scan_40_000, time_uniform_grahams_scan_50_000, time_uniform_grahams_scan_60_000, time_uniform_grahams_scan_70_000, time_uniform_grahams_scan_80_000, time_uniform_grahams_scan_90_000

def benchmark_hundreds_of_thousands_grahams_scan(app,
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
    gaussian_100_000_grahams_scan_copy = list(gaussian_100_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_100_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_100_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_100_000 ended!")
    del gaussian_100_000_grahams_scan_copy
    gc.collect()

    gaussian_200_000_grahams_scan_copy = list(gaussian_200_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_200_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_200_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_200_000 ended!")
    del gaussian_200_000_grahams_scan_copy
    gc.collect()

    gaussian_300_000_grahams_scan_copy = list(gaussian_300_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_300_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_300_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_300_000 ended!")
    del gaussian_300_000_grahams_scan_copy
    gc.collect()

    gaussian_400_000_grahams_scan_copy = list(gaussian_400_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_400_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_400_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_400_000 ended!")
    del gaussian_400_000_grahams_scan_copy
    gc.collect()

    gaussian_500_000_grahams_scan_copy = list(gaussian_500_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_500_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_500_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_500_000 ended!")
    del gaussian_500_000_grahams_scan_copy
    gc.collect()

    gaussian_600_000_grahams_scan_copy = list(gaussian_600_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_600_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_600_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_600_000 ended!")
    del gaussian_600_000_grahams_scan_copy
    gc.collect()

    gaussian_700_000_grahams_scan_copy = list(gaussian_700_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_700_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_700_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_700_000 ended!")
    del gaussian_700_000_grahams_scan_copy
    gc.collect()

    gaussian_800_000_grahams_scan_copy = list(gaussian_800_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_800_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_800_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_800_000 ended!")
    del gaussian_800_000_grahams_scan_copy
    gc.collect()

    gaussian_900_000_grahams_scan_copy = list(gaussian_900_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_900_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_900_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_900_000 ended!")
    del gaussian_900_000_grahams_scan_copy
    gc.collect()

    uniform_100_000_grahams_scan_copy = list(uniform_100_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_100_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_100_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_100_000 ended!")
    del uniform_100_000_grahams_scan_copy
    gc.collect()

    uniform_200_000_grahams_scan_copy = list(uniform_200_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_200_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_200_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_200_000 ended!")
    del uniform_200_000_grahams_scan_copy
    gc.collect()

    uniform_300_000_grahams_scan_copy = list(uniform_300_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_300_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_300_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_300_000 ended!")
    del uniform_300_000_grahams_scan_copy
    gc.collect()

    uniform_400_000_grahams_scan_copy = list(uniform_400_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_400_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_400_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_400_000 ended!")
    del uniform_400_000_grahams_scan_copy
    gc.collect()

    uniform_500_000_grahams_scan_copy = list(uniform_500_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_500_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_500_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_500_000 ended!")
    del uniform_500_000_grahams_scan_copy
    gc.collect()

    uniform_600_000_grahams_scan_copy = list(uniform_600_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_600_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_600_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_600_000 ended!")
    del uniform_600_000_grahams_scan_copy
    gc.collect()

    uniform_700_000_grahams_scan_copy = list(uniform_700_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_700_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_700_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_700_000 ended!")
    del uniform_700_000_grahams_scan_copy
    gc.collect()

    uniform_800_000_grahams_scan_copy = list(uniform_800_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_800_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_800_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_800_000 ended!")
    del uniform_800_000_grahams_scan_copy
    gc.collect()

    uniform_900_000_grahams_scan_copy = list(uniform_900_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_900_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_900_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_900_000 ended!")
    del uniform_900_000_grahams_scan_copy
    gc.collect()

    return time_gaussian_grahams_scan_100_000, time_gaussian_grahams_scan_200_000, time_gaussian_grahams_scan_300_000, time_gaussian_grahams_scan_400_000, time_gaussian_grahams_scan_500_000, time_gaussian_grahams_scan_600_000, time_gaussian_grahams_scan_700_000, time_gaussian_grahams_scan_800_000, time_gaussian_grahams_scan_900_000, time_uniform_grahams_scan_100_000, time_uniform_grahams_scan_200_000, time_uniform_grahams_scan_300_000, time_uniform_grahams_scan_400_000, time_uniform_grahams_scan_500_000, time_uniform_grahams_scan_600_000, time_uniform_grahams_scan_700_000, time_uniform_grahams_scan_800_000, time_uniform_grahams_scan_900_000

def benchmark_millions_grahams_scan(app,
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
    gaussian_1_000_000_grahams_scan_copy = list(gaussian_1_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_1_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_1_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_1_000_000 ended!")
    del gaussian_1_000_000_grahams_scan_copy
    gc.collect()

    gaussian_2_000_000_grahams_scan_copy = list(gaussian_2_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_2_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_2_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_2_000_000 ended!")
    del gaussian_2_000_000_grahams_scan_copy
    gc.collect()

    gaussian_3_000_000_grahams_scan_copy = list(gaussian_3_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_3_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_3_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_3_000_000 ended!")
    del gaussian_3_000_000_grahams_scan_copy
    gc.collect()

    gaussian_4_000_000_grahams_scan_copy = list(gaussian_4_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_4_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_4_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_4_000_000 ended!")
    del gaussian_4_000_000_grahams_scan_copy
    gc.collect()

    gaussian_5_000_000_grahams_scan_copy = list(gaussian_5_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_5_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_5_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_5_000_000 ended!")
    del gaussian_5_000_000_grahams_scan_copy
    gc.collect()

    gaussian_6_000_000_grahams_scan_copy = list(gaussian_6_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_6_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_6_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_6_000_000 ended!")
    del gaussian_6_000_000_grahams_scan_copy
    gc.collect()

    gaussian_7_000_000_grahams_scan_copy = list(gaussian_7_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_7_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_7_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_7_000_000 ended!")
    del gaussian_7_000_000_grahams_scan_copy
    gc.collect()

    gaussian_8_000_000_grahams_scan_copy = list(gaussian_8_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_8_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_8_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_8_000_000 ended!")
    del gaussian_8_000_000_grahams_scan_copy
    gc.collect()

    gaussian_9_000_000_grahams_scan_copy = list(gaussian_9_000_000)
    start_time_gaussian_grahams_scan = time()
    grahams_scan_performance(app, gaussian_9_000_000_grahams_scan_copy)
    end_time_gaussian_grahams_scan = time()
    time_gaussian_grahams_scan_9_000_000 = end_time_gaussian_grahams_scan - start_time_gaussian_grahams_scan
    print("gaussian_grahams_scan_9_000_000 ended!")
    del gaussian_9_000_000_grahams_scan_copy
    gc.collect()

    uniform_1_000_000_grahams_scan_copy = list(uniform_1_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_1_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_1_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_1_000_000 ended!")
    del uniform_1_000_000_grahams_scan_copy
    gc.collect()

    uniform_2_000_000_grahams_scan_copy = list(uniform_2_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_2_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_2_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_2_000_000 ended!")
    del uniform_2_000_000_grahams_scan_copy
    gc.collect()

    uniform_3_000_000_grahams_scan_copy = list(uniform_3_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_3_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_3_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_3_000_000 ended!")
    del uniform_3_000_000_grahams_scan_copy
    gc.collect()

    uniform_4_000_000_grahams_scan_copy = list(uniform_4_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_4_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_4_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_4_000_000 ended!")
    del uniform_4_000_000_grahams_scan_copy
    gc.collect()

    uniform_5_000_000_grahams_scan_copy = list(uniform_5_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_5_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_5_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_5_000_000 ended!")
    del uniform_5_000_000_grahams_scan_copy
    gc.collect()

    uniform_6_000_000_grahams_scan_copy = list(uniform_6_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_6_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_6_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_6_000_000 ended!")
    del uniform_6_000_000_grahams_scan_copy
    gc.collect()

    uniform_7_000_000_grahams_scan_copy = list(uniform_7_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_7_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_7_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_7_000_000 ended!")
    del uniform_7_000_000_grahams_scan_copy
    gc.collect()

    uniform_8_000_000_grahams_scan_copy = list(uniform_8_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_8_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_8_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_8_000_000 ended!")
    del uniform_8_000_000_grahams_scan_copy
    gc.collect()

    uniform_9_000_000_grahams_scan_copy = list(uniform_9_000_000)
    start_time_uniform_grahams_scan = time()
    grahams_scan_performance(app, uniform_9_000_000_grahams_scan_copy)
    end_time_uniform_grahams_scan = time()
    time_uniform_grahams_scan_9_000_000 = end_time_uniform_grahams_scan - start_time_uniform_grahams_scan
    print("uniform_grahams_scan_9_000_000 ended!")
    del uniform_9_000_000_grahams_scan_copy
    gc.collect()

    return time_gaussian_grahams_scan_1_000_000, time_gaussian_grahams_scan_2_000_000, time_gaussian_grahams_scan_3_000_000, time_gaussian_grahams_scan_4_000_000, time_gaussian_grahams_scan_5_000_000, time_gaussian_grahams_scan_6_000_000, time_gaussian_grahams_scan_7_000_000, time_gaussian_grahams_scan_8_000_000, time_gaussian_grahams_scan_9_000_000, time_uniform_grahams_scan_1_000_000, time_uniform_grahams_scan_2_000_000, time_uniform_grahams_scan_3_000_000, time_uniform_grahams_scan_4_000_000, time_uniform_grahams_scan_5_000_000, time_uniform_grahams_scan_6_000_000, time_uniform_grahams_scan_7_000_000, time_uniform_grahams_scan_8_000_000, time_uniform_grahams_scan_9_000_000
