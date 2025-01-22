import sys
import abstract
import ui

def main(argv):
    filename = argv[1]
    size = abstract.getConsoleSize()

    abstract.clear()
    ui.drawFilename(filename)
    ui.drawLines(size.lines-1)

    f = open(filename,"r+")

    # ui.render(f.read())
    f.close()
    while True:
        pass

if __name__ == "__main__":
    main(sys.argv)