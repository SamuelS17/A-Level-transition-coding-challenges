import time
for Counter in range(int(input("How many green bottles:")),0,-1):
    print("{} green bottles hanging on the wall, {} green bottles hanging on the wall, And if one green bottle should accidentally fall, There'll be {} green bottles hanging on the wall".format(Counter,Counter, Counter - 1))
    time.sleep(10)