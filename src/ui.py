def drawHeader(state,width)->None:
    print(f"\033[1;1f\033[7;34m{state.filename} | {len(state.buffer)} lines\033[0;0m",end=" "*(width-len(state.filename)-9-len(str(len(state.buffer)))))

def drawLines(height : int,displayOffsetY : int,cursorX : int, cursorY : int)->None:
    s = "\033[2;1f"
    offsetX = 7
    offsetY = 2
    for i in range(height): 
        blank = " "*(6-len(str(i+1+displayOffsetY)))
        s += f"\033[{i+offsetY};1f\033[1;33m{i+1+displayOffsetY}{blank}\033[{i+offsetY};{offsetX}f\033[0;34m~ \033[0;0m"

    print(f"{s}\033[{cursorY};{cursorX+9}f",end="")


def render(buffer : str,width : int, height : int, displayOffsetY : int)->None:
    s = ""
    numberOfLinesToRender = min(len(buffer)-displayOffsetY,height)
    offsetX = 9
    offsetY = 2
    
    for i in range(numberOfLinesToRender):
        blank = " "*max(0,(width-len(buffer[i+displayOffsetY])-offsetX))
        s += f"\033[{i+offsetY};{offsetX}f{buffer[i+displayOffsetY]}{blank}"

    for i in range(numberOfLinesToRender,height+2):
        s+= " "*(width-offsetX)
    print(s,end="",flush=True)