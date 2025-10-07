#****************************************
#      TOP SECRET - AGENT DOSSIER
#****************************************

#Codename:   [Agent's Codename]
#Real Name:  [Agent's Real Name]
#Gadget:     [Assigned Gadget]

#----------------------------------------
#MISSION DETAILS:
#Operation ID:   OP-[Operation Number]-[Agent's Codename]
#Location:       [Mission Location]
#----------------------------------------
#       *** FOR YOUR EYES ONLY ***
#****************************************

print("Welcome to top secret agent dossier.")
codename = input ("What is your codename?\n")
real_name= input ("What about your real name?\n")
item =input("Enter your assigned gadget.\n")
op = input("Enter your operation number.\n") 
location = input("Where is your mission location?\n")

print("\n\n\n*****************************************")
print("         TOP SECRET - AGENT DOSSIER        ")
print("*****************************************\n\n")
print(f"Codename:   {codename}")
print(f"Real name:  {real_name}")
print(f"Gadget:     {item}")
print("----------------------------------------\n\n\n")
print("MISSION DETAILS:")
print(f"Operation ID:  OP-{op}-{codename}")
print(f"Location:      {location}")  
print("----------------------------------------")
print("        *** FOR YOUR EYES ONLY ***      ")
print("****************************************\n\n\n")