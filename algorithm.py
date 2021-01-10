width = 0
height = 0
heady = 0
headx = 0
length = 0

def set(data):
    global width
    width = data["board"]["width"]
    global height
    height = data["board"]["height"]

def save(data):
    global headx
    headx = data["you"]["head"]["x"]
    global heady
    heady = data["you"]["head"]["y"]

def food(data, move):
    # This function seeks the food
    global width, height, headx, heady
    result = []
    min = width + height + 1
    index = 0
    for i in range(0, len(data["board"]["food"])):
        toFood = abs(data["board"]["food"][i]["x"] - headx) + abs(data["board"]["food"][i]["y"] - heady)
        if toFood < min:
            min = toFood
            index = i
    difx = data["board"]["food"][index]["x"] - headx
    dify = data["board"]["food"][index]["y"] - heady
    if dify < 0 and "down" in move:
        result.append("down")
    if dify > 0 and "up" in move:
        result.append("up")
    if difx < 0 and "left" in move:
        result.append("left")
    if difx > 0 and "right" in move:
        result.append("right")
    if len(result) == 0:
        print(move)
        return move
    print(result)
    return result

#this function avoids the border
def border(data,move):
  global headx, heady
  if heady == height and "up" in move:
      move.remove("up")
  if heady == 0 and "down" in move:
      move.remove("down")
  if headx == 0 and "left" in move:
      move.remove("left")
  if headx == width and "right" in move:
      move.remove("right")
  print(move)
  return move

# gotta think about not eating up myself
def myself(data, move):
    global length
    length = data["you"]["length"]
    global headx, heady
    for pos in data["you"]["body"]:
        if pos["y"] == heady:
            if pos["x"] == headx + 1 and "right" in move:
                move.remove("right")
            if pos["x"] == headx - 1 and "left" in move:
                move.remove("left")
        if pos["x"] == headx:
            if pos["y"] == heady + 1 and "up" in move:
                move.remove("up")
            if pos["y"] == heady - 1 and "down" in move:
                move.remove("down")
    print(move)
    return move

