# 1) Copy and paste the block of the code from markdown (.md) file and type out what you observe happens when you run your program.
#What happens when you respond with "yes"? What happens when you respond with "no"? What if you respond with something completely different?
#Use a hashtag(#) to type out your answers.







# 2) Here is the exact same code, but there is an error that doesn't allow it to run how you want it to. Uncomment it and fix the error!
#HINT: Spacing and indentation matters! Code located at the same indentation position is considered to be in the same "block" of code
#HINT 2: 4 spaces is the same as one tab. Code inside of an IF statement needs to be indented!
'''
answer = input("Are you hungry? ")

if answer == "yes":
print("I made you some lunch!")
  
if answer == "no":
print("I'll put your food in the fridge until you're ready!")
'''   

# 3) You can have multiple lines of code inside of each conditional IF statement. Try adding a couple more print statements to the end
#of each conditional statement (make sure they are indented as well!):
      
      
      
      
      
      
# 4) Conditions help us compare things! We compare things by using RELATIONAL OPERATORS! Did you notice we are using a
#double equals (==) sign? This is fundamentally different than using one equals sign. Remember, using one equals sign is how we create a variable.
#Observe the code below:
x= "hello"
print(x)
#What printed to the console?


#Uncomment the line below and run it. What prints to the console now? What if you change "hello" to a different word? What if you changed it from all lower case letters to all capital letters?
#print(x=="hello")



# 5) There are some other relational operators as well. Uncomment the lines of code below with print functions one at a time and change the number in the print function so it prints True instead of False
number = 10

# == asks is the thing on the left EXACTLY EQUAL TO the thing on the right??
#print(number == 1000)

# > asks is the thing on the left GREATER THAN the thing on the right??
#print(number > 50)

# < asks is the thing on the left LESS THAN the thing on the right??
#print(number < 2)

# >= asks is the thing on the left GREATER THAN OR EQUAL TO the thing on the right??
#print(number >= 10.1)

# <= asks is the thing to the left LESS THAN OR EQUAL TO the thing on the right??
#print(number <= 9.9)

# != asks is the thing on the left NOT EQUAL TO the thing on the right??
#print(number != 10)


# 6)Uncomment the code below to find and correct the error!
'''
age = input("How old are you?")

if age > 18:
  print("Wow, are you in college?")

if age <= 18:
  print("That's cool! Do you go to Viewpoint?")
'''


#Bonus Questions:

# 1) Suppose I use the input function to ask the user this question: Do you like pizza?
# Uncomment the code and change it so the print functions work regardless of whether or not the user types out yes, YES, Yes, yEs, yeS, no, NO, nO, or No as their answer.
'''
pizza = input("Do you like pizza? ")

if pizza == 'yes':
  print("Me too! I love pizza!")
  print("My favorite topping is pepperoni!")
  
if pizza == 'no':
  print("Pizza is overrated anyway.")
  print("I'd rather have tacos instead.")
'''


# 2) Do the same thing for the following block of code:
'''
pizza = input("Do you like pizza? ")

if pizza == 'YES':
  print("Me too! I love pizza!")
  print("My favorite topping is pepperoni!")
  
if pizza == 'NO':
  print("Pizza is overrated anyway.")
  print("I'd rather have tacos instead.")
'''



