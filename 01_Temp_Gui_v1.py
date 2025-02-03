from tkinter import *

class Converter():
    """
    Temperature conversion tool (C° to F° or vise versa)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "24", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press one of the buttons below to convert it from degrees to farenheit"
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=150, width=40,
                                       justify="left",
                                       font=("Arial", "12"))
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14"))

        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_entry = Label(self.temp_frame, text=error,
                                fg="#9C0000")
        self.temp_entry.grid(row=3)

        # Conversion, help and history / export buttons
        self.buttonframe = Frame(self.temp_frame)
        self.buttonframe.grid(row=4)

        self.to_celcius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg="fffffff",
                                        font=("Arial", "12","bold"), width=12)
        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

