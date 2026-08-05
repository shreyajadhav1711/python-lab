print("---------collage addmision eligibility criteria---------")

age=int(input("enter age:"))
mark=int(input("enter mark:"))
if(age>=17 & age<=25):
   print("you are eligibal by age")

   if(mark>60):
    print("eligibal for addmision")
    
    if(mark>85):
      print("eligibal for aiml")

    elif(mark>75):
      print("eligibal for cse")

    elif(mark>70):
      print("eligibal for mech")



   else:
    print("not eligibal for addmission")

