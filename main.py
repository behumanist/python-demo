import pyautogui
print('Press Ctrl-C to quit.')

try: 
  while True:
  # Get and print the mouse coordinates.
    x, y = pyautogui.position()
    positionStr = '----------X: ' + str(x) + ' Y: ' + str(y) + "----------"
    print(positionStr)

except KeyboardInterrupt:
  print('\nDone.')
