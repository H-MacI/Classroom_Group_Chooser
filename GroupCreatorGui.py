import tkinter as tk
import tkinter.messagebox
from TeamChooser import Team_Chooser

#
#
#window = tk.Tk()
#greeting = tk.Label(text="The Group Chooser 5000")
#
#
#question_grade= tk.Label(text="Which class would you like to make groups for?")
#grade_entry=tk.Entry()
#grade=grade_entry.get()
#print(type(grade))
#question_num_groups= tk.Label(text="How many groups would you like to make?")
#num_groups_entry=tk.Entry()
#num_groups=num_groups_entry.get()
#button = tk.Button(
#    text="Determine Groups",
#    width=25,
#    height=5,
#    bg="blue",
#    fg="black",command=print('hi'))
#    #command=Team_Chooser(grade,num_groups))
#
#
#greeting.pack()
#
#question_grade.pack()
#grade_entry.pack()
#question_num_groups.pack()
#num_groups_entry.pack()
#button.pack()
#window.mainloop()
#
#


class Group_Creator(tk.Tk):


    def __init__(self):
    
        super().__init__()
        #Window Title and Size
        self.title("Group Creator 5000")
        self.geometry('300x500')
        
        #Create label
        self.label = tk.Label(self, text="How many groups?")
        self.label.pack()
        
        #Create Button
        self.button = tk.Button(self, text="Create Groups")
        self.button['command']=self.button_clicked
        self.button.pack()
        
        
    def button_clicked(self):
        tk.messagebox.showinfo(title="Information", message="Hello")


if __name__=="__main__":
    create=Group_Creator()
    create.mainloop()
