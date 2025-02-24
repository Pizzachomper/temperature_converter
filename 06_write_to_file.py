from datetime import date

calculations = ['Converting 10.0F is -12C', 'Converting 20.0F is -7C',
                'Converting 30.0F is -1C', 'Converting 40.0F is 4C',
                'Converting 50.0F is 10C', 'Converting 60.0F is 16C']

# Get current date for heading and filename
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"temperature_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("*** Temperature calculations ***\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")