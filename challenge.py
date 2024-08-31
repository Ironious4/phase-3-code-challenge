#Question 1
def add_numbers(num1, num2):
   return num1+num2  
print(add_numbers(num1=40, num2=20)) #Calling the function and printing the sum


#Question 2
def is_even(number):
    return number%2==0
print(is_even(number=4)) #Calling the function and printing whether the given number is even
    

#Question 3
def reverse_string(text):
    return text[::-1] #Returning the reversed version of the input string

message=reverse_string('Write backwards') #Reversing the string and storing the result in message variable

print(message)


#Question 4
text='open' #The text where number of vowels are counted
vowels='aeiouAEIOU' #A string containing all vowels in lowercase and uppercase

def count_vowels(text):
 return
count=sum(text.count(vowel) for vowel in vowels) #Calculating the number of vowels in the text
print(count)


#Question 5  
def calculate_factorial(n):
   return 1 if (n==1 or n==0) else n*calculate_factorial(n-1) #Calculating the factorial of a number

print(calculate_factorial(n=5))


#Question 6
def apply_decorator(func):
    def decorator_func(): #Function that prints 'Decorator Applied' before executing the original function
        print('Decorator Applied')
        return func() #Calling the original function
    return decorator_func() #Returning the decorated function

def already_decorated(): 
   print('Its Decorated')
already_decorated=apply_decorator(already_decorated) #Applying the decorator to the already_decorated function


#Question 7
people=[('Bob', 40),('Mosh', 35),('Mike', 30)] #List of tuples containing names and ages

def sort_by_age(age):
    return age[1] #Returning the age from a tuple to use as a sorting key

people.sort(key=sort_by_age) #Sorting the list of people by age using sort_by_age function as the key
print(people)


#Question 8
def merge_dicts():
  dict1={'a':50, 'b':80}
  dict2={'x':30, 'y':25}
  result=dict1|dict2 #Merging dict1 and dict2 using the union operator
  return result

dict3=merge_dicts() #Merging the dictionaries and storing the result in dict3
print(dict3)


#Question 9
class Car:
   def __init__(self, make, model, year): 
       #Initializing make, model and year attributes
       self.make = make
       self.model = model
       self.year = year

   def display_info(self):
       print(f'Car info:{self.make}, {self.model}, {self.year}') #Printing car information

my_car=Car('Mitsubishi', 'Colt', 2024) #Creating an instance of the Car class

my_car.display_info() #Calling the display_info method to print the car's information













    
    



    





