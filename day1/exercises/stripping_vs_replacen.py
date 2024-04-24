print("original")
example = "  \nHello,\nworld!\n  "
print(example)
print("Stripping")
print(example.strip())  # Removes leading and trailing whitespaces including newlines: "Hello,\nworld!"
print("Replaces new line and then strip ")
print(example.replace("\n", "").strip())  # First removes all newlines, then strips: "Hello,world!"

print("Replacing without stripping") 
print(example.replace("\n",""))
