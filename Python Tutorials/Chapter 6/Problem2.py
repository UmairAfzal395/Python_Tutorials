subject1 = int(input("Enter a number of subject 1:"))
subject2 = int(input("Enter a number of subject 2:"))
subject3 = int(input("Enter a number of subject 3:"))

total_percentage =(100*(subject1+subject2+subject3))/300

if(total_percentage>40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("You are passed.",total_percentage)

else:
    print("You are failed.",total_percentage)
