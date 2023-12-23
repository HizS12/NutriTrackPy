'''
     This Python system is a comprehensive food tracking and chopping system 
     designed to help users manage their daily calorie intake and nutrition issues.
     The application allows users to keep a record of the foods they ate by 
     adding, saving and displaying meals with their respective calorie counts.
     Also, it provides functions for calculating and displaying daily calorie
     intake, calories left to meet a set goal, and basically nutrition
     information for each meal, e.g protein, fat, and carbohydrate levels based
     on added calories . Users interact with the system through an easy-to-use 
     menu interface, access options to perform various tasks such as viewing food
     information, editing notes, text written to a file, and exiting the program 
     Use file operations, conditional statements, loops, activities, . with user 
     feedback, this system feeds users Provides a versatile tool for monitoring,
     tracking calorie intake and gaining insight into the nutritional components
     of their meals, and by has improved the quality of health care
                                                                                     '''


def meal_add(meallog,mealname,countofcalories):
    if mealname in meallog:
        print("Meal already exists.Updating calorie count.")
        
   # Updating the calorie count for an existing meal
   
    meallog[mealname] = countofcalories
    print(f"{mealname} with {countofcalories} calories added to log.")
    
   # Adds a new meal entry to meal log

def dailycaloriesdisplay(meallog):
    if not meallog:
        print("no meals logged yet")
    else:
        totalcalories=sum(meallog.values())
        print(f"Daily calorie intake: {totalcalories} calories")
        
   # Displays the total (daily) calorie intake based on the provided meal

def remainingcalories(meallog, dailygoal):
    
   # It indicates if the goal has been exceeded or if there are remaining calories within the goal.

    if not meallog:
        print("No meals Logged yet.")
    else:
        totalcalories=sum(meallog.values())
        remaining = dailygoal - totalcalories
        if remaining < 0:
            print(f"Goal exceeded by {remaining} calories")
        else:
            print(f"Remaining calories for the day: {remaining} calories")
            
   # Displays the remaining calories for it to meet the daily goal based on the provided meal 

def cal_nutrition(meallog, mealname):
    
   # Checking if the specified meal is in the meal log
    
    if mealname in meallog:
        caloriecount=meallog[mealname]
        
   # Calculating the nutritional information based on assumed percentages
    
        protien=caloriecount * 0.25   # Assuming 25 percent of calories are from protien
        fat=caloriecount * 0.15   # Assuming 15 percent of calories are from fat
        carboh= caloriecount*0.6   # Assuming 60 percent of calories are frm carbohydrates
        
        print(f"Nutritional information for {mealname}:")
        print(f"Calories: {caloriecount}")
        print(f"Protien: {protien} grams")
        print(f"Fat: {fat} grams")
        print(f"Carbohydrates: {carboh} grams")
    else:
        print(f"Meal '{mealname}' not found in the log.")

def savemeallog(meallog, filename):
    try:
        
   # Attempt to open the specified file in write mode.
    
        with open(filename, 'w') as file:
            file.write("Meal Log:\n")
            for meal, calories in meallog.items():
                file.write(f"{meal}: {calories} calories\n")
        print(f"Meal log saved to '{filename}' file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error occored while saving the file: {e}")
        
   #  Saves the meal to a specified file

def displaymeallog(meallog):
   # Printing each meals name and its calorie count from the meal log
    if not meallog:
        print("No meals logged yet.")
    else:
        print("Meal log:")
        for meal, calories in meallog.items():
            print(f"{meal}: {calories} calories")
            
   # Displays the contents of the meal 

def editmeal(meallog, mealname):
   # Edits the calorie count for a specific meal in the meal log
    if mealname in meallog:
        newcalories=int(input(f"Enter new calorie count for {mealname}:"))
        meallog[mealname]=newcalories
        print(f"{mealname} calories updated to {newcalories} calories")
    else:
        print(f"Meal '{mealname}' not found in the log.")
   
   # Prompts the user for new calorie count and updates the log

def readmeallog(filename):
   # Reads the meal log from a specified file
    meallog = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]: 
                meal, calories = line.strip().split(': ')
                meallog[meal] = int(calories.split()[0])
        print(f"Meal log read from '{filename}' file.")
        return meallog
    except FileNotFoundError:
        print(f"Error: File '{filename}' file.")
    except Exception as e:
        print(f"Error occured while reading the file: {e}")
    return meallog

   # Populates a dictionary with meal names and calorie counts

def deletemeal(meallog, mealname):
    if mealname in meallog:
        del meallog[mealname]
        print(f"{mealname} deleted from the meal log.")
    else:
        print(f"Meal '{mealname}' not found in the log.")
   # Deletes a specific meal from the meal log.

def main():
    filename="cps109_a1_output.txt"
    meallog = readmeallog(filename)   
    dailygoal = 2000 
   # Daily calories intaking goal for an average human
    
    while True:
        
   # The following represents the main loop of the Calorie Tracker, displaying the menu options
    
        print("\nCalorie Tracker Menu")
        print("1. Add a Meal")
        print("2. Display Daily Calories")
        print("3. Display Remaining Calories")
        print("4. Calculate Nutritional Information for a Meal")
        print("5. Display Meal Log")
        print("6. Edit a Meal")
        print("7. Delete a Meal")
        print("8. Save Meal Log to File")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")
        
   # As well as handling user input until the user chooses to exit
   # Basically if the user chooses '1', it leads to  meal information and adds it to the meal log
        
        if choice =='1':
            mealname = input("Enter the meal name:")
            caloriecount = int(input("Enter the calorie count for the meal:"))
            meal_add(meallog, mealname, caloriecount)
        elif choice == '2':
            dailycaloriesdisplay(meallog)
        elif choice == '3':
            remainingcalories(meallog, dailygoal)
        elif choice == '4':
            mealname = input("Enter the meal name to calculate the nutritional information:")            
            cal_nutrition(meallog,mealname)
        elif choice == '5':
            displaymeallog(meallog)
        elif choice == '6':
            mealname = input("Enter the meal name you want to edit:")
            editmeal(meallog, mealname)
        elif choice == '7':
            mealname = input("Enter the meal name you want to delete:")
            deletemeal(meallog, mealname)
        elif choice == '8':
            savemeallog(meallog, filename)
        elif choice == '9':
            print("Exiting the program. Take care!!!")
            break
        else: 
            print("Invalid choice. Please enter a valid option.")
if __name__ == "__main__":  # This  statement checks if the script is being run directly as the main program
        main()# Calls the main function to run the code properly