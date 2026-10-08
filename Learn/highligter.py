from tkinter import * # type: ignore

root = Tk()

text_box = Text(root, height=10, width=30)
text_box.pack()

def highlight():

    try:
        start = text_box.index(SEL_FIRST)
        end = text_box.index(SEL_LAST)

        text_box.tag_add("color", start, end)
        text_box.tag_config("color", background="yellow")

    except:
        print("Please select text")

Button(root, text="Highlight", command=highlight).pack()

root.mainloop()