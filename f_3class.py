class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name} age: ({self.age})"

p1= person("john",23)

#we cange the name the value 
p1.name="Mohit"

#we delete the thing or the whole class object
#del p1.age



print(p1)
