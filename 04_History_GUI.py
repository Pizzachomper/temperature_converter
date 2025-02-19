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

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        Opens history dialouge box and disables history button (so that users can't create multiple history boxes)
        """
        HistoryExport(self)


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner):
        pass

    def close_history(self, partner):
        pass


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
