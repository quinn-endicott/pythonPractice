import tkinter
import tkinter.messagebox

class longDistanceGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        #5 frames, maybe
        self.labelFrame = tkinter.Frame(self.mainWindow)
        self.radioFrame = tkinter.Frame(self.mainWindow)
        self.minFrame = tkinter.Frame(self.mainWindow)
        #self.outFrame = tkinter.Frame(self.mainWindow)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        #Top Frame
        #label widget for top Frame
        self.label1 = tkinter.Label(self.labelFrame,
                                    text = "Estimate your long distance charge")
        self.label1.pack(side='left')

        #radio button frame 
        #intVar object for radio buttons
        self.radioVar = tkinter.IntVar()
        self.radioVar.set(1)
        self.rb1 = tkinter.Radiobutton(self.radioFrame,
                                       text='Daytime (6:00 a.m. through 5:59 p.m.)',
                                       variable=self.radioVar,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.radioFrame,
                                       text='Evening (6:00 p.m. through 11:59 p.m.)',
                                       variable=self.radioVar,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.radioFrame,
                                       text='Off-Peak (midnight through 5:59 a.m.)',
                                       variable=self.radioVar,
                                       value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #minutes frame
        self.minPrompt = tkinter.Label(self.minFrame,
                                       text='How many minutes is your call?  ')
        self.minEntry = tkinter.Entry(self.minFrame,
                                      width=10)
        self.minPrompt.pack(side='left')
        self.minEntry.pack(side='left')

        #output frame here if I want to do it that way instead if dialog box

            
            
        #button frame
        self.calcButton = tkinter.Button(self.buttonFrame,
                                         text='Calculate',
                                         command = self.calcPrice)
        self.quitButton = tkinter.Button(self.buttonFrame,
                                         text='Quit',
                                         command = self.mainWindow.destroy)
        self.calcButton.pack(side='left')
        self.quitButton.pack(side='left')

        self.labelFrame.pack()
        self.radioFrame.pack()
        self.minFrame.pack()
        self.buttonFrame.pack()


        tkinter.mainloop()
        
    def calcPrice(self):
        radioNum = self.radioVar.get()
        minEntry = float(self.minEntry.get())
        if radioNum == 1:
            price = minEntry * .07
        elif radioNum == 2:
            price = minEntry * .12
        else:
            price = minEntry * .05
        tkinter.messagebox.showinfo('Long Distance Cost',
                                    f'Your call will cost ${price:.2f}')        

if __name__ == '__main__':
    ldPricer = longDistanceGUI()
       
