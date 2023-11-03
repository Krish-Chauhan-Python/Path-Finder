import tkinter as tk
import math

import random
points = {6 : (0,0) , 1 : (-100,100) , 2 : (0,100) , 3 : (100,100) , 4 : (200,100), 5:(-100,0) , 7 : (100,0) , 8 : (200,0) , 13:(300,0), 9: (-100,-100) , 10: (0,-100),11:(100,-100) , 12: (200,-100)} 
paths = {1 : (2,5), 2: (1,6,3) , 3: (2,4,7) , 4: (3,8 ,13) , 5: (1,6,9) , 6: (6,2,7,10) , 7: (3,6,8,11) , 8: (4,7,12,13) , 9: (5,10) , 10:(6,9,11) , 11: (7,10,12) , 12: (8,11) , 13:(4,8)}
selected = [6,11,8,13]
final_path = []
a = 0
shortest = 999999999999
def is_list_subset(sublist, mainlist):
    return all(element in mainlist for element in sublist)
def dist(a,b):
    global points
    return ((points[a][0] - points[b][0])**2 + (points[a][1] - points[b][1])**2)**0.5
def show_path(path): 
    global points
    app.canvas.delete("all")
    generate("gray")
    for i in range(len(path)-1):
        app.canvas.create_line(points[path[i]][0] + 350, -(points[path[i]][1]) + 350, points[path[i+1]][0] + 350, -(points[path[i+1]][1]) + 350, fill="red", width=12)
def generate(color):
    global points
    global paths
    for i in paths:
        for j in paths[i]:
            app.canvas.create_line(points[i][0] + 350, -(points[i][1] )+ 350, points[j][0] + 350, -(points[j][1])+350, fill=color, width=20)
def path (iteration , prev_path , current_point , distance):
    global paths
    global a
    global selected 
    global final_path
    global shortest
    current_path = prev_path.copy()
    current_path.append(current_point)
    if len(current_path) > 1:
        distance += dist(current_point , current_path[-2])
    if current_path[0] == 1 and current_path[-1] == 1 and is_list_subset(selected,current_path) == True and shortest >= distance:
        shortest = distance
        final_path = current_path
        show_path(final_path)
        print(final_path)

    
        
    if iteration == 13:
        return
    for i in range(len(paths[current_point])):
        if paths[current_point][i] not in current_path or paths[current_point][i] == 1 and current_path.count(1) < 2 or paths[current_point][i] == 2 and current_path.count(2) < 2 or paths[current_point][i] == 5 and current_path.count(5) < 2:
            a += 1

            path(iteration+1 , current_path , paths[current_point][i] , distance)
def generator():
    global selected
    selected = []
    if button_1 == 1:
        selected.append(1)
    path(1,[],1,0)


class CityMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom City Map")

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.generate_button = tk.Button(self.root, text="Generate Map", command=lambda:generate("gray"))
        self.generate_button.pack()

        self.generate1_button = tk.Button(self.root, text="Generate Route", command=lambda:generator())
        self.generate1_button.pack()

        self.city_map = {}
        self.recycle_factory = None

        # Create a label for displaying mouse coordinates
        self.mouse_coords_label = tk.Label(self.root, text="Mouse Coordinates: (0, 0)")
        self.mouse_coords_label.pack()
        button_1 = tk.IntVar()
        checkbox = tk.Checkbutton(root, text=label, variable=button_1)
        checkbox.place

        # Bind the mouse motion event to update the coordinates
        self.canvas.bind("<Motion>", self.update_mouse_coordinates)

    def update_mouse_coordinates(self, event):
        x, y = event.x, event.y
        self.mouse_coords_label.config(text=f"Mouse Coordinates: ({x}, {y})")


if __name__ == "__main__":
    root = tk.Tk()
    app = CityMapApp(root)
    root.mainloop()
