import pyautogui, time, tkinter
from mouse import Mouse

currentX, currentY = pyautogui.position()
screenWidth, screenHeight = pyautogui.size()

mouse = Mouse(currentX, currentY)

#while mouse.x < screenWidth and mouse.y < screenHeight:
#    mouse.moveX(1)
#    time.sleep(1)
def moveMouse():
    while (True):
        step = int(entryStep.get())
        interval = int(entryInterval.get())
        #duration = int(entryDuration.get())
        mouse.moveX(step)
        labelTextX.set("Current X: " + str(mouse.x))
        labelTextY.set("Current Y: " + str(mouse.y))
        time.sleep(interval)
        root.update_idletasks()

root = tkinter.Tk()

root.title("Mouse Mover")
#root.minsize(500, 300)

# Creating Frames for each input
topFrameStep = tkinter.Frame(root)
topFrameStep.pack()
topFrameInterval = tkinter.Frame(root)
topFrameInterval.pack()
topFrameDuration = tkinter.Frame(root)
topFrameDuration.pack()
bottomFrame = tkinter.Frame(root)
bottomFrame.pack()

# Step Input
labelStep = tkinter.Label(topFrameStep, text="Step: ")
labelStep.pack(side = tkinter.LEFT)
entryStep = tkinter.Entry(topFrameStep)
entryStep.pack(side = tkinter.RIGHT, ipadx=6)

# Interval Input
labelInterval = tkinter.Label(topFrameInterval, text = "Interval: ")
labelInterval.pack(side = tkinter.LEFT)
entryInterval = tkinter.Entry(topFrameInterval)
entryInterval.pack(side = tkinter.RIGHT)

# Duration Input
labelDuration = tkinter.Label(topFrameDuration, text = "Duration: ")
labelDuration.pack(side = tkinter.LEFT)
entryDuration = tkinter.Entry(topFrameDuration)
entryDuration.pack(side = tkinter.RIGHT)

# Bottom Information
labelTextX = tkinter.StringVar()
labelTextX.set("Current X: " + str(mouse.x))
labelPositionX = tkinter.Label(bottomFrame, textvariable = labelTextX)
labelPositionX.pack()

labelTextY = tkinter.StringVar()
labelTextY.set("Current Y: " + str(mouse.y))
labelPositionY = tkinter.Label(bottomFrame, textvariable = labelTextY)
labelPositionY.pack()

buttonRun = tkinter.Button(bottomFrame, text="Run", command=moveMouse)
buttonRun.pack()

root.mainloop()

#if __name__ == '__main__':
#    main()