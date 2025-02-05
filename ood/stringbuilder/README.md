Strings in Python are immutable. Let's look at why this inefficient for concatenation.


```
s = "Hello World."

s += " It is a good day."
```

In this example, Python creates a new string "Hello World. It is a good day" and sets that to the variable s. To create a new string, it requires O(len(old_string) + len(additional_string)). After many concatentations, this is inefficient.

Instead, we can create our own string_builder class (inspired by Java's StringBuilder) to reduce this operation to O(len(additional_string)). In this class, we can create a list of characters, initially set to a capacity (if specified). Now, to append to the string_builder, we just need to add to the end of the last character's index.

Here's a small example.


```
1. string = string_builder("i", 10)
2. string.append(" like")
3. string.append(" pie)

1. ['i',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
2. ['i','','l','i','k','e','','','',''] 
3. ['i','','l','i','k','e','','p','i','e'] 
```

Complete this challenge by filling out the missing methods in string_builder.py.



Note: You can raise an exception using the following syntax.



raise Exception("Error message")