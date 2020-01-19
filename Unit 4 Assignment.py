"""
Author: Jacky Ho
Date: March 6,2017
Description: Program that opens up a GUI for the user to interact with. User is
able to enter their own persons name, a noun and a verb. They then decide if they
want to use an adjective and decide which body part they want. The program then 
takes all the user input and creates a story in Mad-lib fashion.

"""
import Tkinter
class StoryMaker:
    def __init__(self):
        # Create the main window widget.
        self.main_window = Tkinter.Tk()
 
        # Create two frames, one for the top of the
        # window, and one for the bottom.
        self.frame_1= Tkinter.Frame(self.main_window)
        self.frame_2= Tkinter.Frame(self.main_window)
        self.frame_3= Tkinter.Frame(self.main_window)
        self.frame_4= Tkinter.Frame(self.main_window)
        self.frame_5= Tkinter.Frame(self.main_window)
        self.frame_6= Tkinter.Frame(self.main_window)
        self.frame_7= Tkinter.Frame(self.main_window)
        self.frame_8= Tkinter.Frame(self.main_window)
        
        # Create label and entry widgets for frames.
        self.label_1 = Tkinter.Label(self.frame_1, text='Please enter information for a new story, then click the "Make Story" button.')
        self.label_2 = Tkinter.Label(self.frame_2, text='Person:          ')
        self.entry_2 = Tkinter.Entry(self.frame_2, width=25)
        self.entry_2.insert(Tkinter.END, "jacky")
        self.label_3 = Tkinter.Label(self.frame_3, text='Noun:            ')
        self.entry_3 = Tkinter.Entry(self.frame_3, width=25)
        self.entry_3.insert(Tkinter.END, "dog")
        self.label_4 = Tkinter.Label(self.frame_4, text='Verb:              ')
        self.entry_4 = Tkinter.Entry(self.frame_4, width=25)
        self.entry_4.insert(Tkinter.END, "pray")
        #check boxes
        self.label_5 = Tkinter.Label(self.frame_5, text='Adjective(s):')
        #radio buttons
        self.label_6 = Tkinter.Label(self.frame_6, text='Body Part: ')
        
        # Create a Button widget
        self.my_button = Tkinter.Button(self.frame_7, text='Make Story!', command=self.make_story)        
        
        # Create three IntVar objects to use with the Checkbuttons.
        self.cb_var1 = Tkinter.IntVar()
        self.cb_var2 = Tkinter.IntVar()
        self.cb_var3 = Tkinter.IntVar()
        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        # Create the Checkbutton widgets in the fifth_frame.
        self.cb1 = Tkinter.Checkbutton(self.frame_5, text='happy', variable=self.cb_var1)
        self.cb2 = Tkinter.Checkbutton(self.frame_5, text='lively', variable=self.cb_var2)
        self.cb3 = Tkinter.Checkbutton(self.frame_5, text='splendid', variable=self.cb_var3)        
        
        # Create an IntVar object to use with the Radiobuttons.
        self.radio_var = Tkinter.IntVar()
        # Set the intVar object to 1.
        self.radio_var.set(1)        
        # Create the Radiobutton widgets.
        self.rb1 = Tkinter.Radiobutton(self.frame_6, text='heart', variable=self.radio_var, value=1)
        self.rb2 = Tkinter.Radiobutton(self.frame_6, text='legs', variable=self.radio_var, value=2)
        self.rb3 = Tkinter.Radiobutton(self.frame_6, text='stomach', variable=self.radio_var, value=3)
        
        #packing
        #labels
        self.label_1.pack(side="left")
        self.label_2.pack(side="left")
        self.label_3.pack(side="left")
        self.label_4.pack(side="left")
        self.label_5.pack(side="left")
        self.label_6.pack(side="left")
        #entrys
        self.entry_2.pack(side="left")
        self.entry_3.pack(side="left")
        self.entry_4.pack(side="left")
        #checkboxes
        self.cb1.pack(side="left")
        self.cb2.pack(side="left")
        self.cb3.pack(side="left")
        #radiobuttons
        self.rb1.pack(side="left")
        self.rb2.pack(side="left")
        self.rb3.pack(side="left")      
        #button
        self.my_button.pack(side="left")
        #frames
        self.frame_1.pack(anchor="w")
        self.frame_2.pack(anchor="w")
        self.frame_3.pack(anchor="w")
        self.frame_4.pack(anchor="w")
        self.frame_5.pack(anchor="w")
        self.frame_6.pack(anchor="w")
        self.frame_7.pack(anchor="w")
        self.frame_8.pack(anchor="w")
        
        # Enter the Tkinter main loop.
        Tkinter.mainloop()        
        
    def make_story(self):
        #determine which checkboxes are selected
        self.adjective=""
        if self.cb_var1.get() == 1:
            self.adjective = self.adjective + "happy, "
        if self.cb_var2.get() == 1:
            self.adjective = self.adjective + "lively, "
        if self.cb_var3.get() == 1:
            self.adjective = self.adjective + "splendid, "
        
        #determine which radio button is selected
        self.body=""
        if self.radio_var.get()== 1:
            self.body="heart"
        elif self.radio_var.get()== 2:
            self.body="legs"
        else:
            self.body="stomach"
        
        #variables for story
        person= (self.entry_2.get()).title()
        noun= self.entry_3.get()
        verb= self.entry_4.get()
        adjective= self.adjective
        body= self.body
    
        
        #tk text creating the story
        self.text= Tkinter.Text(self.frame_8)
        self.text.delete(1.0,Tkinter.END)
        self.text.insert(Tkinter.END,"The famous astronaut " + person + " had nearly given up a life-long quest to find the planet of " + noun + "'s when one day, the planet of " + noun + "'s found " + person + ". A strong, " + adjective + "peculiar feeling of acomplishment overwhelmed " + person + ". After all this time, the search was finally over. " +person+" landed his spaceship on the planet of "+noun+"'s and the astronaut's " + body + " started to feel weak and heavy. " + person + " took one step outside and suddenly a " + noun + " jumped out at him. " + person + " began to run and " + verb + "ed for his life but it wasn't enough as the " + noun + " ended up devouring " + person + ".")
        #pack the text                 
        self.text.pack(side="left")

# Create an instance of the StoryMaker class.
my_story= StoryMaker()