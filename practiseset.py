marks1= int(input("enter the  number marks 1:"))
marks2= int(input("enter the number marks 2:"))
marks3= int(input("enter the number marks 3:"))
total_percentage = (100*(marks1 +  marks2  +  marks3))/300

if (total_percentage >= 40 and marks1>33 , marks2>33 , marks3>33):
    print("you are pass" , total_percentage)
else:
    print("try next year", total_percentage)   
