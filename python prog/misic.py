from tkinter import *



root = Tk()
root.title("Hello codeby!")
root.resizable(width=False, height=False)

C = Canvas(root, bg="blue", height=330, width=500)
filename = PhotoImage(file = "C:\\black_blue.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#zapis = "\n Hello\n codeby!\n"
label2 = Label(text=zapis, justify=LEFT, fg="#D3D3D3", bg="#000000", font="Serif 24", padx=5, pady=2)
label2.place(relx=.1, rely=.1)

hello = "\n Привет КулХацкерам \n\n форума codeby!\n"
end = Label(text=hello, justify=LEFT, fg="#FF0000", bg="#000000", font="Arial 12", padx=5, pady=1)
end.place(relx=.1, rely=.5)




C.pack()
root.mainloop
