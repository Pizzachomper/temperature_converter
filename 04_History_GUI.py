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
        # setup dialouge box and background colour

        green_back = "#D5E8D4"
        peach_back = "#ffe6cc"
        
        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at top, closes history and releases history button
        self.history_box.protocol('WH_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # strings for long tasks 
        recent_intro_txt = ("Below are your recent calculations - showing "
                            "3/3 calculations. All calculations are shown to the nearest degree")

        export_instructions_txt = ("Please push <export> to save your calculations in file."
                                   "If the filename already exsists, it will be replaced.")

        calculations = ""

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            ["calculation list", ("Arial", "14"), green_back],
            [export_instructions_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1], 
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # Retrieve export instruction label so that we can configure it to show the filename if the user exports to file
        self.ex

    def close_history(self, partner):
        pass


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
