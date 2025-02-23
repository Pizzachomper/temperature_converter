all_calculations = ['Converting 10.0F is -12C', 'Converting 20.0F is -7C',
                    'Converting 30.0F is -1C', 'Converting 40.0F is 4C',
                    'Converting 50.0F is 10C', 'Converting 60.0F is 16C']

newest_first = list(reversed(all_calculations))

print("==== Oldest to Newest for File ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ====")
for item in newest_first:
    print(item)

