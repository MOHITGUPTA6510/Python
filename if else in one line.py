a=10
b=100

#simple if else statement
min="a is minimum" if a<b else "b is minimum"
print(min)

#nested if else statement
result="bothe are equal" if a==b else "a is greater" if a>b else "b is greater"
print(result)

# using in tuple
# syntax: (false_value,true_value) [condition]
result1=("b is minimum","a is minimum")[a<b]
print(result1)

#using in dictionary
#syntax : {True: true_value , False:false_value}[condition]
result2={True:"a is minimum" , False:"b is minimum"}[a<b]
print(result2)

#using lambda function
# syntax: (lambda:false_value , lambda:ture_value)[condition]()
result3=(lambda:"b is minimum" , lambda:"a is minimum")[a<b]()
print(result3)

#using print function
# syntax: print(true_value) if (condition) print(false_value)
print("a is minimum") if (a<b) else print("b is minimum")
