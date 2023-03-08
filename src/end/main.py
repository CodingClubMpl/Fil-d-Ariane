from tkinter import *

wall_width = 20
wall_height = 20
canvas_width = 1280
canvas_height = 620
posX = 1
posY = 1

def load_map(filename):
    mapContent = []
    with open(filename) as f:
        mapContent = f.readlines()
    mapContent = [x.strip() for x in mapContent]
    return mapContent

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

def createTk():
    tkMap = Tk()
    tkMap.title("Le Fil d'Ariane")
    return tkMap

def create_canvas(tkMap):
    canvas = Canvas(tkMap, width=1280, height=620)
    return canvas

def create_rect(canvas, x, y, w, h, color):
    canvas.create_rectangle(x, y, w, h, fill=color, width=2, outline="#476042")

def create_squares(canvas, wallCoordinates):
    for y, line in enumerate(wallCoordinates):
        for x, square in enumerate(line):
            if square == 0:
                create_rect(canvas, x * wall_width, y * wall_height, (x + 1) * wall_width, (y + 1) * wall_height, 'white')
            elif square == 1:
                create_rect(canvas, x * wall_width, y * wall_height, (x + 1) * wall_width, (y + 1) * wall_height, 'red')
            else:
                create_rect(canvas, x * wall_width, y * wall_height, (x + 1) * wall_width, (y + 1) * wall_height, 'green')

def right(mapCoord, canvas):
    global posX
    global posY
    if mapCoord[posY][posX + 1] == 1:
        return
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'grey')
    mapCoord[posY][posX] = -1
    posX += 1
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'yellow')
    if mapCoord[posY][posX] == 2:
        exit(0)

def left(mapCoord, canvas):
    global posX
    global posY
    if mapCoord[posY][posX - 1] == 1:
        return
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'grey')
    mapCoord[posY][posX] = -1
    posX -= 1
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'yellow')
    if mapCoord[posY][posX] == 2:
        exit(0)

def up(mapCoord, canvas):
    global posX
    global posY
    if mapCoord[posY - 1][posX] == 1:
        return
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'grey')
    mapCoord[posY][posX] = -1
    posY -= 1
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'yellow')
    if mapCoord[posY][posX] == 2:
        exit(0)

def down(mapCoord, canvas):
    global posX
    global posY
    if mapCoord[posY + 1][posX] == 1:
        return
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'grey')
    mapCoord[posY][posX] = -1
    posY += 1
    create_rect(canvas, posX * wall_width, posY * wall_height, (posX + 1) * wall_width, (posY + 1) * wall_height, 'yellow')
    if mapCoord[posY][posX] == 2:
        exit(0)

def algo(canvas, mapCoord, path):
    global posX
    global posY
    if mapCoord[posY][posX + 1] == 0 or mapCoord[posY][posX + 1] == 2:
        right(mapCoord, canvas)
        path.append("right")
    elif mapCoord[posY + 1][posX] == 0 or mapCoord[posY + 1][posX] == 2:
        down(mapCoord, canvas)
        path.append("down")
    elif mapCoord[posY][posX - 1] == 0 or mapCoord[posY][posX - 1] == 2:
        left(mapCoord, canvas)
        path.append("left")
    elif mapCoord[posY - 1][posX] == 0 or mapCoord[posY - 1][posX] == 2:
        up(mapCoord, canvas)
        path.append("up")
    else:
        if path[-1] == "up":
            down(mapCoord, canvas)
        elif path[-1] == "left":
            right(mapCoord, canvas)
        elif path[-1] == "down":
            up(mapCoord, canvas)
        elif path[-1] == "right":
            left(mapCoord, canvas)
        path.pop()

def main():
    mapContent = load_map("map.txt")
    mapCoord = get_coordinates(mapContent)
    tkMap = createTk()
    canvas = create_canvas(tkMap)
    create_squares(canvas, mapCoord)
    max_loop = 1000
    path = []
    canvas.pack()
    for value in range(0, max_loop):
        tkMap.after(value * 100, algo, canvas, mapCoord, path)
    mainloop()

if __name__ == "__main__":
    main()
