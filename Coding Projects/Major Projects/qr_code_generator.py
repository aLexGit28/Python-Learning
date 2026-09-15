# QR Code Generator using Tkinter

from tkinter import * # type: ignore
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Create window
root = Tk()
root.title("QR Code Generator")
root.geometry("700x600")
root.config(bg="deeppink")

# Function to generate QR code
def generate_qr():

    text = text_entry.get()
    filename = file_entry.get()

    if text == "" or filename == "":
        messagebox.showerror("Error", "Please enter all details")
    
    else:
        # Create QR code
        qr = qrcode.make(text)

        # Save QR code
        qr.save(filename + ".png") # type: ignore

        # Open and resize image
        img = Image.open(filename + ".png")
        img = img.resize((250, 250))

        # Convert image for tkinter
        img_tk = ImageTk.PhotoImage(img)

        # Show image on label
        qr_label.config(image=img_tk)
        qr_label.image = img_tk # type: ignore

        # Success message
        save_label.config(text="File Saved Successfully!")

# Heading
heading = Label(root,
                text="QR Code Generator",
                font=("Arial", 24, "bold"),
                bg="deeppink",
                fg="white")
heading.pack(pady=20)

# Text input
text_label = Label(root,
                   text="Enter the Text :",
                   font=("Arial", 16, "bold"),
                   bg="deeppink")
text_label.pack()

text_entry = Entry(root,
                   font=("Arial", 14),
                   width=35)
text_entry.pack(pady=10)

# File name input
file_label = Label(root,
                   text="File Name (Save As) :",
                   font=("Arial", 16, "bold"),
                   bg="deeppink")
file_label.pack()

file_entry = Entry(root,
                   font=("Arial", 14),
                   width=35)
file_entry.pack(pady=10)

# Button
generate_btn = Button(root,
                      text="Generate QR Code",
                      font=("Arial", 14, "bold"),
                      bg="white",
                      command=generate_qr)
generate_btn.pack(pady=20)

# QR image label
qr_label = Label(root, bg="white")
qr_label.pack(pady=10)

# Save message
save_label = Label(root,
                   text="",
                   font=("Arial", 14, "bold"),
                   bg="deeppink",
                   fg="black")
save_label.pack()

# Run window
root.mainloop()