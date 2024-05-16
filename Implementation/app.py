import math
import tkinter as tk
import numpy as np
from grahams_scan_utilities import grahams_scan_initial_call
from jarvis_march_utilities import jarvis_march_initial_call
from quickhull_utilities import quickhull_initial_call
from mergehull_utilities import mergehull_initial_call

class ConvexHullVisualization:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Convex Hull Visualization")
        self.root.geometry("1400x1000")  # Set window size to 1000x1000
        
        # Creating frames for the left and bottom panels
        self.left_panel = tk.Frame(self.root, width=200, height=1000, bg="light gray")
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.bottom_panel = tk.Frame(self.root, width=1400, height=200, bg="light gray")
        self.bottom_panel.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas = tk.Canvas(self.root, width=1400, height=800)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.coordinates_label = tk.Label(self.canvas, text="Coordinates: (0, 0)", bg="white")
        self.coordinates_label.place(x=10, y=10)  # Initially place at (10, 10)

        self.points = []  # List to store points
        self.mode = "Insert"  # Default mode is Insert

        self.visualization_mode_options = ["Do NOT Visualize", "Visualize w/o Delay", "Visualize Delayed"]
        self.current_visualization_mode_index = 0  # Start with Mode 1 initially


        # Gaussian Distribution Fields
        self.gaussian_name = tk.Label(self.left_panel, text="Gaussian Distribution Parameters", font=("TkDefaultFont", 10, "bold"))
        self.gaussian_name.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.num_points_label_gaussian = tk.Label(self.left_panel, text="Number of Points:")
        self.num_points_label_gaussian.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.num_points_entry_gaussian = tk.Entry(self.left_panel)
        self.num_points_entry_gaussian.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.covariance_label = tk.Label(self.left_panel, text="Covariance Matrix\n(semicolon separated values):")
        self.covariance_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.covariance_entry = tk.Entry(self.left_panel)
        self.covariance_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.generate_points_button_gaussian = tk.Button(self.left_panel, text="Generate Gaussian Points", command=self.generate_points_gaussian)
        self.generate_points_button_gaussian.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Separator Line
        self.separator_line_gaussian_uniform = tk.Frame(self.left_panel, height=2, width=180, bg="black")
        self.separator_line_gaussian_uniform.pack(side=tk.TOP, padx=5, pady=10, fill=tk.X)

        # Uniform Distribution Fields
        self.uniform_name = tk.Label(self.left_panel, text="Uniform Distribution Parameters", font=("TkDefaultFont", 10, "bold"))
        self.uniform_name.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.num_points_label_uniform = tk.Label(self.left_panel, text="Number of Points:")
        self.num_points_label_uniform.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.num_points_entry_uniform = tk.Entry(self.left_panel)
        self.num_points_entry_uniform.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.min_x_value_label = tk.Label(self.left_panel, text="Min X Value:")
        self.min_x_value_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.min_x_value_entry = tk.Entry(self.left_panel)
        self.min_x_value_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.max_x_value_label = tk.Label(self.left_panel, text="Max X Value:")
        self.max_x_value_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.max_x_value_entry = tk.Entry(self.left_panel)
        self.max_x_value_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.min_y_value_label = tk.Label(self.left_panel, text="Min Y Value:")
        self.min_y_value_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.min_y_value_entry = tk.Entry(self.left_panel)
        self.min_y_value_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.max_y_value_label = tk.Label(self.left_panel, text="Max Y Value:")
        self.max_y_value_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)
        self.max_y_value_entry = tk.Entry(self.left_panel)
        self.max_y_value_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.generate_points_button_uniform = tk.Button(self.left_panel, text="Generate Uniform Points", command=self.generate_points_uniform)
        self.generate_points_button_uniform.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Separator Line
        self.separator_line_uniform_modes = tk.Frame(self.left_panel, height=2, width=180, bg="black")
        self.separator_line_uniform_modes.pack(side=tk.TOP, padx=5, pady=10, fill=tk.X)
        
        # Buttons for other functionalities
        self.mode_switching_name = tk.Label(self.left_panel, text="Mode Switching", font=("TkDefaultFont", 10, "bold"))
        self.mode_switching_name.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.current_mode_label = tk.Label(self.left_panel, text="Current Mode: {}".format(self.mode), bg="light gray")
        self.current_mode_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.insert_button = tk.Button(self.left_panel, text="Insert Point", command=self.set_insert_mode, bg="green")
        self.insert_button.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.delete_button = tk.Button(self.left_panel, text="Delete Point", command=self.set_delete_mode, bg="red")
        self.delete_button.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Separator Line
        self.separator_line_modes_visualization = tk.Frame(self.left_panel, height=2, width=180, bg="black")
        self.separator_line_modes_visualization.pack(side=tk.TOP, padx=5, pady=10, fill=tk.X)

        self.visualization_name = tk.Label(self.left_panel, text="Visualization", font=("TkDefaultFont", 10, "bold"))
        self.visualization_name.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Initialize scale factor
        self.scale_factor = 1.0

        # Create a label to display the scale factor
        self.scale_label = tk.Label(self.left_panel, text="Scale Factor: {:.2f}".format(self.scale_factor), bg="light gray")
        self.scale_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Create a label to display the current mode
        self.visualization_mode_label = tk.Label(self.left_panel, text=self.visualization_mode_options[self.current_visualization_mode_index], bg="light gray")
        self.visualization_mode_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Create an entry for delay in visualization
        self.visualization_delay_label = tk.Label(self.left_panel, text="Delay (in Seconds)", bg="light gray")
        self.visualization_delay_label.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.visualization_delay_entry = tk.Entry(self.left_panel, state="disabled")
        self.visualization_delay_entry.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Create a button to switch modes
        self.visualization_mode_button = tk.Button(self.left_panel, text="Switch Mode", command=self.switch_visualization_mode)
        self.visualization_mode_button.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        # Create a button to switch modes
        self.visualization_coordinate_button = tk.Button(self.left_panel, text="Disable Coordinates", command=self.toggle_coordinate_visibility)
        self.visualization_coordinate_button.pack(side=tk.TOP, anchor="w", padx=5, pady=3)

        self.select_grahams_scan_button = tk.Button(self.bottom_panel, text="Graham's Scan", command=self.switch_graham_scan)
        self.select_grahams_scan_button.pack(side=tk.LEFT, padx=5, pady=3)

        self.select_jarvis_march_button = tk.Button(self.bottom_panel, text="Jarvis March", command=self.switch_jarvis_march)
        self.select_jarvis_march_button.pack(side=tk.LEFT, padx=5, pady=3)

        self.select_quickhull_button = tk.Button(self.bottom_panel, text="Quickhull", command=self.switch_quickhull)
        self.select_quickhull_button.pack(side=tk.LEFT, padx=5, pady=3)

        self.select_mergehull_button = tk.Button(self.bottom_panel, text="Mergehull", command=self.switch_mergehull)
        self.select_mergehull_button.pack(side=tk.LEFT, padx=5, pady=3)

        self.clear_button = tk.Button(self.bottom_panel, text="Clear Points", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=3)

        self.select_grahams_scan_button.config(highlightbackground="green")
        self.select_jarvis_march_button.config(highlightbackground="red")
        self.select_quickhull_button.config(highlightbackground="red")
        self.select_mergehull_button.config(highlightbackground="red")

        # Binding mouse click and motion events
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Motion>", self.update_coordinates)
        
        # Additional attribute to track if the mouse button is currently held down
        self.mouse_held_down = False

        # Binding mouse button release event
        self.canvas.bind("<ButtonRelease-1>", self.handle_button_release)

        self.delete_mode_square = None  # Variable to hold the delete mode square
        self.delete_size = 10

        self.show_coordinates = True

        self.grahams_scan_label = "Graham's Scan"
        self.jarvis_march_label = "Jarvis March"
        self.quickhull_label = "Quickhull"
        self.mergehull_label = "Mergehull"
        self.selected_convex_hull_algorithm = self.grahams_scan_label

        self.last_x = 0
        self.last_y = 0

        self.last_real_x = 0
        self.last_real_y = 0
        
        self.lines = []  # List to keep track of lines drawn on the canvas

        self.circle_radius = 5
        # Bind mouse scroll event to the canvas
        #Uncomment when implementing zooming
        
        self.canvas.bind("<Button-4>", self.zoom_in)
        self.canvas.bind("<Button-5>", self.zoom_out)
        self.canvas.focus_set()
        
        self.root.mainloop()


    def set_insert_mode(self):
        self.mode = "Insert"
        self.current_mode_label.config(text="Current Mode: {}".format(self.mode))

    def set_delete_mode(self):
        self.mode = "Delete"
        self.current_mode_label.config(text="Current Mode: {}".format(self.mode))

    def switch_visualization_mode(self):
        # Increment current mode index and wrap around if necessary
        self.current_visualization_mode_index = (self.current_visualization_mode_index + 1) % len(self.visualization_mode_options)
        self.visualization_mode_label.config(text=self.visualization_mode_options[self.current_visualization_mode_index])
        if self.current_visualization_mode_index != 2:
            self.visualization_delay_entry.config(state="disabled")
        else:
            self.visualization_delay_entry.config(state="normal")


    def generate_points_gaussian(self):
        # Retrieve the number of points and covariance matrix from the entry fields
        num_points = int(self.num_points_entry_gaussian.get())
        covariance_str = self.covariance_entry.get()

        # Convert the covariance matrix string to a 2D list
        covariance_matrix = []
        rows = covariance_str.split(';')
        for row in rows:
            values = row.split(',')
            covariance_matrix.append([float(val) for val in values])
        print(covariance_matrix)
        # Generate points using the specified parameters
        mean = [400, 400]  # Mean of the Gaussian distribution (center of the canvas)
        positions = np.random.multivariate_normal(mean, covariance_matrix, num_points)
        
        for pos in positions:
            x, y = pos
            x, y = self.calculate_canvas_coordinates(x, y)
            self.insert_point(x, y)

    def generate_points_uniform(self):
        num_points = int(self.num_points_entry_uniform.get())
        min_x_value = float(self.min_x_value_entry.get())
        max_x_value = float(self.max_x_value_entry.get())
        min_y_value = float(self.min_y_value_entry.get())
        max_y_value = float(self.max_y_value_entry.get())
        xs = np.random.uniform(min_x_value, max_x_value, size=num_points)
        ys = np.random.uniform(min_y_value, max_y_value, size=num_points)
        positions = np.column_stack((xs, ys))
        for pos in positions:
            x, y = pos
            x, y = self.calculate_canvas_coordinates(x, y)
            self.insert_point(x, y)

    def update_delete_mode_square(self, event=None):
        # Delete the existing square if it exists
        if self.delete_mode_square:
            self.canvas.delete(self.delete_mode_square)

        # If not in delete mode, return
        if self.mode != "Delete":
            return

        # Create a square around the cursor position
        x0 = event.x - self.delete_size
        y0 = event.y - self.delete_size
        x1 = event.x + self.delete_size
        y1 = event.y + self.delete_size
        self.delete_mode_square = self.canvas.create_rectangle(x0, y0, x1, y1, outline="red")

    def handle_motion(self, event):
        if self.mode == "Delete" and self.mouse_held_down:
            # Check if previous coordinates are available
              # Update previous coordinates
            self.delete_point(event.x, event.y)

    def handle_click(self, event):
        
        self.mouse_held_down = True
        if self.mode == "Delete":
            self.delete_point(event.x, event.y)
        elif self.mode == "Insert":
            self.disable_algorithm_selection_buttons()
            self.insert_point(event.x, event.y)
            try:
                delay = int(self.visualization_delay_entry.get())
            except ValueError:
                delay = 1
            if self.selected_convex_hull_algorithm == self.grahams_scan_label:
                grahams_scan_initial_call(self, delay)
            elif self.selected_convex_hull_algorithm == self.jarvis_march_label:
                jarvis_march_initial_call(self, delay)
            elif self.selected_convex_hull_algorithm == self.quickhull_label:
                quickhull_initial_call(self, delay)
            elif self.selected_convex_hull_algorithm == self.mergehull_label:
                mergehull_initial_call(self, delay)
            else:
                print("Invalid convex hull algorithm label detected. Terminating.")
                exit(1)
            self.enable_algorithm_selection_buttons()

    def disable_algorithm_selection_buttons(self):
        self.select_grahams_scan_button.config(state="disabled")
        self.select_jarvis_march_button.config(state="disabled")
        self.select_quickhull_button.config(state="disabled")
        self.select_mergehull_button.config(state="disabled")
        

    def enable_algorithm_selection_buttons(self):
        self.select_grahams_scan_button.config(state="normal")
        self.select_jarvis_march_button.config(state="normal")
        self.select_quickhull_button.config(state="normal")
        self.select_mergehull_button.config(state="normal")
        

    def handle_button_release(self, event):
        # Set mouse held down flag to False when mouse button is released
        self.mouse_held_down = False
    
    
    def zoom_in(self, event):
        self.last_x = event.x
        self.scale_canvas(1.1, event)

    def zoom_out(self, event):
        self.scale_canvas(0.9, event)

    def scale_canvas(self, factor, event):
        # Get the current cursor position relative to the canvas
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        self.scale_factor = self.scale_factor * factor
        self.scale_label.config(text="Scale Factor: {:.2f}".format(self.scale_factor))

        try:
            # Apply scaling to canvas items
            try:
                self.canvas.scale("all", x, y, factor, factor)
            except Exception as e:
                print("An error occurred while scaling canvas items:", e)

            # Set focus to the canvas to bring it back to the cursor
            
            try:
                self.canvas.focus_set()
            except Exception as e:
                print("An error occurred while setting focus to the canvas:", e)
            
            # Update the cursor position after scaling
            
            try:
                self.update_coordinates(event)
            except Exception as e:
                print("An error occurred while updating cursor position:", e)
            
        except Exception as e:
            print("An unexpected error occurred:", e)

    

    def insert_point(self, x, y):
        # Adjust coordinates based on scale factor
        
        real_x, real_y = self.calculate_real_coordinates( x, y)
        # Generate a unique tag for the point
        point_tag = f"point_{real_x:.2f}_{real_y:.2f}"
        point_coordinate_tag = f"point_coordinate_{real_x:.2f}_{real_y:.2f}"
        self.points.append((real_x, real_y))
        # Create the oval with the unique tag
        self.canvas.create_oval(x - 2 * self.scale_factor, y - 2 * self.scale_factor, x + 2 * self.scale_factor, y + 2 * self.scale_factor, fill="black", tags=point_tag)
        # Create a text label near the oval to indicate its coordinates
        label_text = f"({real_x:.2f}, {real_y:.2f})"

        if self.show_coordinates:
            self.canvas.create_text(x, y - 10, text=label_text, tags=point_coordinate_tag, state='normal', anchor="s")
        else:
            self.canvas.create_text(x, y - 10, text=label_text, tags=point_coordinate_tag, state='hidden', anchor="s")

    def delete_point(self, x, y):
        print("delete point called")
        points_to_delete = []
        delete_size_scaled = self.delete_size / self.scale_factor
        real_x, real_y = self.calculate_real_coordinates( x, y)
        print("range of points: ", real_x - delete_size_scaled," ", real_x + delete_size_scaled," ", real_y - delete_size_scaled," ", real_y + delete_size_scaled)
        for point in self.points:
            px, py = point
            if (real_x - delete_size_scaled <= px <= real_x + delete_size_scaled) and (real_y - delete_size_scaled <= py <= real_y + delete_size_scaled):
                points_to_delete.append(point)

        for point in points_to_delete:
            self.points.remove(point)
            x, y = point
            print(" deleting point: ", x, " ", y)
            self.canvas.delete(f"point_{x:.2f}_{y:.2f}")
            self.canvas.delete(f"point_coordinate_{x:.2f}_{y:.2f}")

    def toggle_coordinate_visibility(self):
        # Toggle the value of the boolean variable
        self.show_coordinates = not self.show_coordinates
        if self.show_coordinates:
            self.visualization_coordinate_button.config(text="Disable Coordinates")
        else:
            self.visualization_coordinate_button.config(text="Enable Coordinates")
        # If visibility is toggled, update all point labels accordingly
        for point in self.points:
            real_x, real_y = point
            point_tag = f"point_coordinate_{real_x:.2f}_{real_y:.2f}"
            if self.show_coordinates:
                self.canvas.itemconfigure(point_tag, state='normal')
            else:
                self.canvas.itemconfigure(point_tag, state='hidden')


    def calculate_real_coordinates(self, x, y):
        real_x = self.last_real_x + (x - self.last_x) / self.scale_factor
        real_y = self.last_real_y + (y - self.last_y) / self.scale_factor
        return real_x, real_y

    def calculate_canvas_coordinates(self, x, y):
        canvas_x = (x - self.last_real_x) * self.scale_factor + self.last_x
        canvas_y = (y - self.last_real_y) * self.scale_factor + self.last_y
        return canvas_x, canvas_y

    def update_coordinates(self, event):
        # Get the size of the canvas
        canvas_width = self.canvas.winfo_width()

        # Calculate the width of the coordinate text
        text_width = self.coordinates_label.winfo_width()

        # Calculate the offset from the cursor position to the canvas edges
        offset_x = -text_width - 10 if event.x > canvas_width - text_width - 10 else 10
        
        # Calculate scaled coordinates
        real_x, real_y = self.calculate_real_coordinates( event.x, event.y);

        self.last_real_x = real_x
        self.last_real_y = real_y

        self.last_x = event.x
        self.last_y = event.y

        # Update the label with coordinates and adjust its position
        self.coordinates_label.config(text=f"Coordinates: ({self.last_real_x:.2f}, {self.last_real_y:.2f})")
        self.coordinates_label.place(x=event.x + offset_x, y=event.y)

        # Update the position of the delete mode square
        if self.mode == "Delete":
            if self.mouse_held_down:
                self.handle_motion(event)
            self.update_delete_mode_square(event)

    def switch_graham_scan(self):
        self.selected_convex_hull_algorithm = self.grahams_scan_label
        self.select_grahams_scan_button.config(highlightbackground="green")
        self.select_jarvis_march_button.config(highlightbackground="red")
        self.select_quickhull_button.config(highlightbackground="red")
        self.select_mergehull_button.config(highlightbackground="red")

    def switch_jarvis_march(self):
        self.selected_convex_hull_algorithm = self.jarvis_march_label
        self.select_grahams_scan_button.config(highlightbackground="red")
        self.select_jarvis_march_button.config(highlightbackground="green")
        self.select_quickhull_button.config(highlightbackground="red")
        self.select_mergehull_button.config(highlightbackground="red")

    def switch_quickhull(self):
        self.selected_convex_hull_algorithm = self.quickhull_label
        self.select_grahams_scan_button.config(highlightbackground="red")
        self.select_jarvis_march_button.config(highlightbackground="red")
        self.select_quickhull_button.config(highlightbackground="green")
        self.select_mergehull_button.config(highlightbackground="red")

    def switch_mergehull(self):
        self.selected_convex_hull_algorithm = self.mergehull_label
        self.select_grahams_scan_button.config(highlightbackground="red")
        self.select_jarvis_march_button.config(highlightbackground="red")
        self.select_quickhull_button.config(highlightbackground="red")
        self.select_mergehull_button.config(highlightbackground="green")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points = []
    
    def is_left_turn(self, p0, p1, p2):
        return p0[0] * p1[1] + p2[0] * p0[1] + p1[0] * p2[1] - p2[0] * p1[1] - p0[0] * p2[1] - p1[0] * p0[1] > 0

    def is_right_turn(self, p0, p1, p2):
        return p0[0] * p1[1] + p2[0] * p0[1] + p1[0] * p2[1] - p2[0] * p1[1] - p0[0] * p2[1] - p1[0] * p0[1] < 0

    def is_not_right_turn(self, p0, p1, p2):
        return p0[0] * p1[1] + p2[0] * p0[1] + p1[0] * p2[1] - p2[0] * p1[1] - p0[0] * p2[1] - p1[0] * p0[1] >= 0

    def is_not_left_turn(self, p0, p1, p2):
        return p0[0] * p1[1] + p2[0] * p0[1] + p1[0] * p2[1] - p2[0] * p1[1] - p0[0] * p2[1] - p1[0] * p0[1] <= 0
    
    # Define the sorting function
    def sort_by_polar_angle_and_distance(self, point, min_x, min_y):
        # Calculate the vector from p_min_y to the current point
        dx = point[0] - min_x
        dy = point[1] - min_y
        
        # Calculate the polar angle
        polar_angle = math.atan2(dy, dx)
        # Calculate the distance between p_min_y and the current point
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Return a tuple of polar angle and distance
        return (polar_angle, distance)

    def draw_line(self, x1, y1, x2, y2):
        line = self.canvas.create_line(x1, y1, x2, y2, fill="blue")
        self.lines.append(line)
        return line

    def draw_circle(self, x, y, v_text, v_tag):
        # Calculate coordinates for the bounding box of the circle
        x1 = x - self.circle_radius * self.scale_factor
        y1 = y - self.circle_radius * self.scale_factor
        x2 = x + self.circle_radius * self.scale_factor
        y2 = y + self.circle_radius * self.scale_factor
        # Draw an oval using the bounding box coordinates
        self.canvas.create_oval(x1, y1, x2, y2, tags=v_tag, outline="red")
        self.canvas.create_text(x + 15, y + 15, text=v_text, tags=v_tag, anchor="s")

    def clear_lines(self):
        # Remove all lines drawn on the canvas
        for line in self.lines:
            self.canvas.delete(line)
        self.lines = []

if __name__ == "__main__":
    app = ConvexHullVisualization()
