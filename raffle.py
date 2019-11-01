# Beyondcoin Raffle Script

import random
import time
import sys
from progress.bar import Bar

ADDRESSES = [
  'Address 1',
  'Address 2',
  'Address 3',
  'Address 4',
  'Address 5'
]

beyondcoin_amount = '1'
address_total = '5'

print("Welcome to the...")

time.sleep(1)

print("""\n\
#####################################################################################################################
*  ____  ________     ______  _   _ _____   _____ ____ _____ _   _    _____            ______ ______ _      ______  *
* |  _ \|  ____\ \   / / __ \| \ | |  __ \ / ____/ __ \_   _| \ | |  |  __ \     /\   |  ____|  ____| |    |  ____| *
* | |_) | |__   \ \_/ / |  | |  \| | |  | | |   | |  | || | |  \| |  | |__) |   /  \  | |__  | |__  | |    | |__    *
* |  _ <|  __|   \   /| |  | | . ` | |  | | |   | |  | || | | . ` |  |  _  /   / /\ \ |  __| |  __| | |    |  __|   *
* | |_) | |____   | | | |__| | |\  | |__| | |___| |__| || |_| |\  |  | | \ \  / ____ \| |    | |    | |____| |____  *
* |____/|______|  |_|  \____/|_| \_|_____/ \_____\____/_____|_| \_|  |_|  \_\/_/    \_\_|    |_|    |______|______| *
*                                                                                                                   *
#####################################################################################################################
""")

time.sleep(1.75)

print("There are " + beyondcoin_amount  + " Beyondcoins up for grabs and " + address_total  + " participants in this raffle.")

time.sleep(2)

print("\nThe Beyondcoins will be evenly distributed among 3 randomly selected people.")

print("\n")

time.sleep(1.5)

for remaining in range(150, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("The drawing will start in {:2d} seconds!".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

print("\n\nThe drawing has started...")

time.sleep(3)

print("\n")

bar = Bar('and the first Beyondcoin raffle winner is...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the second drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the second Beyondcoin raffle winner is...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!".format(random.choice(ADDRESSES)))

time.sleep(1)

print("\n")

for remaining in range(10, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining till the final drawing.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

bar = Bar('and the third and final Beyondcoin raffle winner is...', max=100)

for i in range(100):
    [x for x in range(999999)]
    bar.next()
bar.finish()

time.sleep(1)

print("\n\n\t{}!\n\n".format(random.choice(ADDRESSES)))

print("-" * 75 + "\n")

time.sleep(1)

print("Congratulations to everyone that won!")
print("\nThank you to eveyone that participated in the Beyondcoin raffle this round!")
print("\nPlease stay tuned as there may be another raffle soon!")
print("\n")
