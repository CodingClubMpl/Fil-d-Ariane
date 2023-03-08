from tkinter import *

def load_map(filename):
    mapContent = []
    with open(filename) as f:
        mapContent = f.readlines()
    mapContent = [x.strip() for x in mapContent]
    return mapContent

def main():
    mapContent = load_map("map.txt")
    tkMap = Tk()
    tkMap.title("Le Fil d'Ariane")
    canvas = Canvas(tkMap, width=1280, height=620)
    canvas.pack()
    mainloop()

if __name__ == "__main__":
    main()
