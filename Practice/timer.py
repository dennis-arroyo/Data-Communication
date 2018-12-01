import time

start = time.time()

while True:
    answer = input()
    if answer == "stop":
        break

end = time.time()

finalTime = round(end - start, 2)

print("Seconds:", finalTime)
