import math
from time import sleep, time
import gc

def jarvis_march_initial_call(ConvexHullVisualization, delay):
    points_copy = list(ConvexHullVisualization.points)
    if len(points_copy) < 3:
        return
    if ConvexHullVisualization.current_visualization_mode_index == 1:
        convex_hull = jarvis_march_without_delay(ConvexHullVisualization, points_copy)
    elif ConvexHullVisualization.current_visualization_mode_index == 2:
        convex_hull = jarvis_march_with_delay(ConvexHullVisualization, points_copy, delay)
    else:
        convex_hull = jarvis_march_performance(ConvexHullVisualization, points_copy)

    for point in convex_hull:
        print(point)
    print("############################################")

def jarvis_march_with_delay(ConvexHullVisualization, points_copy, delay):
    p_min_y = None
    if len(points_copy) < 3:
        return
    ConvexHullVisualization.clear_lines()
    p_min_y = min(points_copy, key=lambda p: (p[1], -p[0]))
    p_max_y = max(points_copy, key=lambda p: (p[1], -p[0]))
    current_point = p_min_y
    pos_x_axis_to_check = True
    prev_angle = 0
    prev_point = None
    convex_hull = []
    current_point_tag = "jarvis_march_current_point"
    next_point_tag = "jarvis_march_next_point"
    next_point_candidate_tag = "jarvis_march_next_point_candidate"
    while True:
        min_angle = 361
        next_point = None
        for point in points_copy:
            if point == current_point:
                continue
            angle = calculate_angle(current_point, point, pos_x_axis_to_check)
            next_point_candidate_canvas_x, next_point_candidate_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(point[0], point[1])
            ConvexHullVisualization.draw_circle(next_point_candidate_canvas_x, next_point_candidate_canvas_y, "next_point_candidate", next_point_candidate_tag)
            ConvexHullVisualization.root.update()
            sleep(delay)
            if angle <= min_angle and angle >= prev_angle:
                if min_angle != 361:
                    ConvexHullVisualization.canvas.delete(ConvexHullVisualization.lines.pop())
                    ConvexHullVisualization.canvas.delete(next_point_tag)
                min_angle = angle
                next_point = point
                next_point_canvas_x, next_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(next_point[0], next_point[1])
                current_point_canvas_x, current_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(current_point[0], current_point[1])
                ConvexHullVisualization.draw_circle(current_point_canvas_x, current_point_canvas_y, "current_point", current_point_tag)
                ConvexHullVisualization.draw_circle(next_point_canvas_x, next_point_canvas_y, "next_point", next_point_tag)
                ConvexHullVisualization.draw_line(current_point_canvas_x, current_point_canvas_y, next_point_canvas_x, next_point_canvas_y)
            ConvexHullVisualization.canvas.delete(next_point_candidate_tag)
            ConvexHullVisualization.root.update()
        if min_angle == prev_angle:
            convex_hull.remove(prev_point)
        convex_hull.append(current_point)
        prev_point = current_point
        prev_angle = min_angle
        current_point = next_point
        if current_point == p_max_y:
            pos_x_axis_to_check = False
            prev_angle = 0
        ConvexHullVisualization.canvas.delete(current_point_tag)
        ConvexHullVisualization.canvas.delete(next_point_tag)
        ConvexHullVisualization.canvas.delete(next_point_candidate_tag)
        ConvexHullVisualization.root.update()
        if current_point == p_min_y:
            break
        
    return convex_hull

