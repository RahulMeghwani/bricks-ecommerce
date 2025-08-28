from flask import Flask, request, jsonify 

# # # app = Flask(__name__)

# # # app.run(port=8080)

# # # __import__("flask").Flask(__name__).run(port=8080)

# # # s = input()
# # # if s == s[::-1]:
# # #     print("palindrome!")
# # # else:
# # #     print("not a palindrome!")

# # # print(["palindrome", "not a palindrome"][0 if (s:=input())==s[::-1] else 1])

# # # def HelloWorld(a):
# # #     print("Hello World!")

# # import json

# with open("flow.json", "r") as f:
#     data = json.load(f)

# # for brick in data["Bricks"]:
# #     print(brick)
# #     print(f"Name: {brick['name']}")
# #     print()

import json
with open("flow.json","r") as file:
    data = json.load(file)
    # print(data)
    # for brick in data["Bricks"]:
    #     # print(brick)
    #     print()
    #     print(f"Name:{brick['name']}")
    #     print(f"Size:{brick['sizes']}")
    #     print(f"Colour:{brick['colors']}")
    #     print()

app = Flask(__name__)

## function number = 1  
# def all_bricks(data):
#     return data['Bricks']

# result = all_bricks(data)
# print(result)

@app.route('/')
def print_fun():
    return("Enter /bricks")


@app.route('/bricks', methods = ['GET'])
def all_bricks():
    return (data['Bricks'])


## function number = 2
# def brick_name(data,name):
#     for brick in data["Bricks"]:
#         if name == brick['name']:
#             return brick
#     return "none"

# result1 = brick_name(data, "Flyash Bricks")
# print(result1)

@app.route('/bricks/<name>',methods = ['GET'])
def api_brick_name(name):
    with open("flow.json","r") as file:
        data = json.load(file)

    search_name = name.strip().lower()
    for brick in data['Bricks']:
        if brick['name'].strip().lower() == search_name:
            return jsonify(brick)
    return jsonify("None")


## function number = 3

# def brick_color(data, color):
#     for brick in data['Bricks']:
#         if color in brick['colors']:
#             return brick
#     return "none"

# result2 = brick_color(data, "red")
# print(result2)

@app.route('/bricks_color/<color>',methods=['GET'])
def api_color_name(color):
    with open("flow.json","r") as file:
        data = json.load(file)

    search_color = color.strip().lower()
    color_lst = []
    for brick in data['Bricks']:
        if search_color in brick['colors']:
            color_lst.append(brick)
    if len(color_lst) == 0:
        return jsonify("None")
    return jsonify(color_lst)

# function 4

# def add_bricks(data,new_brick):

#     # file = open("flow.json", "r")
#     # file.close()
#     with open("flow.json", "r") as file:
#         data = json.load(file)
        
#     # Step 2: Add new brick
#     data["Bricks"].append(new_brick)

#     # Step 3: Save updated data back
#     with open("flow.json", "w") as file:
#         json.dump(data, file, indent=4)
#     return data

# n_brick = {
#     "name":"fly - ash brick 2",
#     "colors":["blue","red"],
#     "sizes":["5*5","6*6"]
# }
# result = add_bricks(data,n_brick)
# print(result)

@app.route('/add_brick', methods=['POST'])
def add_brick():
    with open("flow.json","r") as file:
        data = json.load(file)
    
    new_brick = request.json
    print(request)
    if "color" not in new_brick.keys():
        new_brick["colors"] = []
    if "size" not in new_brick.keys():
        new_brick["sizes"] = []
        
    data["Bricks"].append(new_brick)

    with open("flow.json", "w") as file:
        json.dump(data, file, indent=4)
    return jsonify(data)

# ##function 5

# def update_bricks(data, brick_name, color = None, size = None):
#     if not color and not size:
#         return "Nothing is added"
#     with open("flow.json", "r") as file:
#         data = json.load(file)

#     for brick in data["Bricks"]:
#         if brick["name"] == brick_name:
#             if color:
#                 brick["colors"].append(color)
#             if size:
#                 brick["sizes"].append(size)
#             with open("flow.json",'w') as file:
#                 json.dump(data, file, indent = 4) 
#             return brick

#     return "Brick not found"

# result2 = update_bricks(data, "fly - ash brick 2")
# print(result2)


@app.route('/update_brick',methods=['POST'])
def update_attribute():
    with open("flow.json","r") as file:
        data = json.load(file)
    brick_name = request.json.get("brick_name")
    color = request.json.get("colors")
    size = request.json.get("sizes")

    if not color and not size:
        return jsonify({"message":"Nothing is added"})
    
    for brick in data["Bricks"]:
        if brick["name"] == brick_name:
            if color:
                brick["colors"].append(color)
            if size:
                brick["sizes"].append(size)

            with open("flow.json","w") as file:
                json.dump(data, file, indent = 4)

            return jsonify({"message": "Brick updated", "brick": brick})
        
    return jsonify({"message": "Brick not found"})




if __name__ == '__main__':
     app.run(debug=True, port=8000)