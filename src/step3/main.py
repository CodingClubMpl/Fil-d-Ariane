from tkinter import *

def load_map(filename):
    mapContent = []
    with open(filename) as f:
        mapContent = f.readlines()
    mapContent = [x.strip() for x in mapContent]
    return mapContent

def draw_square(canvas, x, y, color):
    canvas.create_rectangle(x*20, y*20, x*20+20, y*20+20, fill=color, outline='#476042', width=2)

def create_squares(canvas, mapContent):
    for y, line in enumerate(mapContent):
        for x, square in enumerate(line):
            if square == 'x':
                draw_square(canvas, x, y, 'red')
            elif square == 'o':
                draw_square(canvas, x, y, 'green')
            else:
                draw_square(canvas, x, y, 'white')

def get_coordinates(mapContent):
    coordinates = []
    for line in mapContent:
        coordinates.append([])
        for c in line:
            if c == 'x':
                coordinates[-1].append(1)
            elif c == 'o':
                coordinates[-1].append(2)
            else:
                coordinates[-1].append(0)
    return coordinates

def algo(canvas, mapCoord, path):
    pass

def main():
    mapContent = load_map("map.txt")
    mapCoord = get_coordinates(mapContent)
    tkMap = Tk()
    tkMap.title("Le Fil d'Ariane")
    canvas = Canvas(tkMap, width=1280, height=620)
    create_squares(canvas, mapContent)
    canvas.pack()
    max_loop = 1000
    path = []
    for value in range(0, max_loop):
        tkMap.after(value * 100, algo, canvas, mapCoord, path)
    mainloop()

if __name__ == "__main__":
    main()
