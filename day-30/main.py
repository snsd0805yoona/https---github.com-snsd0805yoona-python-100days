

try:
    file = open("a.txt")
    dict = {"key": "value"}
    print(dict["key"])
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("This is something new.")

except KeyError as errorMessage:
    print(f"The {errorMessage} is not exist in dictionary")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file closed.")
