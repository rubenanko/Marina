import sys
import abstract
import ui

API_KEY = None

def main(argv : list):
    filename = argv[1]
    size = abstract.getConsoleSize()
    # cursorX,cursorY = 0,size.lines-1
    
    abstract.clear()
    ui.drawFilename(filename,size.columns)
    ui.drawLines(size.lines-2)

    f = open(filename,"r+")
    buffer = f.read().split("\n")
    f.close()

    ui.render(buffer,size.columns-1,size.lines-2,0,size.lines-1)

    run = True
    while run:
        tmp,size = size,abstract.getConsoleSize()
        if tmp.lines != size.lines or tmp.columns != size.columns:
            ui.drawFilename(filename,size.columns)
            ui.drawLines(size.lines-2)            
            ui.render(buffer,size.columns,size.lines-2,0,size.lines-1)
        input("\033[1;36mMarina : \033[0;0m")

if __name__ == "__main__":
    main(sys.argv)