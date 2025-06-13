list_spisok = [10, 20, 30, 40]

interator = iter(list_spisok)

print(next(interator))
print(next(interator))
print(next(interator))
print(next(interator))



x= 5
def myfunction999():
    x = 25
    print("inside function x = ", x)

myfunction999()
print("outside function x = ", x)



x = 12
def myfunction12():
    global x 
    x = 10
    print("global modified" , x)

myfunction12()
print("after global change", x)    

import random
random_int = random.randint(1, 100)
print("Random num from 1 to 100: ", random_int)



from datetime import datetime  
pyatnica13 = datetime.now()        
print(pyatnica13.strftime("%d-%m-%Y"))  



from datetime import date  
today = date.today() 

happy_birthday = date(today.year, 8, 20) 

if happy_birthday < today: 
    happy_birthday = date(today.year + 1, 8, 20)  
print((happy_birthday - today).days,'days until birthday')

import json  
student = {
    "name": "Alexander",
    "age": 20,
    "GPA": 3.0
}

json_data = json.dumps(student) 
print(json_data)




json_stroka= '{"course": "Python", "level": "beginner"}'  
inform = json.loads(json_stroka) 
print(inform["course"])  
