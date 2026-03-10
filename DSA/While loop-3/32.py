bin = int(input("Enter a binary number: "))
out = 0
power = 0
while bin > 0 :
    last =  bin%10
    out += last*(2**power)
    power += 1
    bin//= 10

print(out)