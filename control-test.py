from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()

print("The curr pos is {0}".format(mouse.position))

mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

sleep(3)

# Move pointer relative to current position
mouse.move(500, -150)
print('Now we have moved it to {0}'.format(
    mouse.position))