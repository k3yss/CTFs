# generate 50 number

output = []
def gen():
    for i in range(50):
        output.append(1)
    

gen()
print(output)
# output to a file
open("flagbs.txt", "w").write(str(output))