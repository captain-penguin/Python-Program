#2nd Task
grades = {}

while True:
    print("\n1. Type '1' to Add/Update Student Grade")
    print("2. Press 'Any Key' Other than '1' to 'Exit' to see all stored data results in dictionary")
    entry=str(input("\nEnter Choice: ").strip())
    if entry=="1":
        name = str(input("\nEnter student name: ").strip())
        while name=="":
            print("'Name' input cannot be empty")
            name = str(input("\nEnter student name: ").strip())
        for key in grades.keys():
            if name.lower() in key.lower():
                temp=grades[key]
                print(f"\n'{name}', is already present in data")
                print("\n 1. Type '1' if you want to 'skip' this entry \n 2. Type'2' if you want to update the 'Grades'")
                Choice = str(input("\nEnter Your Choice: ").strip())
                if Choice=="2":
                    grade = str(input("\nEnter student grade: ").strip())
                    while grade=="":
                        print("Grade input cannot be empty")
                        grade = str(input("\nEnter student grade: ").strip())
                    grades[key]=grade
                    print(f"\nupdated.... '{name}'s' grade Value '{temp}' replaced with the latest input Grade'{grade}'")
                    break
            
                else:
                    print(f"\nThe 'Grade' input entry has been skipped.....")
                    break
        else:
            grade = str(input("\nEnter student grade: ").strip())
            while grade=="":
                        print("'Grade' input cannot be empty")
                        grade = str(input("\nEnter student grade: ").strip())
            grades[name]=grade

    else:
        break
    
for student, grade in grades.items():
    print(f"{student}: {grade}")