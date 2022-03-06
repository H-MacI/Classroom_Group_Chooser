import tkinter as tk
from TeamChooser import Team_Chooser

# Initialize
heather = tk.Tk()
heather.title("TheGroupGenerator5000")
# Declare integer variables
grade_var      = tk.IntVar()
num_groups_var = tk.IntVar()
groups = tk.StringVar()
# Function that calculate shits
def run():
    # Gets input from user
    grade      = grade_var.get()
    num_groups = num_groups_var.get()
    print(grade, num_groups) # For debugging
    # Creates Groups
    groups=Team_Chooser(grade, num_groups)
    # Displays Groups in new window
    newwin = tk.Toplevel(heather)
    newwin.title('Groups')
    
    for i in range(num_groups):
        w1 = tk.Label(newwin, text="Group "+str(i+1))
        w2= tk.Label(newwin, text=str(groups[i]))
        w1.pack()
        w2.pack()



## GUI stuff
greeting = tk.Label(text="The Group Generator 5000")
question_grade      = tk.Label(text = "Which class would you like to make groups for?")
grade_entry         = tk.Entry(textvariable = grade_var)

question_num_groups = tk.Label(text = "How many groups would you like to make?")
num_groups_entry    = tk.Entry(textvariable = num_groups_var)

# Button to submit and calculate data
button = tk.Button(heather, text="Create Groups", command=run)

# Other way of setting up does not need 'pack()' but this will do
greeting.pack()
question_grade.pack()
grade_entry.pack()
question_num_groups.pack()
num_groups_entry.pack()
button.pack()


# Main loop
heather.mainloop()
