## Installation Details

It is suggested to use a python environment to install the modules used in this project.
I chose to use a conda environment. After setting up miniconda or Anaconda on you machine,
you can construct the conda environment as follows:

conda create --name erkin_aydin_2d_convex_hull python=3.12.2

Then you can activate this conda environment as follows:

conda activate erkin_aydin_2d_convex_hull

The only external module you need to install is numpy. You can install it as follows:

conda install numpy

## How to run

You can run the application as follows: python app.py
You can run the benchmarks as follows: python benchmark.py
Closing the opened canvas will automatically start benchmarking process.

## User Interface

There are certain details needed to be mentioned about this application implementation:

    • Y-axis is flipped in tkinter.canvas. Therefore, algorithms may look like being executed in reverse order.
    For instance, where Jarvis March is marching up it will look like it is marching down.

    • For visualization purposes, a scale factor has been implemented for zooming in and out to the canvas.
    Using this scale factor, the points are relocated into the limited screen space of the canvas based on to which point we zoom in and out.
    The sizes of the points are also managed using this scale factor.

    • tkinter.canvas provides coordinates for the mouse traveling on the canvas taking the top left corner of the canvas as the origin,
    however this does not match the real coordinates in the coordinate system since we zoom in and out to canvas.
    Therefore, a mechanism has been implemented for converting the canvas coordinates to real coordinates.
    This mechanism is used when we figure out the real coordinate of the mouse, so when we insert points, we have the real coordinates of the points.

    • Again, tkinter.canvas  inserts and visualizes the points based on the canvas coordinates, therefore another mechanism has been implemented for converting
    the real coordinates to canvas coordinates. This is used when we insert a point to the canvas: we take its real coordinates and convert it to canvas coordinates
    and visualize the point on the canvas using its canvas coordinates.

    • When you move your mouse on the canvas, you will see coordinates of the mouse near it. Those are the real coordinates of the mouse.

A list of features is as follows:

    • User can insert points using 2D Gaussian and 2D Uniform distributions. For both distributions, first you need to specify the number of points.
    For Gaussian distribution you need to provide a covariance matrix in the following format <val1>,<val2>;<val3>,<val4>. An example input would be 1000,0;0,1000.
    For Uniform distribution you need to provide minimum and maximum X-coordinate values and minimum and maximum Y-coordinate values.

    • You can use the “Clear Points” button available on the bottom panel to clear all the points.

    • Every point has its real coordinates displayed near it. You can disable this setting in the application by clicking “Disable Coordinates” button.
    This button will not disable your mouse coordinates.

    • This implementation has two modes for the mouse clicking: “Insert Point” mode and “Delete Point” mode. When you are in “Insert Point” mode, your mouse
    click will insert a point to the coordinates of your mouse and trigger the selected algorithm to run. When you are in “Delete Point” mode, a red square shaped
    boundary will appear around your mouse in which every point inside that square will be deleted. The size of the square is not relative to the canvas but it is
    relative to the real coordinate system, its size changes by the scale factor. Thus, you can fit more points to be deleted into the square by zooming out, and less
    points by zooming in.

    • This implementation has three modes for visualizing the convex hull algorithms:
    1) Do NOT visualize,
    2) Visualize without delay,
    3) Visualize with delay.
    In all of the modes, the coordinates of the points in the convex hull are printed to the terminal.
    In the first mode, there is no visualization happening.
    In the second mode visualization happens in a fast pace without any delay.
    In the third mode visualization happens with a delay that you can specify in seconds, default delay is 1 second.

    • Bottom panel contains buttons for switching between algorithms. When an algorithm runs in any mode, these buttons are disabled.
    They are re-enabled when the algorithm is done. If you have a lot of points in the canvas and due to your selected mode the algorithm takes
    too much time due to visualization, there is no functionality implemented to stop it. It will eventually finish, but if you are in a hurry,
    simply close the application and rerun it.

Things to be careful about when using the application:

    • The delay for the third visualization mode has been implemented using time.sleep, therefore, whole app freezes in a delay.

    • If you try to insert a point in the middle of an algorithm running, you may get unexpected results. Thus, do not do it.

    • Please be aware of the number of points you create on the canvas. After 10,000 points Running Graham’s Scan, Jarvis March and Merge Hull in
    visual modes will take huge amount of time. Make sure coordinates are disabled before creating 10,000 points or more, as the data you see on the
    canvas will not make much sense and disabling coordinates after creating that many points will take a lot of time.