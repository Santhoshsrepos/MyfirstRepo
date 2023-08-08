score=int(input("Enter the mark: "))
if(score<35):
    print("Poor student")
elif(score>=35 and score<70):
    print("Average student")
elif(score>=70 and score<100):
    print("Good student")
elif(score==100):
    print("Excellent")
else:
    print("Invalid mark")