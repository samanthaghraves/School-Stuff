import webbrowser
import time

breaks = 0

print("This program started on"+time.ctime())
while (breaks < 3):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=6yDEYu61piI")
    breaks = breaks + 1
