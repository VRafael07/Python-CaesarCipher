import tkinter as tk
from cipher import *


root = tk.Tk()
root.title("Caesar Cipher")


def getResults():
    rawText = textEntry.get()
    mode = v.get()
    key = int(keyRange.get())
    translated = getCriptography(mode, rawText, key)
    result.set(translated)


# Radiobutton where the mode will be defined
MODES = [
    ("Encrypt", 1), ("Decrypt", 2), ("Brute Force", 3)
    ]
rowNumber = 1
v = tk.IntVar()
modeLabel = tk.Label(
    root,
    text="Mode:",
    font="Helvetica 14 bold",
    foreground="black"
    ).grid(
        row=0,
        column=0
    )
for text, mode in MODES:
    b = tk.Radiobutton(
        root,
        text=text,
        font="Helvetica 13",
        foreground="black",
        variable=v,
        value=mode
    ).grid(
        row=rowNumber,
        column=0,
        sticky=tk.W
        )
    rowNumber += 1

# Spinbox where the key value will be defined
keyLabel = tk.Label(
        root,
        text="Encryption/Decryption Key:",
        font="Helvetica 14 bold"
        ).grid(
        row=0,
        column=1)
keyRange = tk.Spinbox(
    root,
    from_=1,
    to=26,
    width=3
    )
keyRange.grid(
    row=1,
    column=1)

# Entry label where the message will be inserted
textLabel = tk.Label(
    root,
    text="Message:",
    font="Helvetica 14",
    foreground="black"
    ).grid(
        row=2,
        column=1,
        pady=2)
textEntry = tk.Entry(root)
textEntry.grid(
    row=3,
    column=1
    )

# Button that will start the cryptography
finalButton = tk.Button(
    root,
    text="Send",
    font="Helvetica 14 bold",
    foreground="black",
    width=10,
    command=getResults
    ).grid(
        row=3,
        column=2,
        sticky=tk.W+tk.E
        )

# Label where the result will be showed
result = tk.StringVar()
result.set("")
outputLabel = tk.Label(
    root,
    textvariable=result,
    font="Helvetica 13",
    foreground="black",
    relief='flat',
    bd=0,
    takefocus=0,
    highlightthickness=0
    ).grid(
        row=4,
        columnspan=4)


root.mainloop()
