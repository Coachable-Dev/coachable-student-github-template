# Week 1 Practice Exercises

## Instructions

1. Make your own copy of the DSA Week 1 Practice Exercises using **"File → Make a Copy"** in Google Docs.
2. Add the copy you just made to your **Coachable Google Drive Folder**. If you do not know how to do this, ask us on Slack.
3. Add a link to your copy in your **Coachable shared Google Drive Notes**.
4. Complete the exercises and fill in your responses inline on your own copy. Your answer should be directly below the question you are answering.
5. Ask questions on Slack if you get stuck on any of the questions.
6. Once you've completed the assignment, let us know on Slack so we can review your responses.

---

## Python Fundamentals and Object-Oriented Programming

### Free Response Questions

1. **What is the difference between a class and an instance?**
   - a. What is a class attribute?
   - b. What is an instance attribute?

2. **Why do we use objects in our code? What are some of the benefits?**

3. **What is the runtime of:**
   - a. `list.pop()`
   - b. `list.remove(...)`
   - c. `list.insert(..., ...)`

4. **What does the following code block output?**
   
```python
def function(a: int) -> None:
    a = 5

a = 3
function(a)
print(a)
```


5. **What does the following code block output?** 

```python
def function(a: list[int]) -> None:
    a.append(5)

a = [1, 2, 3, 4]
function(a)
print(a)
```

6. Let’s say that you had this scenario of objects like a Dog and Animal class. What type of relationship would that be from an Object-Oriented Design sense?

7. Why do we use getters/setters? Please give an example of a potential issue if you do not use them.

8. What is the difference between abstraction and implementation?

9. Why do we focus on the features before focusing on the implementation?

10. What’s wrong with the below Customer and LunchLine classes? How would you fix it? In other words, if we run the code below, there will be an error. What is the error?

```python
import time

class Customer:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class LunchLine:
    def __init__(self, customers: list[Customer], time_end: int) -> None:
        self.time_end = time_end
        self.line_size = len(customers)
        self.customers = customers

    def line_size(self) -> int:
        return self.line_size

    def get_customers(self) -> list[Customer]:
        return self.customers

    def is_lunch_over(self) -> bool:
        current_time = time.time()
        if current_time > self.time_end:
            return True
        return False

c1 = Customer("Annie", 29)
c2 = Customer("Bob", 26)
c3 = Customer("Charlie", 29)
c4 = Customer("Dana", 35)
my_list = [c1, c2, c3, c4]
lunchline = LunchLine(my_list, 24)
print(lunchline.line_size())
print(lunchline.is_lunch_over())
for customer in lunchline.get_customers():
    print(customer)
```