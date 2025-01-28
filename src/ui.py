def drawFilename(filename : str,width : int)->None:
    print(f"\033[1;1f\033[7;34m{filename}\033[0;0m",end=" "*(width-len(filename)))

def drawLines(height : int,displayOffsetY : int)->None:
    s = "\033[2;1f"
    offsetX = 7
    offsetY = 2
    for i in range(height):  s += f"\033[{i+offsetY};1f\033[1;33m{i+1} \033[{i+offsetY};{offsetX}f\033[0;34m~\033[0;0m"
    print(s,end="")

def render(buffer : str,width : int, height : int,cursorX : int, cursorY : int, displayOffsetY : int)->None:
    s = ""
    numberOfLinesToRender = min(len(buffer),height)
    offsetX = 9
    offsetY = 2
    
    for i in range(displayOffsetY,numberOfLinesToRender):
        blank = " "*max(0,(width-len(buffer[i])-offsetX))
        s += f"\033[{i+offsetY};{offsetX}f{buffer[i]}{blank}"

    for i in range(numberOfLinesToRender,height+2):
        s+= " "*(width-offsetX)
    print(f"{s}\033[{cursorY};{cursorX+offsetX}f",end="",flush=True)