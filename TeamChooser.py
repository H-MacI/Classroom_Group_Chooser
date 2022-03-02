import pandas as pd
import random
import numpy as np
def Team_Chooser():
    #random.seed(10)
    ##Import List of Student
    CSV=pd.read_csv("7ClassList.csv")
    Names=CSV["Names"]
    restrict=['Ava','Olivia']
    #Declare List of Groups

    while True:
        try:

            numTeams=int(input("How many teams would you like? "))
        except ValueError:
            print("Number of teams must be an integer number")
            #better try again... Return to the start of the loop
            continue
        else:
            #successfully parsed!
            #we're ready to exit the loop.
            break
    any_trues=True
    while any_trues:
            test_results=[]
            shuffled_names=sorted(Names.values, key=lambda k: random.random())
            #print(shuffled_names)


            groups=np.array_split(np.array(shuffled_names),numTeams)
            groups_df=pd.DataFrame(list(map(np.ravel, groups)))
            
            #print(groups_df)
            
            ##Check if restrictions occured.## Ex Ava and Olivia can't be in the same group
            for i in range(len(groups_df.index)):
                #print(groups_df.iloc[i])
                test=all(x in groups_df.iloc[i].to_numpy() for x in restrict)
                test_results.append(test)
            #print(test_results)
            groups_df["Test"]=test_results
            any_trues=True in test_results
            


    for i in range(numTeams):
        print("Group ",i+1)
        print(groups[i])

    return()
Team_Chooser()
