from time import time
from grahams_scan_utilities import grahams_scan_performance, benchmark_thousands_grahams_scan, benchmark_tens_of_thousands_grahams_scan, benchmark_hundreds_of_thousands_grahams_scan
from jarvis_march_utilities import jarvis_march_performance, benchmark_thousands_jarvis_march, benchmark_tens_of_thousands_jarvis_march, benchmark_hundreds_of_thousands_jarvis_march
from quickhull_utilities import quickhull_performance, benchmark_thousands_quickhull, benchmark_tens_of_thousands_quickhull, benchmark_hundreds_of_thousands_quickhull
from mergehull_utilities import mergehull_performance, benchmark_thousands_mergehull, benchmark_tens_of_thousands_mergehull, benchmark_hundreds_of_thousands_mergehull
import numpy as np
from app import ConvexHullVisualization
import gc

def benchmark():
    # Test the performance of the algorithms
    print("Benchmarking the performance of the algorithms...")
    print("############################################")

    covariance_1_000 = [[10000.0, 0.0],[0.0, 10000.0]]
    covariance_2_000 = [[20000.0, 0.0],[0.0, 20000.0]]
    covariance_3_000 = [[30000.0, 0.0],[0.0, 30000.0]]
    covariance_4_000 = [[40000.0, 0.0],[0.0, 40000.0]]
    covariance_5_000 = [[50000.0, 0.0],[0.0, 50000.0]]
    covariance_6_000 = [[60000.0, 0.0],[0.0, 60000.0]]
    covariance_7_000 = [[70000.0, 0.0],[0.0, 70000.0]]
    covariance_8_000 = [[80000.0, 0.0],[0.0, 80000.0]]
    covariance_9_000 = [[90000.0, 0.0],[0.0, 90000.0]]

    covariance_10_000 = [[100000.0, 0.0],[0.0, 100000.0]]
    covariance_20_000 = [[200000.0, 0.0],[0.0, 200000.0]]
    covariance_30_000 = [[300000.0, 0.0],[0.0, 300000.0]]
    covariance_40_000 = [[400000.0, 0.0],[0.0, 400000.0]]
    covariance_50_000 = [[500000.0, 0.0],[0.0, 500000.0]]
    covariance_60_000 = [[600000.0, 0.0],[0.0, 600000.0]]
    covariance_70_000 = [[700000.0, 0.0],[0.0, 700000.0]]
    covariance_80_000 = [[800000.0, 0.0],[0.0, 800000.0]]
    covariance_90_000 = [[900000.0, 0.0],[0.0, 900000.0]]


    covariance_100_000 = [[1000000.0, 0.0],[0.0, 1000000.0]]
    covariance_200_000 = [[2000000.0, 0.0],[0.0, 2000000.0]]
    covariance_300_000 = [[3000000.0, 0.0],[0.0, 3000000.0]]
    covariance_400_000 = [[4000000.0, 0.0],[0.0, 4000000.0]]
    covariance_500_000 = [[5000000.0, 0.0],[0.0, 5000000.0]]
    covariance_600_000 = [[6000000.0, 0.0],[0.0, 6000000.0]]
    covariance_700_000 = [[7000000.0, 0.0],[0.0, 7000000.0]]
    covariance_800_000 = [[8000000.0, 0.0],[0.0, 8000000.0]]
    covariance_900_000 = [[9000000.0, 0.0],[0.0, 9000000.0]]

    app = ConvexHullVisualization()

    
    gaussian_1_000 = generate_points_gaussian(1000, covariance_1_000)
    gaussian_2_000 = generate_points_gaussian(2000, covariance_2_000)
    gaussian_3_000 = generate_points_gaussian(3000, covariance_3_000)
    gaussian_4_000 = generate_points_gaussian(4000, covariance_4_000)
    gaussian_5_000 = generate_points_gaussian(5000, covariance_5_000)
    gaussian_6_000 = generate_points_gaussian(6000, covariance_6_000)
    gaussian_7_000 = generate_points_gaussian(7000, covariance_7_000)
    gaussian_8_000 = generate_points_gaussian(8000, covariance_8_000)
    gaussian_9_000 = generate_points_gaussian(9000, covariance_9_000)
    print("gaussian thousands created!")

    uniform_1_000 = generate_points_uniform(1000, 0, 1000, 0, 1000)
    uniform_2_000 = generate_points_uniform(2000, 0, 2000, 0, 2000)
    uniform_3_000 = generate_points_uniform(3000, 0, 3000, 0, 3000)
    uniform_4_000 = generate_points_uniform(4000, 0, 4000, 0, 4000)
    uniform_5_000 = generate_points_uniform(5000, 0, 5000, 0, 5000)
    uniform_6_000 = generate_points_uniform(6000, 0, 6000, 0, 6000)
    uniform_7_000 = generate_points_uniform(7000, 0, 7000, 0, 7000)
    uniform_8_000 = generate_points_uniform(8000, 0, 8000, 0, 8000)
    uniform_9_000 = generate_points_uniform(9000, 0, 9000, 0, 9000)
    print("uniform thousands created!")

    print("Benchmarking thousands...")
    gaussian_1_000_grahams_scan_time, gaussian_2_000_grahams_scan_time, gaussian_3_000_grahams_scan_time, gaussian_4_000_grahams_scan_time, gaussian_5_000_grahams_scan_time, gaussian_6_000_grahams_scan_time, gaussian_7_000_grahams_scan_time, gaussian_8_000_grahams_scan_time, gaussian_9_000_grahams_scan_time, uniform_1_000_grahams_scan_time, uniform_2_000_grahams_scan_time, uniform_3_000_grahams_scan_time, uniform_4_000_grahams_scan_time, uniform_5_000_grahams_scan_time, uniform_6_000_grahams_scan_time, uniform_7_000_grahams_scan_time, uniform_8_000_grahams_scan_time, uniform_9_000_grahams_scan_time = benchmark_thousands_grahams_scan(app, gaussian_1_000, gaussian_2_000, gaussian_3_000, gaussian_4_000, gaussian_5_000, gaussian_6_000, gaussian_7_000, gaussian_8_000, gaussian_9_000, uniform_1_000, uniform_2_000, uniform_3_000, uniform_4_000, uniform_5_000, uniform_6_000, uniform_7_000, uniform_8_000, uniform_9_000) 
    gaussian_1_000_jarvis_march_time, gaussian_2_000_jarvis_march_time, gaussian_3_000_jarvis_march_time, gaussian_4_000_jarvis_march_time, gaussian_5_000_jarvis_march_time, gaussian_6_000_jarvis_march_time, gaussian_7_000_jarvis_march_time, gaussian_8_000_jarvis_march_time, gaussian_9_000_jarvis_march_time, uniform_1_000_jarvis_march_time, uniform_2_000_jarvis_march_time, uniform_3_000_jarvis_march_time, uniform_4_000_jarvis_march_time, uniform_5_000_jarvis_march_time, uniform_6_000_jarvis_march_time, uniform_7_000_jarvis_march_time, uniform_8_000_jarvis_march_time, uniform_9_000_jarvis_march_time = benchmark_thousands_jarvis_march(app, gaussian_1_000, gaussian_2_000, gaussian_3_000, gaussian_4_000, gaussian_5_000, gaussian_6_000, gaussian_7_000, gaussian_8_000, gaussian_9_000, uniform_1_000, uniform_2_000, uniform_3_000, uniform_4_000, uniform_5_000, uniform_6_000, uniform_7_000, uniform_8_000, uniform_9_000)
    gaussian_1_000_quickhull_time, gaussian_2_000_quickhull_time, gaussian_3_000_quickhull_time, gaussian_4_000_quickhull_time, gaussian_5_000_quickhull_time, gaussian_6_000_quickhull_time, gaussian_7_000_quickhull_time, gaussian_8_000_quickhull_time, gaussian_9_000_quickhull_time, uniform_1_000_quickhull_time, uniform_2_000_quickhull_time, uniform_3_000_quickhull_time, uniform_4_000_quickhull_time, uniform_5_000_quickhull_time, uniform_6_000_quickhull_time, uniform_7_000_quickhull_time, uniform_8_000_quickhull_time, uniform_9_000_quickhull_time = benchmark_thousands_quickhull(app, gaussian_1_000, gaussian_2_000, gaussian_3_000, gaussian_4_000, gaussian_5_000, gaussian_6_000, gaussian_7_000, gaussian_8_000, gaussian_9_000, uniform_1_000, uniform_2_000, uniform_3_000, uniform_4_000, uniform_5_000, uniform_6_000, uniform_7_000, uniform_8_000, uniform_9_000)
    gaussian_1_000_mergehull_time, gaussian_2_000_mergehull_time, gaussian_3_000_mergehull_time, gaussian_4_000_mergehull_time, gaussian_5_000_mergehull_time, gaussian_6_000_mergehull_time, gaussian_7_000_mergehull_time, gaussian_8_000_mergehull_time, gaussian_9_000_mergehull_time, uniform_1_000_mergehull_time, uniform_2_000_mergehull_time, uniform_3_000_mergehull_time, uniform_4_000_mergehull_time, uniform_5_000_mergehull_time, uniform_6_000_mergehull_time, uniform_7_000_mergehull_time, uniform_8_000_mergehull_time, uniform_9_000_mergehull_time = benchmark_thousands_mergehull(app, gaussian_1_000, gaussian_2_000, gaussian_3_000, gaussian_4_000, gaussian_5_000, gaussian_6_000, gaussian_7_000, gaussian_8_000, gaussian_9_000, uniform_1_000, uniform_2_000, uniform_3_000, uniform_4_000, uniform_5_000, uniform_6_000, uniform_7_000, uniform_8_000, uniform_9_000)
    print("Thousands benchmarked!")
    del gaussian_1_000, gaussian_2_000, gaussian_3_000, gaussian_4_000, gaussian_5_000, gaussian_6_000, gaussian_7_000, gaussian_8_000, gaussian_9_000, uniform_1_000, uniform_2_000, uniform_3_000, uniform_4_000, uniform_5_000, uniform_6_000, uniform_7_000, uniform_8_000, uniform_9_000
    gc.collect()

    gaussian_10_000 = generate_points_gaussian(10000, covariance_10_000)
    gaussian_20_000 = generate_points_gaussian(20000, covariance_20_000)
    gaussian_30_000 = generate_points_gaussian(30000, covariance_30_000)
    gaussian_40_000 = generate_points_gaussian(40000, covariance_40_000)
    gaussian_50_000 = generate_points_gaussian(50000, covariance_50_000)
    gaussian_60_000 = generate_points_gaussian(60000, covariance_60_000)
    gaussian_70_000 = generate_points_gaussian(70000, covariance_70_000)
    gaussian_80_000 = generate_points_gaussian(80000, covariance_80_000)
    gaussian_90_000 = generate_points_gaussian(90000, covariance_90_000)
    print("gaussian tens of thousands created!")

    uniform_10_000 = generate_points_uniform(10000, 0, 10000, 0, 10000)
    uniform_20_000 = generate_points_uniform(20000, 0, 20000, 0, 20000)
    uniform_30_000 = generate_points_uniform(30000, 0, 30000, 0, 30000)
    uniform_40_000 = generate_points_uniform(40000, 0, 40000, 0, 40000)
    uniform_50_000 = generate_points_uniform(50000, 0, 50000, 0, 50000)
    uniform_60_000 = generate_points_uniform(60000, 0, 60000, 0, 60000)
    uniform_70_000 = generate_points_uniform(70000, 0, 70000, 0, 70000)
    uniform_80_000 = generate_points_uniform(80000, 0, 80000, 0, 80000)
    uniform_90_000 = generate_points_uniform(90000, 0, 90000, 0, 90000)
    print("uniform tens of thousands created!")

    print("Benchmarking tens of thousands...")
    gaussian_10_000_grahams_scan_time, gaussian_20_000_grahams_scan_time, gaussian_30_000_grahams_scan_time, gaussian_40_000_grahams_scan_time, gaussian_50_000_grahams_scan_time, gaussian_60_000_grahams_scan_time, gaussian_70_000_grahams_scan_time, gaussian_80_000_grahams_scan_time, gaussian_90_000_grahams_scan_time, uniform_10_000_grahams_scan_time, uniform_20_000_grahams_scan_time, uniform_30_000_grahams_scan_time, uniform_40_000_grahams_scan_time, uniform_50_000_grahams_scan_time, uniform_60_000_grahams_scan_time, uniform_70_000_grahams_scan_time, uniform_80_000_grahams_scan_time, uniform_90_000_grahams_scan_time = benchmark_tens_of_thousands_grahams_scan(app, gaussian_10_000, gaussian_20_000, gaussian_30_000, gaussian_40_000, gaussian_50_000, gaussian_60_000, gaussian_70_000, gaussian_80_000, gaussian_90_000, uniform_10_000, uniform_20_000, uniform_30_000, uniform_40_000, uniform_50_000, uniform_60_000, uniform_70_000, uniform_80_000, uniform_90_000)
    gaussian_10_000_jarvis_march_time, gaussian_20_000_jarvis_march_time, gaussian_30_000_jarvis_march_time, gaussian_40_000_jarvis_march_time, gaussian_50_000_jarvis_march_time, gaussian_60_000_jarvis_march_time, gaussian_70_000_jarvis_march_time, gaussian_80_000_jarvis_march_time, gaussian_90_000_jarvis_march_time, uniform_10_000_jarvis_march_time, uniform_20_000_jarvis_march_time, uniform_30_000_jarvis_march_time, uniform_40_000_jarvis_march_time, uniform_50_000_jarvis_march_time, uniform_60_000_jarvis_march_time, uniform_70_000_jarvis_march_time, uniform_80_000_jarvis_march_time, uniform_90_000_jarvis_march_time = benchmark_tens_of_thousands_jarvis_march(app, gaussian_10_000, gaussian_20_000, gaussian_30_000, gaussian_40_000, gaussian_50_000, gaussian_60_000, gaussian_70_000, gaussian_80_000, gaussian_90_000, uniform_10_000, uniform_20_000, uniform_30_000, uniform_40_000, uniform_50_000, uniform_60_000, uniform_70_000, uniform_80_000, uniform_90_000)
    gaussian_10_000_quickhull_time, gaussian_20_000_quickhull_time, gaussian_30_000_quickhull_time, gaussian_40_000_quickhull_time, gaussian_50_000_quickhull_time, gaussian_60_000_quickhull_time, gaussian_70_000_quickhull_time, gaussian_80_000_quickhull_time, gaussian_90_000_quickhull_time, uniform_10_000_quickhull_time, uniform_20_000_quickhull_time, uniform_30_000_quickhull_time, uniform_40_000_quickhull_time, uniform_50_000_quickhull_time, uniform_60_000_quickhull_time, uniform_70_000_quickhull_time, uniform_80_000_quickhull_time, uniform_90_000_quickhull_time = benchmark_tens_of_thousands_quickhull(app, gaussian_10_000, gaussian_20_000, gaussian_30_000, gaussian_40_000, gaussian_50_000, gaussian_60_000, gaussian_70_000, gaussian_80_000, gaussian_90_000, uniform_10_000, uniform_20_000, uniform_30_000, uniform_40_000, uniform_50_000, uniform_60_000, uniform_70_000, uniform_80_000, uniform_90_000)
    gaussian_10_000_mergehull_time, gaussian_20_000_mergehull_time, gaussian_30_000_mergehull_time, gaussian_40_000_mergehull_time, gaussian_50_000_mergehull_time, gaussian_60_000_mergehull_time, gaussian_70_000_mergehull_time, gaussian_80_000_mergehull_time, gaussian_90_000_mergehull_time, uniform_10_000_mergehull_time, uniform_20_000_mergehull_time, uniform_30_000_mergehull_time, uniform_40_000_mergehull_time, uniform_50_000_mergehull_time, uniform_60_000_mergehull_time, uniform_70_000_mergehull_time, uniform_80_000_mergehull_time, uniform_90_000_mergehull_time = benchmark_tens_of_thousands_mergehull(app, gaussian_10_000, gaussian_20_000, gaussian_30_000, gaussian_40_000, gaussian_50_000, gaussian_60_000, gaussian_70_000, gaussian_80_000, gaussian_90_000, uniform_10_000, uniform_20_000, uniform_30_000, uniform_40_000, uniform_50_000, uniform_60_000, uniform_70_000, uniform_80_000, uniform_90_000)
    print("Tens of thousands benchmarked!")
    del gaussian_10_000, gaussian_20_000, gaussian_30_000, gaussian_40_000, gaussian_50_000, gaussian_60_000, gaussian_70_000, gaussian_80_000, gaussian_90_000, uniform_10_000, uniform_20_000, uniform_30_000, uniform_40_000, uniform_50_000, uniform_60_000, uniform_70_000, uniform_80_000, uniform_90_000
    gc.collect()


    gaussian_100_000 = generate_points_gaussian(100000, covariance_100_000)
    gaussian_200_000 = generate_points_gaussian(200000, covariance_200_000)
    gaussian_300_000 = generate_points_gaussian(300000, covariance_300_000)
    gaussian_400_000 = generate_points_gaussian(400000, covariance_400_000)
    gaussian_500_000 = generate_points_gaussian(500000, covariance_500_000)
    gaussian_600_000 = generate_points_gaussian(600000, covariance_600_000)
    gaussian_700_000 = generate_points_gaussian(700000, covariance_700_000)
    gaussian_800_000 = generate_points_gaussian(800000, covariance_800_000)
    gaussian_900_000 = generate_points_gaussian(900000, covariance_900_000)
    print("gaussian hundreds of thousands created!")

    uniform_100_000 = generate_points_uniform(100000, 0, 100000, 0, 100000)
    uniform_200_000 = generate_points_uniform(200000, 0, 200000, 0, 200000)
    uniform_300_000 = generate_points_uniform(300000, 0, 300000, 0, 300000)
    uniform_400_000 = generate_points_uniform(400000, 0, 400000, 0, 400000)
    uniform_500_000 = generate_points_uniform(500000, 0, 500000, 0, 500000)
    uniform_600_000 = generate_points_uniform(600000, 0, 600000, 0, 600000)
    uniform_700_000 = generate_points_uniform(700000, 0, 700000, 0, 700000)
    uniform_800_000 = generate_points_uniform(800000, 0, 800000, 0, 800000)
    uniform_900_000 = generate_points_uniform(900000, 0, 900000, 0, 900000)
    print("uniform hundreds of thousands created!")

    print("Benchmarking hundreds of thousands...")
    gaussian_100_000_grahams_scan_time, gaussian_200_000_grahams_scan_time, gaussian_300_000_grahams_scan_time, gaussian_400_000_grahams_scan_time, gaussian_500_000_grahams_scan_time, gaussian_600_000_grahams_scan_time, gaussian_700_000_grahams_scan_time, gaussian_800_000_grahams_scan_time, gaussian_900_000_grahams_scan_time, uniform_100_000_grahams_scan_time, uniform_200_000_grahams_scan_time, uniform_300_000_grahams_scan_time, uniform_400_000_grahams_scan_time, uniform_500_000_grahams_scan_time, uniform_600_000_grahams_scan_time, uniform_700_000_grahams_scan_time, uniform_800_000_grahams_scan_time, uniform_900_000_grahams_scan_time = benchmark_hundreds_of_thousands_grahams_scan(app, gaussian_100_000, gaussian_200_000, gaussian_300_000, gaussian_400_000, gaussian_500_000, gaussian_600_000, gaussian_700_000, gaussian_800_000, gaussian_900_000, uniform_100_000, uniform_200_000, uniform_300_000, uniform_400_000, uniform_500_000, uniform_600_000, uniform_700_000, uniform_800_000, uniform_900_000)
    gaussian_100_000_jarvis_march_time, gaussian_200_000_jarvis_march_time, gaussian_300_000_jarvis_march_time, gaussian_400_000_jarvis_march_time, gaussian_500_000_jarvis_march_time, gaussian_600_000_jarvis_march_time, gaussian_700_000_jarvis_march_time, gaussian_800_000_jarvis_march_time, gaussian_900_000_jarvis_march_time, uniform_100_000_jarvis_march_time, uniform_200_000_jarvis_march_time, uniform_300_000_jarvis_march_time, uniform_400_000_jarvis_march_time, uniform_500_000_jarvis_march_time, uniform_600_000_jarvis_march_time, uniform_700_000_jarvis_march_time, uniform_800_000_jarvis_march_time, uniform_900_000_jarvis_march_time = benchmark_hundreds_of_thousands_jarvis_march(app, gaussian_100_000, gaussian_200_000, gaussian_300_000, gaussian_400_000, gaussian_500_000, gaussian_600_000, gaussian_700_000, gaussian_800_000, gaussian_900_000, uniform_100_000, uniform_200_000, uniform_300_000, uniform_400_000, uniform_500_000, uniform_600_000, uniform_700_000, uniform_800_000, uniform_900_000)
    gaussian_100_000_quickhull_time, gaussian_200_000_quickhull_time, gaussian_300_000_quickhull_time, gaussian_400_000_quickhull_time, gaussian_500_000_quickhull_time, gaussian_600_000_quickhull_time, gaussian_700_000_quickhull_time, gaussian_800_000_quickhull_time, gaussian_900_000_quickhull_time, uniform_100_000_quickhull_time, uniform_200_000_quickhull_time, uniform_300_000_quickhull_time, uniform_400_000_quickhull_time, uniform_500_000_quickhull_time, uniform_600_000_quickhull_time, uniform_700_000_quickhull_time, uniform_800_000_quickhull_time, uniform_900_000_quickhull_time = benchmark_hundreds_of_thousands_quickhull(app, gaussian_100_000, gaussian_200_000, gaussian_300_000, gaussian_400_000, gaussian_500_000, gaussian_600_000, gaussian_700_000, gaussian_800_000, gaussian_900_000, uniform_100_000, uniform_200_000, uniform_300_000, uniform_400_000, uniform_500_000, uniform_600_000, uniform_700_000, uniform_800_000, uniform_900_000)
    gaussian_100_000_mergehull_time, gaussian_200_000_mergehull_time, gaussian_300_000_mergehull_time, gaussian_400_000_mergehull_time, gaussian_500_000_mergehull_time, gaussian_600_000_mergehull_time, gaussian_700_000_mergehull_time, gaussian_800_000_mergehull_time, gaussian_900_000_mergehull_time, uniform_100_000_mergehull_time, uniform_200_000_mergehull_time, uniform_300_000_mergehull_time, uniform_400_000_mergehull_time, uniform_500_000_mergehull_time, uniform_600_000_mergehull_time, uniform_700_000_mergehull_time, uniform_800_000_mergehull_time, uniform_900_000_mergehull_time = benchmark_hundreds_of_thousands_mergehull(app, gaussian_100_000, gaussian_200_000, gaussian_300_000, gaussian_400_000, gaussian_500_000, gaussian_600_000, gaussian_700_000, gaussian_800_000, gaussian_900_000, uniform_100_000, uniform_200_000, uniform_300_000, uniform_400_000, uniform_500_000, uniform_600_000, uniform_700_000, uniform_800_000, uniform_900_000)
    print("Hundreds of thousands benchmarked!")
    del gaussian_100_000, gaussian_200_000, gaussian_300_000, gaussian_400_000, gaussian_500_000, gaussian_600_000, gaussian_700_000, gaussian_800_000, gaussian_900_000, uniform_100_000, uniform_200_000, uniform_300_000, uniform_400_000, uniform_500_000, uniform_600_000, uniform_700_000, uniform_800_000, uniform_900_000
    gc.collect()
    
    gaussian_grahams_scan_time_list, gaussian_jarvis_march_time_list, gaussian_quickhull_time_list, gaussian_mergehull_time_list, uniform_grahams_scan_time_list, uniform_jarvis_march_time_list, uniform_quickhull_time_list, uniform_mergehull_time_list = benchmark_millions(app)
    
    print("Final Results:")
    print("#############################################")
    print("#############################################")
    print("Gaussian:")
    print("###################################################")
    print("Graham's Scan:")
    
    print( gaussian_1_000_grahams_scan_time)
    print( gaussian_2_000_grahams_scan_time)
    print( gaussian_3_000_grahams_scan_time)
    print( gaussian_4_000_grahams_scan_time)
    print( gaussian_5_000_grahams_scan_time)
    print( gaussian_6_000_grahams_scan_time)
    print( gaussian_7_000_grahams_scan_time)
    print( gaussian_8_000_grahams_scan_time)
    print( gaussian_9_000_grahams_scan_time)
    print( gaussian_10_000_grahams_scan_time)
    print( gaussian_20_000_grahams_scan_time)
    print( gaussian_30_000_grahams_scan_time)
    print( gaussian_40_000_grahams_scan_time)
    print( gaussian_50_000_grahams_scan_time)
    print( gaussian_60_000_grahams_scan_time)
    print( gaussian_70_000_grahams_scan_time)
    print( gaussian_80_000_grahams_scan_time)
    print( gaussian_90_000_grahams_scan_time)
    print( gaussian_100_000_grahams_scan_time)
    print( gaussian_200_000_grahams_scan_time)
    print( gaussian_300_000_grahams_scan_time)
    print( gaussian_400_000_grahams_scan_time)
    print( gaussian_500_000_grahams_scan_time)
    print( gaussian_600_000_grahams_scan_time)
    print( gaussian_700_000_grahams_scan_time)
    print( gaussian_800_000_grahams_scan_time)
    print( gaussian_900_000_grahams_scan_time)
    
    print( gaussian_grahams_scan_time_list[0])
    print( gaussian_grahams_scan_time_list[1])
    print( gaussian_grahams_scan_time_list[2])
    print( gaussian_grahams_scan_time_list[3])
    print( gaussian_grahams_scan_time_list[4])
    print( gaussian_grahams_scan_time_list[5])
    print( gaussian_grahams_scan_time_list[6])
    print( gaussian_grahams_scan_time_list[7])
    print( gaussian_grahams_scan_time_list[8])
    print("###################################################")
    print("Jarvis' March:")
    
    print( gaussian_1_000_jarvis_march_time)
    print( gaussian_2_000_jarvis_march_time)
    print( gaussian_3_000_jarvis_march_time)
    print( gaussian_4_000_jarvis_march_time)
    print( gaussian_5_000_jarvis_march_time)
    print( gaussian_6_000_jarvis_march_time)
    print( gaussian_7_000_jarvis_march_time)
    print( gaussian_8_000_jarvis_march_time)
    print( gaussian_9_000_jarvis_march_time)
    print( gaussian_10_000_jarvis_march_time)
    print( gaussian_20_000_jarvis_march_time)
    print( gaussian_30_000_jarvis_march_time)
    print( gaussian_40_000_jarvis_march_time)
    print( gaussian_50_000_jarvis_march_time)
    print( gaussian_60_000_jarvis_march_time)
    print( gaussian_70_000_jarvis_march_time)
    print( gaussian_80_000_jarvis_march_time)
    print( gaussian_90_000_jarvis_march_time)
    print( gaussian_100_000_jarvis_march_time)
    print( gaussian_200_000_jarvis_march_time)
    print( gaussian_300_000_jarvis_march_time)
    print( gaussian_400_000_jarvis_march_time)
    print( gaussian_500_000_jarvis_march_time)
    print( gaussian_600_000_jarvis_march_time)
    print( gaussian_700_000_jarvis_march_time)
    print( gaussian_800_000_jarvis_march_time)
    print( gaussian_900_000_jarvis_march_time)
    
    print( gaussian_jarvis_march_time_list[0])
    print( gaussian_jarvis_march_time_list[1])
    print( gaussian_jarvis_march_time_list[2])
    print( gaussian_jarvis_march_time_list[3])
    print( gaussian_jarvis_march_time_list[4])
    print( gaussian_jarvis_march_time_list[5])
    print( gaussian_jarvis_march_time_list[6])
    print( gaussian_jarvis_march_time_list[7])
    print( gaussian_jarvis_march_time_list[8])
    print("###################################################")
    print("Quickhull:")
    
    print( gaussian_1_000_quickhull_time)
    print( gaussian_2_000_quickhull_time)
    print( gaussian_3_000_quickhull_time)
    print( gaussian_4_000_quickhull_time)
    print( gaussian_5_000_quickhull_time)
    print( gaussian_6_000_quickhull_time)
    print( gaussian_7_000_quickhull_time)
    print( gaussian_8_000_quickhull_time)
    print( gaussian_9_000_quickhull_time)
    print( gaussian_10_000_quickhull_time)
    print( gaussian_20_000_quickhull_time)
    print( gaussian_30_000_quickhull_time)
    print( gaussian_40_000_quickhull_time)
    print( gaussian_50_000_quickhull_time)
    print( gaussian_60_000_quickhull_time)
    print( gaussian_70_000_quickhull_time)
    print( gaussian_80_000_quickhull_time)
    print( gaussian_90_000_quickhull_time)
    print( gaussian_100_000_quickhull_time)
    print( gaussian_200_000_quickhull_time)
    print( gaussian_300_000_quickhull_time)
    print( gaussian_400_000_quickhull_time)
    print( gaussian_500_000_quickhull_time)
    print( gaussian_600_000_quickhull_time)
    print( gaussian_700_000_quickhull_time)
    print( gaussian_800_000_quickhull_time)
    print( gaussian_900_000_quickhull_time)
    
    print( gaussian_quickhull_time_list[0])
    print( gaussian_quickhull_time_list[1])
    print( gaussian_quickhull_time_list[2])
    print( gaussian_quickhull_time_list[3])
    print( gaussian_quickhull_time_list[4])
    print( gaussian_quickhull_time_list[5])
    print( gaussian_quickhull_time_list[6])
    print( gaussian_quickhull_time_list[7])
    print( gaussian_quickhull_time_list[8])
    print("###################################################")
    print("Mergehull:")
    
    print( gaussian_1_000_mergehull_time)
    print( gaussian_2_000_mergehull_time)
    print( gaussian_3_000_mergehull_time)
    print( gaussian_4_000_mergehull_time)
    print( gaussian_5_000_mergehull_time)
    print( gaussian_6_000_mergehull_time)
    print( gaussian_7_000_mergehull_time)
    print( gaussian_8_000_mergehull_time)
    print( gaussian_9_000_mergehull_time)
    print( gaussian_10_000_mergehull_time)
    print( gaussian_20_000_mergehull_time)
    print( gaussian_30_000_mergehull_time)
    print( gaussian_40_000_mergehull_time)
    print( gaussian_50_000_mergehull_time)
    print( gaussian_60_000_mergehull_time)
    print( gaussian_70_000_mergehull_time)
    print( gaussian_80_000_mergehull_time)
    print( gaussian_90_000_mergehull_time)
    print( gaussian_100_000_mergehull_time)
    print( gaussian_200_000_mergehull_time)
    print( gaussian_300_000_mergehull_time)
    print( gaussian_400_000_mergehull_time)
    print( gaussian_500_000_mergehull_time)
    print( gaussian_600_000_mergehull_time)
    print( gaussian_700_000_mergehull_time)
    print( gaussian_800_000_mergehull_time)
    print( gaussian_900_000_mergehull_time)
    
    print( gaussian_mergehull_time_list[0])
    print( gaussian_mergehull_time_list[1])
    print( gaussian_mergehull_time_list[2])
    print( gaussian_mergehull_time_list[3])
    print( gaussian_mergehull_time_list[4])
    print( gaussian_mergehull_time_list[5])
    print( gaussian_mergehull_time_list[6])
    print( gaussian_mergehull_time_list[7])
    print( gaussian_mergehull_time_list[8])
    print("###################################################")
    print("###################################################")
    print("Uniform:")
    print("###################################################")
    print("Graham's Scan:")
    
    print( uniform_1_000_grahams_scan_time)
    print( uniform_2_000_grahams_scan_time)
    print( uniform_3_000_grahams_scan_time)
    print( uniform_4_000_grahams_scan_time)
    print( uniform_5_000_grahams_scan_time)
    print( uniform_6_000_grahams_scan_time)
    print( uniform_7_000_grahams_scan_time)
    print( uniform_8_000_grahams_scan_time)
    print( uniform_9_000_grahams_scan_time)
    print( uniform_10_000_grahams_scan_time)
    print( uniform_20_000_grahams_scan_time)
    print( uniform_30_000_grahams_scan_time)
    print( uniform_40_000_grahams_scan_time)
    print( uniform_50_000_grahams_scan_time)
    print( uniform_60_000_grahams_scan_time)
    print( uniform_70_000_grahams_scan_time)
    print( uniform_80_000_grahams_scan_time)
    print( uniform_90_000_grahams_scan_time)
    print( uniform_100_000_grahams_scan_time)
    print( uniform_200_000_grahams_scan_time)
    print( uniform_300_000_grahams_scan_time)
    print( uniform_400_000_grahams_scan_time)
    print( uniform_500_000_grahams_scan_time)
    print( uniform_600_000_grahams_scan_time)
    print( uniform_700_000_grahams_scan_time)
    print( uniform_800_000_grahams_scan_time)
    print( uniform_900_000_grahams_scan_time)
    
    print( uniform_grahams_scan_time_list[0])
    print( uniform_grahams_scan_time_list[1])
    print( uniform_grahams_scan_time_list[2])
    print( uniform_grahams_scan_time_list[3])
    print( uniform_grahams_scan_time_list[4])
    print( uniform_grahams_scan_time_list[5])
    print( uniform_grahams_scan_time_list[6])
    print( uniform_grahams_scan_time_list[7])
    print( uniform_grahams_scan_time_list[8])
    print("###################################################")
    print("Jarvis' March:")
    
    print( uniform_1_000_jarvis_march_time)
    print( uniform_2_000_jarvis_march_time)
    print( uniform_3_000_jarvis_march_time)
    print( uniform_4_000_jarvis_march_time)
    print( uniform_5_000_jarvis_march_time)
    print( uniform_6_000_jarvis_march_time)
    print( uniform_7_000_jarvis_march_time)
    print( uniform_8_000_jarvis_march_time)
    print( uniform_9_000_jarvis_march_time)
    print( uniform_10_000_jarvis_march_time)
    print( uniform_20_000_jarvis_march_time)
    print( uniform_30_000_jarvis_march_time)
    print( uniform_40_000_jarvis_march_time)
    print( uniform_50_000_jarvis_march_time)
    print( uniform_60_000_jarvis_march_time)
    print( uniform_70_000_jarvis_march_time)
    print( uniform_80_000_jarvis_march_time)
    print( uniform_90_000_jarvis_march_time)
    print( uniform_100_000_jarvis_march_time)
    print( uniform_200_000_jarvis_march_time)
    print( uniform_300_000_jarvis_march_time)
    print( uniform_400_000_jarvis_march_time)
    print( uniform_500_000_jarvis_march_time)
    print( uniform_600_000_jarvis_march_time)
    print( uniform_700_000_jarvis_march_time)
    print( uniform_800_000_jarvis_march_time)
    print( uniform_900_000_jarvis_march_time)
    
    print( uniform_jarvis_march_time_list[0])
    print( uniform_jarvis_march_time_list[1])
    print( uniform_jarvis_march_time_list[2])
    print( uniform_jarvis_march_time_list[3])
    print( uniform_jarvis_march_time_list[4])
    print( uniform_jarvis_march_time_list[5])
    print( uniform_jarvis_march_time_list[6])
    print( uniform_jarvis_march_time_list[7])
    print( uniform_jarvis_march_time_list[8])
    print("###################################################")
    print("Quickhull:")
    
    print( uniform_1_000_quickhull_time)
    print( uniform_2_000_quickhull_time)
    print( uniform_3_000_quickhull_time)
    print( uniform_4_000_quickhull_time)
    print( uniform_5_000_quickhull_time)
    print( uniform_6_000_quickhull_time)
    print( uniform_7_000_quickhull_time)
    print( uniform_8_000_quickhull_time)
    print( uniform_9_000_quickhull_time)
    print( uniform_10_000_quickhull_time)
    print( uniform_20_000_quickhull_time)
    print( uniform_30_000_quickhull_time)
    print( uniform_40_000_quickhull_time)
    print( uniform_50_000_quickhull_time)
    print( uniform_60_000_quickhull_time)
    print( uniform_70_000_quickhull_time)
    print( uniform_80_000_quickhull_time)
    print( uniform_90_000_quickhull_time)
    print( uniform_100_000_quickhull_time)
    print( uniform_200_000_quickhull_time)
    print( uniform_300_000_quickhull_time)
    print( uniform_400_000_quickhull_time)
    print( uniform_500_000_quickhull_time)
    print( uniform_600_000_quickhull_time)
    print( uniform_700_000_quickhull_time)
    print( uniform_800_000_quickhull_time)
    print( uniform_900_000_quickhull_time)
    
    print( uniform_quickhull_time_list[0])
    print( uniform_quickhull_time_list[1])
    print( uniform_quickhull_time_list[2])
    print( uniform_quickhull_time_list[3])
    print( uniform_quickhull_time_list[4])
    print( uniform_quickhull_time_list[5])
    print( uniform_quickhull_time_list[6])
    print( uniform_quickhull_time_list[7])
    print( uniform_quickhull_time_list[8])
    print("###################################################")
    print("Mergehull:")
    
    print( uniform_1_000_mergehull_time)
    print( uniform_2_000_mergehull_time)
    print( uniform_3_000_mergehull_time)
    print( uniform_4_000_mergehull_time)
    print( uniform_5_000_mergehull_time)
    print( uniform_6_000_mergehull_time)
    print( uniform_7_000_mergehull_time)
    print( uniform_8_000_mergehull_time)
    print( uniform_9_000_mergehull_time)
    print( uniform_10_000_mergehull_time)
    print( uniform_20_000_mergehull_time)
    print( uniform_30_000_mergehull_time)
    print( uniform_40_000_mergehull_time)
    print( uniform_50_000_mergehull_time)
    print( uniform_60_000_mergehull_time)
    print( uniform_70_000_mergehull_time)
    print( uniform_80_000_mergehull_time)
    print( uniform_90_000_mergehull_time)
    print( uniform_100_000_mergehull_time)
    print( uniform_200_000_mergehull_time)
    print( uniform_300_000_mergehull_time)
    print( uniform_400_000_mergehull_time)
    print( uniform_500_000_mergehull_time)
    print( uniform_600_000_mergehull_time)
    print( uniform_700_000_mergehull_time)
    print( uniform_800_000_mergehull_time)
    print( uniform_900_000_mergehull_time)
    
    print( uniform_mergehull_time_list[0])
    print( uniform_mergehull_time_list[1])
    print( uniform_mergehull_time_list[2])
    print( uniform_mergehull_time_list[3])
    print( uniform_mergehull_time_list[4])
    print( uniform_mergehull_time_list[5])
    print( uniform_mergehull_time_list[6])
    print( uniform_mergehull_time_list[7])
    print( uniform_mergehull_time_list[8])
    print("###################################################")


