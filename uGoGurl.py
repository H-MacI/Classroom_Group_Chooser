import tkinter as tk
from TeamChooser import Team_Chooser

# Initialize
heather = tk.Tk()

# Declare integer variables
grade_var      = tk.IntVar()
num_groups_var = tk.IntVar()

# Function that calculate shits
def run():

    grade      = grade_var.get()
    num_groups = num_groups_var.get()
    print(grade, num_groups) # For debugging

    Team_Chooser(grade, num_groups)

## GUI stuff
greeting = tk.Label(text="The Group Chooser 5000")
question_grade      = tk.Label(text = "Which class would you like to make groups for?")
grade_entry         = tk.Entry(textvariable = grade_var)

question_num_groups = tk.Label(text = "How many groups would you like to make?")
num_groups_entry    = tk.Entry(textvariable = num_groups_var)

# Button to submit and calculate data
button = tk.Button(heather, text="<3", command = run)

# Other way of setting up does not need 'pack()' but this will do
greeting.pack()
question_grade.pack()
grade_entry.pack()
question_num_groups.pack()
num_groups_entry.pack()
button.pack()


# Main loop
heather.mainloop()
