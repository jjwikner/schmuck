import time
import os

tick = 0

timestart = time.time()

idx = 0
snakes = ["…","-","¨","-"]
while True: # Or look for a file os.path.isfile("")
    # Could run a bit more often with the timer
    with open('tick.txt', "w") as fid:
        fid.write(f"{tick}\n")
    print(snakes[idx%4],end="", flush=True)
    time.sleep(0.5)
    tick += 0.5
    idx += 1
