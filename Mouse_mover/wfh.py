import pyautogui as p

distance = 200

while True:
    p.moveRel(distance,0,duration=0.5) # move right
    distance -=5
    p.moveRel(0,distance,duration=0.5) # move down
    p.moveRel(-distance,0,duration=0.5) # move left
    distance -=5
    p.moveRel(0,-distance,duration=0.5) # move up
    distance +=10