def jarvis_march_without_delay(ConvexHullVisualization, points_copy):
    p_min_y = None
    if len(points_copy) < 3:
        return
    ConvexHullVisualization.clear_lines()
    p_min_y = min(points_copy, key=lambda p: (p[1], -p[0]))
    p_max_y = max(points_copy, key=lambda p: (p[1], -p[0]))
    current_point = p_min_y
    pos_x_axis_to_check = True
    prev_angle = 0
    prev_point = None
    convex_hull = []
    current_point_tag = "jarvis_march_current_point"
    next_point_tag = "jarvis_march_next_point"
    next_point_candidate_tag = "jarvis_march_next_point_candidate"
    while True:
        min_angle = 361
        next_point = None
        for point in points_copy:
            if point == current_point:
                continue
            angle = calculate_angle(current_point, point, pos_x_axis_to_check)
            next_point_candidate_canvas_x, next_point_candidate_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(point[0], point[1])
            ConvexHullVisualization.draw_circle(next_point_candidate_canvas_x, next_point_candidate_canvas_y, "next_point_candidate", next_point_candidate_tag)
            ConvexHullVisualization.root.update()
            if angle <= min_angle and angle >= prev_angle:
                if min_angle != 361:
                    ConvexHullVisualization.canvas.delete(ConvexHullVisualization.lines.pop())
                    ConvexHullVisualization.canvas.delete(next_point_tag)
                min_angle = angle
                next_point = point
                next_point_canvas_x, next_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(next_point[0], next_point[1])
                current_point_canvas_x, current_point_canvas_y = ConvexHullVisualization.calculate_canvas_coordinates(current_point[0], current_point[1])
                ConvexHullVisualization.draw_circle(current_point_canvas_x, current_point_canvas_y, "current_point", current_point_tag)
                ConvexHullVisualization.draw_circle(next_point_canvas_x, next_point_canvas_y, "next_point", next_point_tag)
                ConvexHullVisualization.draw_line(current_point_canvas_x, current_point_canvas_y, next_point_canvas_x, next_point_canvas_y)
            ConvexHullVisualization.canvas.delete(next_point_candidate_tag)
            ConvexHullVisualization.root.update()
        if min_angle == prev_angle:
            convex_hull.remove(prev_point)
        convex_hull.append(current_point)
        prev_point = current_point
        prev_angle = min_angle
        current_point = next_point
        if current_point == p_max_y:
            pos_x_axis_to_check = False
            prev_angle = 0
        ConvexHullVisualization.canvas.delete(current_point_tag)
        ConvexHullVisualization.canvas.delete(next_point_tag)
        ConvexHullVisualization.canvas.delete(next_point_candidate_tag)
        ConvexHullVisualization.root.update()
        if current_point == p_min_y:
            break
        
    return convex_hull

def jarvis_march_performance(ConvexHullVisualization, points_copy):
    p_min_y = None
    if len(points_copy) < 3:
        return

    p_min_y = min(points_copy, key=lambda p: (p[1], -p[0]))
    p_max_y = max(points_copy, key=lambda p: (p[1], -p[0]))
    current_point = p_min_y
    pos_x_axis_to_check = True
    prev_angle = 0
    prev_point = None
    convex_hull = []
    while True:
        min_angle = 361
        next_point = None
        for point in points_copy:
            if point == current_point:
                continue
            angle = calculate_angle(current_point, point, pos_x_axis_to_check)
            if angle <= min_angle and angle >= prev_angle:
                min_angle = angle
                next_point = point
        if min_angle == prev_angle:
            convex_hull.remove(prev_point)
        convex_hull.append(current_point)
        prev_point = current_point
        prev_angle = min_angle
        current_point = next_point
        if current_point == p_max_y:
            pos_x_axis_to_check = False
            prev_angle = 0
        if current_point == p_min_y:
            break
        
    return convex_hull

def calculate_angle(p1, p2, pos_x_axis_to_check):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if pos_x_axis_to_check:
        return math.degrees(math.atan2(dy, dx))
    else:
        return math.degrees(-math.atan2(dy, -dx))

