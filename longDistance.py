#this class depends on the tkinter and tkinter.messagebox modules
import tkinter
import tkinter.messagebox
#The longDistanceGUI class describes a gui program that allows a user to calculate
#an estimated charge for their call based on a selection of rate from a set of radio
#buttons and outputs the result in a dialog box when the user presses a button.
class longDistanceGUI:
    #__init__ method will create the gui window
    def __init__(self):
        #create the main window
        self.mainWindow = tkinter.Tk()
        #label frame tells user about the use of the program
        self.labelFrame = tkinter.Frame(self.mainWindow)
        #radio frame contains the radio buttons to select rate
        self.radioFrame = tkinter.Frame(self.mainWindow)
        #minFrame is for entering how long the call will take
        self.minFrame = tkinter.Frame(self.mainWindow)
        #self.outFrame = tkinter.Frame(self.mainWindow), did not end up doing this
        #buttonFrame contains the calculate and quit buttons
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        
        #label widget for label frame
        self.label1 = tkinter.Label(self.labelFrame,
                                    text = "Estimate your long distance charge")
        #pack label widget into frame
        self.label1.pack(side='left')

        
        #intVar object for radio buttons
        self.radioVar = tkinter.IntVar()
        #set radioVar to 1
        self.radioVar.set(1)
        #first radio button, value 1
        self.rb1 = tkinter.Radiobutton(self.radioFrame,
                                       text='Daytime (6:00 a.m. through 5:59 p.m.)',
                                       variable=self.radioVar,
                                       value=1)
        #second radio button, value 2
        self.rb2 = tkinter.Radiobutton(self.radioFrame,
                                       text='Evening (6:00 p.m. through 11:59 p.m.)',
                                       variable=self.radioVar,
                                       value=2)
        #third radio button, value 3
        self.rb3 = tkinter.Radiobutton(self.radioFrame,
                                       text='Off-Peak (midnight through 5:59 a.m.)',
                                       variable=self.radioVar,
                                       value=3)
        #pack radio buttons into frame
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #prompt user to enter how long their call is in minutes
        self.minPrompt = tkinter.Label(self.minFrame,
                                       text='How many minutes is your call?  ')
        #entry widget for minute entry to go in
        self.minEntry = tkinter.Entry(self.minFrame,
                                      width=10)
        #back both in line, label furthest left
        self.minPrompt.pack(side='left')
        self.minEntry.pack(side='left')

        #output frame here if I want to do it that way instead if dialog box

            
            
        #calc button calls on calcPrice method
        self.calcButton = tkinter.Button(self.buttonFrame,
                                         text='Calculate',
                                         command = self.calcPrice)
        #quit button detroys window
        self.quitButton = tkinter.Button(self.buttonFrame,
                                         text='Quit',
                                         command = self.mainWindow.destroy)
        #pack buttons in frame, calculate furthest left
        self.calcButton.pack(side='left')
        self.quitButton.pack(side='left')
        #pack frames in window
        self.labelFrame.pack(pady=10)
        self.radioFrame.pack(pady=5)
        #the min frame is longest and has an ugly merger with the side of the window
        #add padding on x axis
        self.minFrame.pack(padx=10, pady=5)
        self.buttonFrame.pack(pady=10)

        #run tkinter event loop
        tkinter.mainloop()
    #the calcPrice method calculates call price based on minutes entered and which
    #radio button is selected    
    def calcPrice(self):
        #get the value of the current radioVar, assign to variable
        radioNum = self.radioVar.get()
        #get the number of minutes entered by user, assign to variable
        minEntry = float(self.minEntry.get())
        #if the first button is selected
        if radioNum == 1:
            price = minEntry * .07
        #if the second button is selected
        elif radioNum == 2:
            price = minEntry * .12
        #if the third button is selected
        else:
            price = minEntry * .05
        #create a dialog box that tells the user how much their call will cost
        tkinter.messagebox.showinfo('Long Distance Cost',
                                    f'Your call will cost ${price:.2f}')        

       
