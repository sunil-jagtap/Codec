from enum import Enum
 
class Card_direction(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"
class Hum_direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"
    BACKWARD = "B"
    

x=1
y=1
d=Card_direction.NORTH.value
grid=[{"position":[x,y], "dir":d}]
values_hum = [member.value for member in Hum_direction]
m,n=list(map(int,input("Enter the plateau size for e.g 5x5: ").split("x")))

command=input("Enter the Command for robot: ")
for l in command:
    if x>=1 and y>=1 and l in values_hum:
        if d==Card_direction.NORTH.value:
            if l==Hum_direction.LEFT.value:
                x-=1
                d=Card_direction.WEST.value
            elif l==Hum_direction.RIGHT.value:
                x+=1
                d=Card_direction.EAST.value
            elif l==Hum_direction.FORWARD.value:
                y+=1
        elif d==Card_direction.EAST.value:
            if l==Hum_direction.LEFT.value:
                y+=1
                d=Card_direction.NORTH.value
            elif l==Hum_direction.RIGHT.value:
                y-=1
                d=Card_direction.SOUTH.value
            elif l==Hum_direction.FORWARD.value:
                x+=1
        elif d==Card_direction.SOUTH.value:
            if l==Hum_direction.LEFT.value:
                x+=1
                d=Card_direction.EAST.value
            elif l==Hum_direction.RIGHT.value:
                x-=1
                d=Card_direction.WEST.value
            elif l==Hum_direction.FORWARD.value:
                y-=1
        elif d==Card_direction.WEST.value:
            if l==Hum_direction.LEFT.value:
                y-=1
                d=Card_direction.SOUTH.value
            elif l==Hum_direction.RIGHT.value:
                y+=1
                d=Card_direction.NORTH.value
            elif l==Hum_direction.FORWARD.value:
                x-=1
        if x==m: # if next move is on boundry then just wait
            x-=1
        if y==n:
            y-=1
        if x>=1 and y>=1:
            grid.append({"position":[x,y], "dir":d})
result=grid[-1] # last element
print("Result: "+str(result['position']).strip("[]")+", "+Card_direction(result['dir']).name)