def benchmark_thousands_jarvis_march(app,
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
    gaussian_1_000_jarvis_march_copy = list(gaussian_1_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_1_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_1_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_1_000 ended!")
    del gaussian_1_000_jarvis_march_copy
    gc.collect()

    gaussian_2_000_jarvis_march_copy = list(gaussian_2_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_2_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_2_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_2_000 ended!")
    del gaussian_2_000_jarvis_march_copy
    gc.collect()

    gaussian_3_000_jarvis_march_copy = list(gaussian_3_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_3_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_3_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_3_000 ended!")
    del gaussian_3_000_jarvis_march_copy
    gc.collect()

    gaussian_4_000_jarvis_march_copy = list(gaussian_4_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_4_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_4_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_4_000 ended!")
    del gaussian_4_000_jarvis_march_copy
    gc.collect()

    gaussian_5_000_jarvis_march_copy = list(gaussian_5_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_5_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_5_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_5_000 ended!")
    del gaussian_5_000_jarvis_march_copy
    gc.collect()

    gaussian_6_000_jarvis_march_copy = list(gaussian_6_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_6_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_6_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_6_000 ended!")
    del gaussian_6_000_jarvis_march_copy
    gc.collect()

    gaussian_7_000_jarvis_march_copy = list(gaussian_7_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_7_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_7_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_7_000 ended!")
    del gaussian_7_000_jarvis_march_copy
    gc.collect()

    gaussian_8_000_jarvis_march_copy = list(gaussian_8_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_8_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_8_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_8_000 ended!")
    del gaussian_8_000_jarvis_march_copy
    gc.collect()

    gaussian_9_000_jarvis_march_copy = list(gaussian_9_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_9_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_9_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_9_000 ended!")
    del gaussian_9_000_jarvis_march_copy
    gc.collect()

    uniform_1_000_jarvis_march_copy = list(uniform_1_000)
    start_time_uniform_jarvis_march= time()
    jarvis_march_performance(app, uniform_1_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_1_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_1_000 ended!")
    del uniform_1_000_jarvis_march_copy
    gc.collect()

    uniform_2_000_jarvis_march_copy = list(uniform_2_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_2_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_2_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_2_000 ended!")
    del uniform_2_000_jarvis_march_copy
    gc.collect()

    uniform_3_000_jarvis_march_copy = list(uniform_3_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_3_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_3_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_3_000 ended!")
    del uniform_3_000_jarvis_march_copy
    gc.collect()

    uniform_4_000_jarvis_march_copy = list(uniform_4_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_4_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_4_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_4_000 ended!")
    del uniform_4_000_jarvis_march_copy
    gc.collect()

    uniform_5_000_jarvis_march_copy = list(uniform_5_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_5_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_5_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_5_000 ended!")
    del uniform_5_000_jarvis_march_copy
    gc.collect()

    uniform_6_000_jarvis_march_copy = list(uniform_6_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_6_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_6_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_6_000 ended!")
    del uniform_6_000_jarvis_march_copy
    gc.collect()

    uniform_7_000_jarvis_march_copy = list(uniform_7_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_7_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_7_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_7_000 ended!")
    del uniform_7_000_jarvis_march_copy
    gc.collect()

    uniform_8_000_jarvis_march_copy = list(uniform_8_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_8_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_8_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_8_000 ended!")
    del uniform_8_000_jarvis_march_copy
    gc.collect()

    uniform_9_000_jarvis_march_copy = list(uniform_9_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_9_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_9_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_9_000 ended!")
    del uniform_9_000_jarvis_march_copy
    gc.collect()

    return time_gaussian_jarvis_march_1_000, time_gaussian_jarvis_march_2_000, time_gaussian_jarvis_march_3_000, time_gaussian_jarvis_march_4_000, time_gaussian_jarvis_march_5_000, time_gaussian_jarvis_march_6_000, time_gaussian_jarvis_march_7_000, time_gaussian_jarvis_march_8_000, time_gaussian_jarvis_march_9_000, time_uniform_jarvis_march_1_000, time_uniform_jarvis_march_2_000, time_uniform_jarvis_march_3_000, time_uniform_jarvis_march_4_000, time_uniform_jarvis_march_5_000, time_uniform_jarvis_march_6_000, time_uniform_jarvis_march_7_000, time_uniform_jarvis_march_8_000, time_uniform_jarvis_march_9_000

def benchmark_tens_of_thousands_jarvis_march(app,
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
    gaussian_10_000_jarvis_march_copy = list(gaussian_10_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_10_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_10_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_10_000 ended!")
    del gaussian_10_000_jarvis_march_copy
    gc.collect()

    gaussian_20_000_jarvis_march_copy = list(gaussian_20_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_20_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_20_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_20_000 ended!")
    del gaussian_20_000_jarvis_march_copy
    gc.collect()

    gaussian_30_000_jarvis_march_copy = list(gaussian_30_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_30_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_30_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_30_000 ended!")
    del gaussian_30_000_jarvis_march_copy
    gc.collect()

    gaussian_40_000_jarvis_march_copy = list(gaussian_40_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_40_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_40_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_40_000 ended!")
    del gaussian_40_000_jarvis_march_copy
    gc.collect()

    gaussian_50_000_jarvis_march_copy = list(gaussian_50_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_50_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_50_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_50_000 ended!")
    del gaussian_50_000_jarvis_march_copy
    gc.collect()

    gaussian_60_000_jarvis_march_copy = list(gaussian_60_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_60_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_60_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_60_000 ended!")
    del gaussian_60_000_jarvis_march_copy
    gc.collect()

    gaussian_70_000_jarvis_march_copy = list(gaussian_70_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_70_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_70_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_70_000 ended!")
    del gaussian_70_000_jarvis_march_copy
    gc.collect()

    gaussian_80_000_jarvis_march_copy = list(gaussian_80_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_80_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_80_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_80_000 ended!")
    del gaussian_80_000_jarvis_march_copy
    gc.collect()

    gaussian_90_000_jarvis_march_copy = list(gaussian_90_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_90_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_90_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_90_000 ended!")
    del gaussian_90_000_jarvis_march_copy
    gc.collect()

    uniform_10_000_jarvis_march_copy = list(uniform_10_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_10_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_10_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_10_000 ended!")
    del uniform_10_000_jarvis_march_copy
    gc.collect()

    uniform_20_000_jarvis_march_copy = list(uniform_20_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_20_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_20_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_20_000 ended!")
    del uniform_20_000_jarvis_march_copy
    gc.collect()

    uniform_30_000_jarvis_march_copy = list(uniform_30_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_30_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_30_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_30_000 ended!")
    del uniform_30_000_jarvis_march_copy
    gc.collect()

    uniform_40_000_jarvis_march_copy = list(uniform_40_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_40_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_40_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_40_000 ended!")
    del uniform_40_000_jarvis_march_copy
    gc.collect()

    uniform_50_000_jarvis_march_copy = list(uniform_50_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_50_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_50_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_50_000 ended!")
    del uniform_50_000_jarvis_march_copy
    gc.collect()

    uniform_60_000_jarvis_march_copy = list(uniform_60_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_60_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_60_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_60_000 ended!")
    del uniform_60_000_jarvis_march_copy
    gc.collect()

    uniform_70_000_jarvis_march_copy = list(uniform_70_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_70_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_70_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_70_000 ended!")
    del uniform_70_000_jarvis_march_copy
    gc.collect()

    uniform_80_000_jarvis_march_copy = list(uniform_80_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_80_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_80_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_80_000 ended!")
    del uniform_80_000_jarvis_march_copy
    gc.collect()

    uniform_90_000_jarvis_march_copy = list(uniform_90_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_90_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_90_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_90_000 ended!")
    del uniform_90_000_jarvis_march_copy
    gc.collect()

    return time_gaussian_jarvis_march_10_000, time_gaussian_jarvis_march_20_000, time_gaussian_jarvis_march_30_000, time_gaussian_jarvis_march_40_000, time_gaussian_jarvis_march_50_000, time_gaussian_jarvis_march_60_000, time_gaussian_jarvis_march_70_000, time_gaussian_jarvis_march_80_000, time_gaussian_jarvis_march_90_000, time_uniform_jarvis_march_10_000, time_uniform_jarvis_march_20_000, time_uniform_jarvis_march_30_000, time_uniform_jarvis_march_40_000, time_uniform_jarvis_march_50_000, time_uniform_jarvis_march_60_000, time_uniform_jarvis_march_70_000, time_uniform_jarvis_march_80_000, time_uniform_jarvis_march_90_000

def benchmark_hundreds_of_thousands_jarvis_march(app,
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
    gaussian_100_000_jarvis_march_copy = list(gaussian_100_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_100_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_100_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_100_000 ended!")
    del gaussian_100_000_jarvis_march_copy
    gc.collect()

    gaussian_200_000_jarvis_march_copy = list(gaussian_200_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_200_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_200_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_200_000 ended!")
    del gaussian_200_000_jarvis_march_copy
    gc.collect()

    gaussian_300_000_jarvis_march_copy = list(gaussian_300_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_300_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_300_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_300_000 ended!")
    del gaussian_300_000_jarvis_march_copy
    gc.collect()

    gaussian_400_000_jarvis_march_copy = list(gaussian_400_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_400_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_400_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_400_000 ended!")
    del gaussian_400_000_jarvis_march_copy
    gc.collect()

    gaussian_500_000_jarvis_march_copy = list(gaussian_500_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_500_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_500_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_500_000 ended!")
    del gaussian_500_000_jarvis_march_copy
    gc.collect()

    gaussian_600_000_jarvis_march_copy = list(gaussian_600_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_600_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_600_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_600_000 ended!")
    del gaussian_600_000_jarvis_march_copy
    gc.collect()

    gaussian_700_000_jarvis_march_copy = list(gaussian_700_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_700_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_700_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_700_000 ended!")
    del gaussian_700_000_jarvis_march_copy
    gc.collect()

    gaussian_800_000_jarvis_march_copy = list(gaussian_800_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_800_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_800_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_800_000 ended!")
    del gaussian_800_000_jarvis_march_copy
    gc.collect()

    gaussian_900_000_jarvis_march_copy = list(gaussian_900_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_900_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_900_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_900_000 ended!")
    del gaussian_900_000_jarvis_march_copy
    gc.collect()

    uniform_100_000_jarvis_march_copy = list(uniform_100_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_100_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_100_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_100_000 ended!")
    del uniform_100_000_jarvis_march_copy
    gc.collect()

    uniform_200_000_jarvis_march_copy = list(uniform_200_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_200_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_200_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_200_000 ended!")
    del uniform_200_000_jarvis_march_copy
    gc.collect()

    uniform_300_000_jarvis_march_copy = list(uniform_300_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_300_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_300_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_300_000 ended!")
    del uniform_300_000_jarvis_march_copy
    gc.collect()

    uniform_400_000_jarvis_march_copy = list(uniform_400_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_400_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_400_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_400_000 ended!")
    del uniform_400_000_jarvis_march_copy
    gc.collect()

    uniform_500_000_jarvis_march_copy = list(uniform_500_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_500_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_500_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_500_000 ended!")
    del uniform_500_000_jarvis_march_copy
    gc.collect()

    uniform_600_000_jarvis_march_copy = list(uniform_600_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_600_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_600_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_600_000 ended!")
    del uniform_600_000_jarvis_march_copy
    gc.collect()

    uniform_700_000_jarvis_march_copy = list(uniform_700_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_700_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_700_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_700_000 ended!")
    del uniform_700_000_jarvis_march_copy
    gc.collect()

    uniform_800_000_jarvis_march_copy = list(uniform_800_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_800_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_800_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_800_000 ended!")
    del uniform_800_000_jarvis_march_copy
    gc.collect()

    uniform_900_000_jarvis_march_copy = list(uniform_900_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_900_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_900_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_900_000 ended!")
    del uniform_900_000_jarvis_march_copy
    gc.collect()

    return time_gaussian_jarvis_march_100_000, time_gaussian_jarvis_march_200_000, time_gaussian_jarvis_march_300_000, time_gaussian_jarvis_march_400_000, time_gaussian_jarvis_march_500_000, time_gaussian_jarvis_march_600_000, time_gaussian_jarvis_march_700_000, time_gaussian_jarvis_march_800_000, time_gaussian_jarvis_march_900_000, time_uniform_jarvis_march_100_000, time_uniform_jarvis_march_200_000, time_uniform_jarvis_march_300_000, time_uniform_jarvis_march_400_000, time_uniform_jarvis_march_500_000, time_uniform_jarvis_march_600_000, time_uniform_jarvis_march_700_000, time_uniform_jarvis_march_800_000, time_uniform_jarvis_march_900_000

def benchmark_millions_jarvis_march(app,
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
    gaussian_1_000_000_jarvis_march_copy = list(gaussian_1_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_1_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_1_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_1_000_000 ended!")
    del gaussian_1_000_000_jarvis_march_copy
    gc.collect()

    gaussian_2_000_000_jarvis_march_copy = list(gaussian_2_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_2_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_2_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_2_000_000 ended!")
    del gaussian_2_000_000_jarvis_march_copy
    gc.collect()

    gaussian_3_000_000_jarvis_march_copy = list(gaussian_3_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_3_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_3_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_3_000_000 ended!")
    del gaussian_3_000_000_jarvis_march_copy
    gc.collect()

    gaussian_4_000_000_jarvis_march_copy = list(gaussian_4_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_4_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_4_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_4_000_000 ended!")
    del gaussian_4_000_000_jarvis_march_copy
    gc.collect()

    gaussian_5_000_000_jarvis_march_copy = list(gaussian_5_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_5_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_5_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_5_000_000 ended!")
    del gaussian_5_000_000_jarvis_march_copy
    gc.collect()

    gaussian_6_000_000_jarvis_march_copy = list(gaussian_6_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_6_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_6_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_6_000_000 ended!")
    del gaussian_6_000_000_jarvis_march_copy
    gc.collect()

    gaussian_7_000_000_jarvis_march_copy = list(gaussian_7_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_7_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_7_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_7_000_000 ended!")
    del gaussian_7_000_000_jarvis_march_copy
    gc.collect()

    gaussian_8_000_000_jarvis_march_copy = list(gaussian_8_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_8_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_8_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_8_000_000 ended!")
    del gaussian_8_000_000_jarvis_march_copy
    gc.collect()

    gaussian_9_000_000_jarvis_march_copy = list(gaussian_9_000_000)
    start_time_gaussian_jarvis_march = time()
    jarvis_march_performance(app, gaussian_9_000_000_jarvis_march_copy)
    end_time_gaussian_jarvis_march = time()
    time_gaussian_jarvis_march_9_000_000 = end_time_gaussian_jarvis_march - start_time_gaussian_jarvis_march
    print("gaussian_jarvis_march_9_000_000 ended!")
    del gaussian_9_000_000_jarvis_march_copy
    gc.collect()

    uniform_1_000_000_jarvis_march_copy = list(uniform_1_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_1_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_1_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_1_000_000 ended!")
    del uniform_1_000_000_jarvis_march_copy
    gc.collect()

    uniform_2_000_000_jarvis_march_copy = list(uniform_2_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_2_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_2_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_2_000_000 ended!")
    del uniform_2_000_000_jarvis_march_copy
    gc.collect()

    uniform_3_000_000_jarvis_march_copy = list(uniform_3_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_3_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_3_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_3_000_000 ended!")
    del uniform_3_000_000_jarvis_march_copy
    gc.collect()

    uniform_4_000_000_jarvis_march_copy = list(uniform_4_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_4_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_4_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_4_000_000 ended!")
    del uniform_4_000_000_jarvis_march_copy
    gc.collect()

    uniform_5_000_000_jarvis_march_copy = list(uniform_5_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_5_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_5_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_5_000_000 ended!")
    del uniform_5_000_000_jarvis_march_copy
    gc.collect()

    uniform_6_000_000_jarvis_march_copy = list(uniform_6_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_6_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_6_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_6_000_000 ended!")
    del uniform_6_000_000_jarvis_march_copy
    gc.collect()

    uniform_7_000_000_jarvis_march_copy = list(uniform_7_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_7_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_7_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_7_000_000 ended!")
    del uniform_7_000_000_jarvis_march_copy
    gc.collect()

    uniform_8_000_000_jarvis_march_copy = list(uniform_8_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_8_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_8_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_8_000_000 ended!")
    del uniform_8_000_000_jarvis_march_copy
    gc.collect()

    uniform_9_000_000_jarvis_march_copy = list(uniform_9_000_000)
    start_time_uniform_jarvis_march = time()
    jarvis_march_performance(app, uniform_9_000_000_jarvis_march_copy)
    end_time_uniform_jarvis_march = time()
    time_uniform_jarvis_march_9_000_000 = end_time_uniform_jarvis_march - start_time_uniform_jarvis_march
    print("uniform_jarvis_march_9_000_000 ended!")
    del uniform_9_000_000_jarvis_march_copy
    gc.collect()

    return time_gaussian_jarvis_march_1_000_000, time_gaussian_jarvis_march_2_000_000, time_gaussian_jarvis_march_3_000_000, time_gaussian_jarvis_march_4_000_000, time_gaussian_jarvis_march_5_000_000, time_gaussian_jarvis_march_6_000_000, time_gaussian_jarvis_march_7_000_000, time_gaussian_jarvis_march_8_000_000, time_gaussian_jarvis_march_9_000_000, time_uniform_jarvis_march_1_000_000, time_uniform_jarvis_march_2_000_000, time_uniform_jarvis_march_3_000_000, time_uniform_jarvis_march_4_000_000, time_uniform_jarvis_march_5_000_000, time_uniform_jarvis_march_6_000_000, time_uniform_jarvis_march_7_000_000, time_uniform_jarvis_march_8_000_000, time_uniform_jarvis_march_9_000_000
