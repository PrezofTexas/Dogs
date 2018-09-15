def main():
    dogs = []
    print ("This application, using SCIENCE, can help determine the optimal number of dogs for your household. Each question has been carefully tested.  Please answer as accurately as possible.")
    name = str(input("Please enter your last name:  "))
    
    havedogs = str(input("Do you have a dog? 'Yes' or 'No'?  "))
    if havedogs == "Yes":
        numdogs = int(input("How many dogs do you have in your household?  "))
        i=0
        for i in range (numdogs):
            x = str(input("Enter the dog:"))
            if x not in dogs:
                dogs.append(x)
                print (dogs)
            else:
                print ("Dog is already in the list.")
        i += 1
    elif havedogs == "No":
        print ("The", name, "household does not have any dogs.")
    
    
      
    #Can this person hand a new dog?
    age = int(input("Please enter your age:  "))
    if age <= 17:
        print ("For best accuracy, please be 18 before ordering a new dog.")
  
    house = str(input("Do you own your own home or do you rent? 'Own' or 'Rent' or 'None'?  "))

    children = int(input("How many children live in your household?  "))
    
    married = str(input("Are you married? T or F "))
    if married == 'T':
        s = int(input("How many dogs could your spouse accept before leaving you?"))
           
  
    #Determining the optimal number of dogs for the household.
    if married == 'T':
        OptDogs = s-1
    else:
        OptDogs = numdogs +1
      
    
   
    print ("The optimal number of dogs for your household has been scientifically calculated to be", OptDogs, ". ")      

        
    
 
if __name__ == '__main__': main()
