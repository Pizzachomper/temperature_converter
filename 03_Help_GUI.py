from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Temperature conversion tool (C° to F° or vise versa)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                       text="Help / Info",
                                       bg="#CC6600",
                                       fg="#FFFFFF",
                                       font=("Arial", "14", "bold"), width=12,
                                       command=self.to_help)
        
        self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        """
        Opens help dialogue box and disables help button (So users don't create multible boxes)
        """
        DisplayHelp(self)

class DisplayHelp:

    def __init__(self, partner):
        
        # setup dialouge box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and releases help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner)) 

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature you wish to convert to either Celsisus or Fahrenheit \n"\
                    "Note that -273C and -459F, if you try to convert a temperature lower than these values, you will get an error message\n"\
                    "To see your calculation history and export it as a text file, please click the 'History / Export' button." 

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", 
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]
        
        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
