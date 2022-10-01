from lift import Lift

# objecten van type Lift:
lift0 = Lift(-2,10,1,2)  # langzame lift
lift1 = Lift(-2,10,0.8,1.0) # snelle lift


#%%
liften = []
liften.append(Lift(0,10,1,1))
liften.append(Lift(0,10,0.5,0.2))
liften.append(Lift(0,10,0.5,0.2))
liften.append(Lift(0,10,0.5,0.2))


# utility functions
def printLiften(lift_lijst):
    for index,lift in enumerate(lift_lijst):
        print("Lift nummer: ",index)
        lift.printPositie()
        lift.printDeur()
        print("") # eindig met lege regel

# def returnStatus(lift_lijst):
#     ret = []
#     for lift in lift_lijst:
#         ret.append([lift.positie, lift.deur_open])
#     return ret


