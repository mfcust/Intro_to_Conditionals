# What is a conditional statement??
It's basically like a yes or no question; there are only two possibilities. If I were to ask you, "Are you hungry?" you could ultimately respond one of two ways. You could say "Yes" or "No." Then, I can respond based on your answer. If you _are_ hungry, I can respond by saying "I made you some lunch!" If you _aren't_ hungry, I can say "I'll put your food in the fridge until you're ready!" My response depends on whether or not the statement "You are hungry" is either _true_ or _false_.

Let's think about how to structure that logic in English below:
**_If_** you _**are**_ hungry:
        then I respond by saying "I made you some lunch!"
**_If_** you _**aren't**_ hungry:
        then I respond by saying "I'll put your food in the fridge until you're ready!"
        
In Python, we can simulate this scenario by asking the user a question, and storing the answer as a variable. Then, depending on the answer, we can print a response to the output window. Let's see how this looks in Python code:
```
answer = input("Are you hungry? ")

if answer == "yes":
  print("I made you some lunch!")
  
if answer =="no":
  print("I'll put your food in the fridge until you're ready!")
  ```
Copy and paste this code into your .py file and see what happens when you type in "yes" or "no" in response to your input question.

This is a basic example of what a conditional statement is! Navigate to your Python file to learn more about them!
