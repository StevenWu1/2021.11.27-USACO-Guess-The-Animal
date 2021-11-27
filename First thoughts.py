import sys

sys.stdin = open("guess.in","r")
sys.stdout = open("guess.out","w")

def parse_input(lines):
    n = int(lines.pop(0))
    for line in lines:
        animals, num, traits = line.strip(). split()
        data[animals] = set(traits)
    return data

def slowmethod(data):
    animals = data.keys()
    most_common = 0
    for a in animals:
        for b in animals:
            if a != b:
                common = len(data[a].intersection(data[b]))
                most_common = max(common, most_common)
    return most_common + 1
 
demo = """
4
bird 2 flies eatsworms
cow 4 eatsgrass isawesome makesmilk goesmoo
sheep 1 eatsgrass
goat 2 makesmilk eatsgrass
""".strip().split("\n")

print(slowmethod(parse_input(sys.stdin.readlines())))
 
close(sys.stdout)