def generate_points_gaussian(num_points, covariance_matrix):
    # Generate points using the specified parameters
    mean = [400, 400]  # Mean of the Gaussian distribution (center of the canvas)
    positions = np.random.multivariate_normal(mean, covariance_matrix, num_points)
    points = []
    for position in positions:
        x, y = position
        points.append((x, y))
    return points

def generate_points_uniform(num_points, min_x_value, max_x_value, min_y_value, max_y_value):
    xs = np.random.uniform(min_x_value, max_x_value, size=num_points)
    ys = np.random.uniform(min_y_value, max_y_value, size=num_points)
    positions = np.column_stack((xs, ys))
    
    points = []
    for position in positions:
        x, y = position
        points.append((x, y))
    return points

def benchmark_millions(app):

    covariance_1_000_000 = [[10000000.0, 0.0],[0.0, 10000000.0]]
    covariance_2_000_000 = [[20000000.0, 0.0],[0.0, 20000000.0]]
    covariance_3_000_000 = [[30000000.0, 0.0],[0.0, 30000000.0]]
    covariance_4_000_000 = [[40000000.0, 0.0],[0.0, 40000000.0]]
    covariance_5_000_000 = [[50000000.0, 0.0],[0.0, 50000000.0]]
    covariance_6_000_000 = [[60000000.0, 0.0],[0.0, 60000000.0]]
    covariance_7_000_000 = [[70000000.0, 0.0],[0.0, 70000000.0]]
    covariance_8_000_000 = [[80000000.0, 0.0],[0.0, 80000000.0]]
    covariance_9_000_000 = [[90000000.0, 0.0],[0.0, 90000000.0]]

    gaussian_grahams_scan_time_list = []
    gaussian_jarvis_march_time_list = []
    gaussian_quickhull_time_list = []
    gaussian_mergehull_time_list = []

    uniform_grahams_scan_time_list = []
    uniform_jarvis_march_time_list = []
    uniform_quickhull_time_list = []
    uniform_mergehull_time_list = []


    gaussian_1_000_000 = generate_points_gaussian(1000000, covariance_1_000_000)
    gaussian_1_000_000_grahams_scan_time, gaussian_1_000_000_jarvis_march_time, gaussian_1_000_000_quickhull_time, gaussian_1_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_1_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_1_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_1_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_1_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_1_000_000_mergehull_time)
    del gaussian_1_000_000
    gc.collect()

    gaussian_2_000_000 = generate_points_gaussian(2000000, covariance_2_000_000)
    gaussian_2_000_000_grahams_scan_time, gaussian_2_000_000_jarvis_march_time, gaussian_2_000_000_quickhull_time, gaussian_2_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_2_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_2_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_2_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_2_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_2_000_000_mergehull_time)
    del gaussian_2_000_000
    gc.collect()

    gaussian_3_000_000 = generate_points_gaussian(3000000, covariance_3_000_000)
    gaussian_3_000_000_grahams_scan_time, gaussian_3_000_000_jarvis_march_time, gaussian_3_000_000_quickhull_time, gaussian_3_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_3_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_3_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_3_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_3_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_3_000_000_mergehull_time)
    del gaussian_3_000_000
    gc.collect()


    gaussian_4_000_000 = generate_points_gaussian(4000000, covariance_4_000_000)
    gaussian_4_000_000_grahams_scan_time, gaussian_4_000_000_jarvis_march_time, gaussian_4_000_000_quickhull_time, gaussian_4_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_4_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_4_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_4_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_4_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_4_000_000_mergehull_time)
    del gaussian_4_000_000
    gc.collect()

    gaussian_5_000_000 = generate_points_gaussian(5000000, covariance_5_000_000)
    gaussian_5_000_000_grahams_scan_time, gaussian_5_000_000_jarvis_march_time, gaussian_5_000_000_quickhull_time, gaussian_5_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_5_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_5_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_5_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_5_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_5_000_000_mergehull_time)
    del gaussian_5_000_000
    gc.collect()

    gaussian_6_000_000 = generate_points_gaussian(6000000, covariance_6_000_000)
    gaussian_6_000_000_grahams_scan_time, gaussian_6_000_000_jarvis_march_time, gaussian_6_000_000_quickhull_time, gaussian_6_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_6_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_6_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_6_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_6_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_6_000_000_mergehull_time)
    del gaussian_6_000_000
    gc.collect()

    gaussian_7_000_000 = generate_points_gaussian(7000000, covariance_7_000_000)
    gaussian_7_000_000_grahams_scan_time, gaussian_7_000_000_jarvis_march_time, gaussian_7_000_000_quickhull_time, gaussian_7_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_7_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_7_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_7_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_7_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_7_000_000_mergehull_time)
    del gaussian_7_000_000
    gc.collect()

    gaussian_8_000_000 = generate_points_gaussian(8000000, covariance_8_000_000)
    gaussian_8_000_000_grahams_scan_time, gaussian_8_000_000_jarvis_march_time, gaussian_8_000_000_quickhull_time, gaussian_8_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_8_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_8_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_8_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_8_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_8_000_000_mergehull_time)
    del gaussian_8_000_000
    gc.collect()

    gaussian_9_000_000 = generate_points_gaussian(9000000, covariance_9_000_000)
    gaussian_9_000_000_grahams_scan_time, gaussian_9_000_000_jarvis_march_time, gaussian_9_000_000_quickhull_time, gaussian_9_000_000_mergehull_time = benchmark_algorithms_in_million(app, gaussian_9_000_000, True)
    gaussian_grahams_scan_time_list.append(gaussian_9_000_000_grahams_scan_time)
    gaussian_jarvis_march_time_list.append(gaussian_9_000_000_jarvis_march_time)
    gaussian_quickhull_time_list.append(gaussian_9_000_000_quickhull_time)
    gaussian_mergehull_time_list.append(gaussian_9_000_000_mergehull_time)
    del gaussian_9_000_000
    gc.collect()


    uniform_1_000_000 = generate_points_uniform(1000000, 0, 1000000, 0, 1000000)
    uniform_1_000_000_grahams_scan_time, uniform_1_000_000_jarvis_march_time, uniform_1_000_000_quickhull_time, uniform_1_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_1_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_1_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_1_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_1_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_1_000_000_mergehull_time)
    del uniform_1_000_000
    gc.collect()

    uniform_2_000_000 = generate_points_uniform(2000000, 0, 2000000, 0, 2000000)
    uniform_2_000_000_grahams_scan_time, uniform_2_000_000_jarvis_march_time, uniform_2_000_000_quickhull_time, uniform_2_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_2_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_2_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_2_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_2_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_2_000_000_mergehull_time)
    del uniform_2_000_000
    gc.collect()

    uniform_3_000_000 = generate_points_uniform(3000000, 0, 3000000, 0, 3000000)
    uniform_3_000_000_grahams_scan_time, uniform_3_000_000_jarvis_march_time, uniform_3_000_000_quickhull_time, uniform_3_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_3_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_3_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_3_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_3_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_3_000_000_mergehull_time)
    del uniform_3_000_000
    gc.collect()

    uniform_4_000_000 = generate_points_uniform(4000000, 0, 4000000, 0, 4000000)
    uniform_4_000_000_grahams_scan_time, uniform_4_000_000_jarvis_march_time, uniform_4_000_000_quickhull_time, uniform_4_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_4_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_4_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_4_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_4_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_4_000_000_mergehull_time)
    del uniform_4_000_000
    gc.collect()

    uniform_5_000_000 = generate_points_uniform(5000000, 0, 5000000, 0, 5000000)
    uniform_5_000_000_grahams_scan_time, uniform_5_000_000_jarvis_march_time, uniform_5_000_000_quickhull_time, uniform_5_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_5_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_5_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_5_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_5_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_5_000_000_mergehull_time)
    del uniform_5_000_000
    gc.collect()

    uniform_6_000_000 = generate_points_uniform(6000000, 0, 6000000, 0, 6000000)
    uniform_6_000_000_grahams_scan_time, uniform_6_000_000_jarvis_march_time, uniform_6_000_000_quickhull_time, uniform_6_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_6_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_6_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_6_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_6_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_6_000_000_mergehull_time)
    del uniform_6_000_000
    gc.collect()

    uniform_7_000_000 = generate_points_uniform(7000000, 0, 7000000, 0, 7000000)
    uniform_7_000_000_grahams_scan_time, uniform_7_000_000_jarvis_march_time, uniform_7_000_000_quickhull_time, uniform_7_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_7_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_7_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_7_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_7_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_7_000_000_mergehull_time)
    del uniform_7_000_000
    gc.collect()

    uniform_8_000_000 = generate_points_uniform(8000000, 0, 8000000, 0, 8000000)
    uniform_8_000_000_grahams_scan_time, uniform_8_000_000_jarvis_march_time, uniform_8_000_000_quickhull_time, uniform_8_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_8_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_8_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_8_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_8_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_8_000_000_mergehull_time)
    del uniform_8_000_000
    gc.collect()

    uniform_9_000_000 = generate_points_uniform(9000000, 0, 9000000, 0, 9000000)
    uniform_9_000_000_grahams_scan_time, uniform_9_000_000_jarvis_march_time, uniform_9_000_000_quickhull_time, uniform_9_000_000_mergehull_time = benchmark_algorithms_in_million(app, uniform_9_000_000, False)
    uniform_grahams_scan_time_list.append(uniform_9_000_000_grahams_scan_time)
    uniform_jarvis_march_time_list.append(uniform_9_000_000_jarvis_march_time)
    uniform_quickhull_time_list.append(uniform_9_000_000_quickhull_time)
    uniform_mergehull_time_list.append(uniform_9_000_000_mergehull_time)
    del uniform_9_000_000
    gc.collect()

    return gaussian_grahams_scan_time_list, gaussian_jarvis_march_time_list, gaussian_quickhull_time_list, gaussian_mergehull_time_list, uniform_grahams_scan_time_list, uniform_jarvis_march_time_list, uniform_quickhull_time_list, uniform_mergehull_time_list

