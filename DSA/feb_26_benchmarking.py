#February 26th Benchmarking Questions
def modify_values(a, b, c):
    a += 1
    b.append(4)
    c = c + (5)

x = 10
y = [1, 2, 3]
z = (1, 2, 3)

modify_values(x, y, z)

print(x)  
print(y)  
print(z)
#The output will be 10, [1,2,3,4], and (1,2,3) for modify_values(x, y, z)

def register_user(name: str, membership_type="Basic", subscribe_to_newsletter=True):
    user_registration = (
        f"Registration Summary:\n"
        f"Name: {name}\n"
        f"Membership Type: {membership_type}\n"
        f"Subscribe To Newsletter: {'Yes' if subscribe_to_newsletter else 'No'}"
    )
    return user_registration
print(register_user("Andrew", "Premium", True))
print(register_user("Bobby", False))
print(register_user("Chuck"))

#Iterative approach
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def reverse_string(word: str):
    result = []
    for i in range(len(word) -1, -1, -1):
        result.append(word[i])
    return ''.join(result)
word = "apple"
print(reverse_string(word)) #Output: "elppa"

def reverse_alternate_chars(word: str):
    result = []
    for i in range(len(word)):
        if i % 2 == 1: #Must be odd index
            result.append(word[len(word) - i - 1]) #Appends the character from the end if odd
        else:
             result.append(word[i]) #Appends the even index and keeps character as is.
    return ''.join(result)
word = "ghost"
print(reverse_alternate_chars(word)) #Output: "gsoht"

#For this we can use the reverse_string function to help out.
def reverse_words(strings):
  reversed_words = []
  for string in strings:
    reversed_words.append(reverse_string(string))
  return reversed_words

strings = ["apple", "ghost", "doctor"]
print(reverse_words(strings)) #Output: ["elppa", "tsohg", "rotcod"]
