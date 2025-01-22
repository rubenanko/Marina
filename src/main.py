import sys
import abstract
import ui

def main(argv : list):
    filename = argv[1]
    size = abstract.getConsoleSize()
    cursorX,cursorY = 0,0

    abstract.clear()
    ui.drawFilename(filename,size.columns)
    ui.drawLines(size.lines-1)

    f = open(filename,"r+")
    buffer = f.read()
    f.close()

    ui.render(buffer,size.columns-1,size.lines-1,cursorX,cursorY)

    run = True
    while run:
        tmp,size = size,abstract.getConsoleSize()
        if tmp.lines != size.lines or tmp.columns != size.columns:
            ui.drawFilename(filename,size.columns)
            ui.drawLines(size.lines-1)            
            ui.render(buffer,size.columns,size.lines-1,cursorX,cursorY)


if __name__ == "__main__":
    main(sys.argv)