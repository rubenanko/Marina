import sys
import abstract
import ui
from openai import OpenAI
# import configparser

CONFIG_MODE = 0
EDITING_MODE = 1
ASKING_MODE = 2

INPUT_LABEL = ["\033[1;30mConfig : \033[0;0m",
               "\033[1;36mEdit : \033[0;0m",
               "\033[1;31mAsk : \033[0;0m"]

EDITING_PREPROMPT = "You are a programmer, i will submit raw code and instructions and you will respond with the raw code only. Assume that every request are modifications or additions to the given code. No quotation marks before the code, just the raw code. Respond with the whole code only. You must not add additionnal comments or characters to delimit the code."
ASKING_PREPROMPT = "You are a helpful code assistant, i will ask you questions."



class State:
    def __init__(self,filename : str = None):
        self.run = True
        self.offsetY = 0
        self.config = None
        self.mode = EDITING_MODE
        self.client = OpenAI(api_key="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")
        self.askMessages = [{"role": "system", "content": ASKING_PREPROMPT}]
        self.editMessages =  [{"role": "system", "content": EDITING_PREPROMPT}]

        if filename == None:
            open("new file","w+").close()
            self.filename = "new file"
            self.file = open("new file","r+")
        else:
            self.filename = filename
            self.file = open(filename,"r+")

        self.rawBuffer = self.file.read()
        self.buffer = self.rawBuffer.split("\n")
        self.displayBuffer = self.buffer

    def close(self)->None:
        self.file.close()

    def setFile(self,filename : str)->None:
        self.file.close()
        self.file = open(filename,"r+")

    def handle(self,userInput : str)->None:
        if userInput == "exit": self.run = False

        elif userInput == "save":   
            self.file.seek(0)
            self.file.write(self.rawBuffer)
    
        elif userInput == "save":
            if self.mode == EDITING_MODE:
                self.file.seek(0)
                self.file.write(self.rawBuffer)       
            elif self.mode == ASKING_MODE:
                with open("marina_logs.txt","w+") as f:
                    f.seek(0,2)
                    f.writelines(self.displayBuffer)

        elif userInput == "config":
            self.mode = CONFIG_MODE

        elif userInput == "edit":
            self.mode = EDITING_MODE
            self.displayBuffer = self.buffer

        elif userInput == "ask":
            self.mode = ASKING_MODE  

        elif userInput.removeprefix("+").removeprefix("-").isdigit():
            # self.offsetY = int(userInput)
            intUserInput = int(userInput)
            if not userInput[0].isdigit():
                newOffset = self.offsetY + int(userInput)
                if newOffset >=0 and newOffset < len(self.buffer):  self.offsetY = newOffset
            elif self.offsetY >= 0 and self.offsetY < len(self.buffer):
                self.offsetY = int(userInput)

        elif self.mode == EDITING_MODE:
            prompt = "name of the file : " + self.filename + "\ncontent : " + self.rawBuffer + "\nrequest : " + userInput
            self.editMessages.append({"role":"user","content":prompt})

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.editMessages
            )

            self.editMessages.append(response.choices[0].message)
            self.rawBuffer = response.choices[0].message.content
            self.buffer = self.rawBuffer.split("\n")
            self.displayBuffer = self.buffer

        elif self.mode == ASKING_MODE:
            prompt = "name of the file : " + self.filename + "\ncontent : " + self.rawBuffer + "\nrequest : " + userInput
            self.askMessages.append({"role":"user","content":prompt})

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.askMessages
            )

            self.askMessages.append(response.choices[0].message)
            
            self.displayBuffer = response.choices[0].message.content.split("\n")


def main(argv : list):
    filename = argv[1]
    size = abstract.getConsoleSize()
    state = State(filename)
    # cursorX,cursorY = 0,size.lines-1
    
    abstract.clear()

    while state.run:
        size = abstract.getConsoleSize()
        ui.drawFilename(filename,size.columns)
        ui.drawLines(min(size.lines-2,len(state.buffer)),state.offsetY)            
        ui.render(state.displayBuffer,size.columns,size.lines-3,0,size.lines-1,state.offsetY)
        userInput = input(INPUT_LABEL[state.mode])
        state.handle(userInput)
        
    state.close()    
    abstract.clear()


if __name__ == "__main__":
    main(sys.argv)