import noteDictionary_v2 as nd

f = open("notelist.txt", "w+")          # Creates a new file named notelist.txt in current directory to store key(s) and value(s) of loop

note = ("C", "C#", "D", "D#", "E", "F", "G", "G#", "A", "A#", "B")
A4 = 440            # Frequency (in hertz) of "Stuttgart pitch"
exp = pow(2, (1/12))
base_Freq = A4*pow(exp, -57)            # Formula to convert A4 to base frequency C0 (C0 is 57 steps behind A4)

for i in range (0, 9, 1):           # loop from C0 to C8
    j = 0
    for element in note:            # loop through keys in "note"
        freq =  base_Freq * (2**(j/12))         # fn = C0 * (2***(n/12))

        key = f"{element}{i}"           # f = formatted string literals
        value = f"{round(freq, 2)} HZ"
        nd.noteDict[key] = value
        # new file formatting
        f.write("\n")
        f.write(key)
        f.write(" ")
        f.write(value)
        j = j + 1


    base_Freq = base_Freq * 2           # eg. C1 = 2 * C0

