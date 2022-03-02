import tkinter as tk
from TeamChooser import Team_Chooser
window = tk.Tk()
greeting = tk.Label(text="The Group Chooser 5000")


question_grade= tk.Label(text="Which class would you like to make groups for?")
grade_entry=tk.Entry()
grade=grade_entry.get()

question_num_groups= tk.Label(text="How many groups would you like to make?")
num_groups_entry=tk.Entry()
num_groups=num_groups_entry.get()


greeting.pack()

question_grade.pack()
grade_entry.pack()
question_num_groups.pack()
num_groups_entry.pack()
button = tk.Button(
    text="Determine Groups",
    width=25,
    height=5,
    bg="blue",
    fg="black",
command=Team_Chooser(grade,num_groups))
button.pack()
window.mainloop()


