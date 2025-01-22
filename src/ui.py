def drawFilename(filename : str)->None:
    print(f"\033[1;1f\033[7;34m{filename}\033[0;0m")

def drawLines(height : int)->None:
    s = "\033[2;1f"
    for i in range(height):  s += f"\033[1;33m{i+1} \033[0;34m~\033[0;0m\n"
    print(s)

def render(buffer : str)->None:
    s = ""
    lines = buffer.split("\n")
    for i in range(len(lines)):
        s += f"\033[{i+2};5f{lines[i]}"
    print(s)