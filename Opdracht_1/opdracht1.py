
#%%
#Opgave 1A, tijds omzetting 
#def Tijdsomzetting():
#voer de tijd in bij uren, minuten en seconden.
Tijd_Invoer_Uren = 74
Tijd_Invoer_Minuten = 23
Tijd_Invoer_Seconden = 12

Tijd_Totaal_Seconden = Tijd_Invoer_Uren*3600 + Tijd_Invoer_Minuten*60 + Tijd_Invoer_Seconden

Tijd_Uitvoer = Tijd_Totaal_Seconden
print (Tijd_Uitvoer)


#    if __name__ == "__Tijdsomzetting__":
#        Tijdsomzetting()

#%%
# Opgave 1A verbeterd
def tijd_Omzetting(Uren,Minuten,Seconden):
    return (Uren*3600) + (Minuten*60) + Seconden

# %%
#Opgave 1B
def tijd_Omzetting_Inverse(Invoer_Seconden):
    Minuten, Seconden = divmod( Invoer_Seconden, 60)
    Uren, Minuten = divmod(Minuten, 60)

    return (Uren, Minuten, Seconden)

# %%
#Opgave 1C
#Testen uitgevoerd, werken naar behoren.

#%%
#Opgave 2A
