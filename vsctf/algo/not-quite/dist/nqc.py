from enum import Enum
import random
random.seed(1337)
ops = [
    lambda x: x+3,
    lambda x: x-3,
    lambda x: x*3,
    lambda x: x^3,
]

# an enum in python with 4 value
class Ops(Enum):
     ADD = 4
     SUB = -2
     MUL = 3
     POW = 2


# flag = list(open("flag.txt", "rb").read())
flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
out = []
cipher = []
for v in flag:
    val = random.choice(ops)(v)
    if val == Ops.SUB.value:
        cipher.append("SUB")
    if val == Ops.ADD.value:
        cipher.append("ADD")
    if val == Ops.MUL.value:
        cipher.append("MUL")
    if val == Ops.POW.value:
        cipher.append("POW")
    out.append(val)

# print(f'{len(out)=}')
# print(f'{out=}')
# print(f'{cipher=}')

# open the file out.txt and take the contents inside it which is a list an an input
output = [354, 112, 297, 119, 306, 369, 111, 108, 333, 110, 112, 92, 111, 315, 104, 102, 285, 102, 303, 100, 112, 94, 111, 285, 97, 351, 113, 98, 108, 118, 109, 119, 98, 94, 51, 56, 159, 50, 53, 153, 100, 144, 98, 51, 53, 303, 99, 52, 49, 128]

decry = []
for i in range(len(output)):
    val = output[i]
    if cipher[i] == "ADD":
        decry.append(int(val - 3))
    if cipher[i] == "SUB":
        decry.append(int(val + 3))
    if cipher[i] == "MUL":
        decry.append(int(val / 3))
    if cipher[i] == "POW":
        decry.append(int(val ^ 3))


def write_to_file(flag_list):
    with open("flag.txt", 'wb') as f:
        f.write(bytes(flag_list))

write_to_file(decry) 