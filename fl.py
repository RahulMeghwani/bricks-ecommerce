# from flask import Flask

# app = Flask(__name__)

# app.run(port=8080)

# __import__("flask").Flask(__name__).run(port=8080)

# s = input()
# if s == s[::-1]:
#     print("palindrome!")
# else:
#     print("not a palindrome!")

# print(["palindrome", "not a palindrome"][0 if (s:=input())==s[::-1] else 1])

# def HelloWorld(a):
#     print("Hello World!")

import json

with open("flow.json", "r") as f:
    data = json.load(f)

for brick in data["Bricks"]:
    print(brick)
    print(f"Name: {brick['name']}")
    print()