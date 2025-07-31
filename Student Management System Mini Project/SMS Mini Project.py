students = {}

while True:
    print()
    print("---------------------------------------------------------------------------------")
    user_option = input('''                        
Please Choose one of the following options:
                         
       --> To add new Student details [PRESS 1]: 
                        
       --> To View Student information [PRESS 2]: 
                        
       --> To Update Student Information [PRESS 3]:
                        
       --> To del Student Information [PRESS 4]:
                        
       --> To Exit, Simply [PRESS 5]: 
                        
---------------------------------------------------------------------------------
''')
    
    if user_option == '1':
        print()
        roll = input("Enter Roll Number: ")
        if roll in students:
            print()
            print("Roll Number Already Exists. Please Try New Roll Number. ")
        else:
            Name = input("Please Enter Student Name: ")
            Age = int(input("Please Enter Student Age: "))
            Marks = int(input("Please Enter Student Marks: "))
            Grade = input("Please Enter Student Grade: ")
            students[roll] = {'Name':Name, 'Age':Age, 'Marks':Marks,'Grade':Grade}
            print()
            print("All the Details are Successfully stored.")

    elif user_option == '2':
        print()
        roll = input("Enter Roll Number: ")
        print()
        if roll in students:
            print("Name:", students[roll]['Name'])
            print()
            print("Age:", students[roll]['Age'])
            print()
            print("Grade:", students[roll]['Grade'])
            print()
            print("Marks:", students[roll]['Marks'])
            print()            
        else:
            print(f"Sorry, Roll Number - {roll} not Exists")
    
    elif user_option == '3':
        print()
        roll = input("Enter Student Roll Number to update: ")
        if roll in students:
            print("What do you want to update?")
            print("For Name  --> Press [1] ")
            print("For Age   --> Press [2] ")
            print("For Grade --> Press [3] ")
            print("For Marks --> Press [4] ")
            updated_choice = input("Enter your updated choice [1-4]: ")

            if updated_choice == '1':
                New_Name = input("Enter updated Name: ")
                students[roll]['Name'] = New_Name
                print("New Name is now updated successfully")
            elif updated_choice == '2':
                New_Age = input("Enter updated Age: ")
                students[roll]['Age'] = int(New_Age)
                print("New Age is now updated successfully")
            elif updated_choice == '3':
                New_Grade = input("Enter updated Grade: ")
                students[roll]['Grade'] = New_Grade
                print("New Grade is now updated successfully")
            elif updated_choice == '4':
                New_Marks = input("Enter updated Marks: ")
                students[roll]['Marks'] = int(New_Marks)
                print("New Marks are now updated successfully")
            else: 
                print("Invalid Option! Sorry, Try Again.")
            
    elif user_option == '4':
        print()
        roll = input("Enter Students Roll Number to delete: ")
        if roll in students:
            del students[roll]
            print()
            print("Roll Number is now successfully deleted")
        else:
            print()
            print("Sorry, Roll Number not Found. Try again!")
    elif user_option == '5':
        print()
        print("Thank you, It was a great time. Please come back again")
        print()
        break

    else:
        print()
        print("Invalid option. Please Try again!")




        


    