import sys
import abstract
import ui
from pynput import keyboard

def main(argv : list):
    filename = argv[1]
    size = abstract.getConsoleSize()
    cursorX,cursorY = 0,0

    abstract.clear()
    # ui.drawFilename(filename,size.columns)
    # ui.drawLines(size.lines-1)

    f = open(filename,"r+")
    buffer = f.read().split("\n")
    f.close()

    # ui.render(buffer,size.columns-1,size.lines-1,cursorX,cursorY)

    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                break
            else:
                print('Received event {}'.format(event))

    # run = True
    # while run:
    #     tmp,size = size,abstract.getConsoleSize()
    #     if tmp.lines != size.lines or tmp.columns != size.columns:
    #         ui.drawFilename(filename,size.columns)
    #         ui.drawLines(size.lines-1)            
    #         ui.render(buffer,size.columns,size.lines-1,cursorX,cursorY)


if __name__ == "__main__":
    main(sys.argv)