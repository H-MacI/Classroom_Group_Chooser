import tkinter as tk
from TeamChooser import Team_Chooser
window = tk.Tk()
greeting = tk.Label(text="The Group Chooser 5000")
button = tk.Button(
    text="Determine Groups",
    width=25,
    height=5,
    bg="blue",
    fg="black",
)

question_grade= tk.Label(text="Which class would you like to make groups for?")
grade_entry=tk.Entry()
grade=grade_entry.get()



greeting.pack()
button.pack()
question_grade.pack()
grade_entry.pack()


window.mainloop()
#Team_Chooser(grade)


#ws = tk.Tk()
#ws.title("Team Chooser")
#ws.geometry('400x300')
#ws['bg'] = '#ffbf00'
#
#def getClassName():
#    classname = class_name.get()
#    tk.Label(ws, text=f'Making groups of Grade {classname} students!', pady=20, bg='#ffbf00').pack()
#
#
#class_name = tk.Entry(ws)
#class_name.pack(pady=30)
#
#tk.Button(
#    ws,
#    text="Which class would you like to make groups for?",
#    padx=10,
#    pady=5,
#    command=getClassName
#    ).pack()
##print(str(class_name.get()))
##Team_Chooser(classname.str())
#ws.mainloop()