def benchmark_algorithms_in_million(app, million_points, is_gaussian):
    
    length = len(million_points)
    
    grahams_scan_copy = list(million_points)
    start_time_grahams_scan = time()
    grahams_scan_performance(app, grahams_scan_copy)
    end_time_grahams_scan = time()
    time_grahams_scan = end_time_grahams_scan - start_time_grahams_scan
    if is_gaussian:
        print("gaussian_grahams_scan at following number of points ended: ", length)
    else:
        print("uniform_grahams_scan at following number of points ended: ", length)
    del grahams_scan_copy
    gc.collect()
    
    jarvis_march_copy = list(million_points)
    start_time_jarvis_march = time()
    jarvis_march_performance(app, jarvis_march_copy)
    end_time_jarvis_march = time()
    time_jarvis_march = end_time_jarvis_march - start_time_jarvis_march
    if is_gaussian:
        print("gaussian_jarvis_march at following number of points ended: ", length)
    else:
        print("uniform_jarvis_march at following number of points ended: ", length)
    del jarvis_march_copy
    gc.collect()
    
    quickhull_copy = list(million_points)
    start_time_quickhull = time()
    left = min(quickhull_copy, key=lambda p: (p[0], p[1]))
    right = (left[0], left[1] - 1e-9)
    quickhull_performance(app, quickhull_copy, left, right)
    end_time_quickhull = time()
    time_quickhull = end_time_quickhull - start_time_quickhull
    if is_gaussian:
        print("gaussian_quickhull at following number of points ended: ", length)
    else:
        print("uniform_quickhull at following number of points ended: ", length)
    del quickhull_copy
    gc.collect()
    
    mergehull_copy = list(million_points)
    start_time_mergehull = time()
    mergehull_performance(app, mergehull_copy)
    end_time_mergehull = time()
    time_mergehull = end_time_mergehull - start_time_mergehull
    if is_gaussian:
        print("gaussian_mergehull at following number of points ended: ", length)
    else:
        print("uniform_mergehull at following number of points ended: ", length)
    print("time: ", time_mergehull)
    del mergehull_copy
    gc.collect()
    
    return time_grahams_scan, time_jarvis_march, time_quickhull, time_mergehull


benchmark()