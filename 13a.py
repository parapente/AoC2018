#!/usr/bin/python3


class Cart:

    def __init__(self, pos, heading):
        self.pos = pos
        # 0 - left, 1 - up, 2 - right, 3 - down
        self.heading = heading
        # 0 - left, 1 - straight, 2 - right
        self.last_turn = 2


def cartsort(cart):
    return cart.pos[0] * 1000 + cart.pos[1]


def move():
    global lines
    for i, cart in enumerate(carts):
        if cart.heading == 0:
            cart.pos[1] -= 1
        if cart.heading == 1:
            cart.pos[0] -= 1
        if cart.heading == 2:
            cart.pos[1] += 1
        if cart.heading == 3:
            cart.pos[0] += 1

        # Check for crash
        for j, val in enumerate(carts):
            if i != j and val.pos == cart.pos:
                print('Crash at ', cart.pos)
                return False

        # Check map for turns
        if lines[cart.pos[0]][cart.pos[1]] == '/':
            if cart.heading == 0:
                cart.heading = 3
            else:
                if cart.heading == 1:
                    cart.heading = 2
                else:
                    if cart.heading == 2:
                        cart.heading = 1
                    else:
                        if cart.heading == 3:
                            cart.heading = 0
        if lines[cart.pos[0]][cart.pos[1]] == '\\':
            if cart.heading == 0:
                cart.heading = 1
            else:
                if cart.heading == 1:
                    cart.heading = 0
                else:
                    if cart.heading == 2:
                        cart.heading = 3
                    else:
                        if cart.heading == 3:
                            cart.heading = 2
        if lines[cart.pos[0]][cart.pos[1]] == '+':
            cart.last_turn = (cart.last_turn + 1) % 3
            if cart.last_turn == 0:
                cart.heading = (cart.heading - 1) % 4
            else:
                if cart.last_turn == 2:
                    cart.heading = (cart.heading + 1) % 4
    return True


with open('13.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
for i, val in enumerate(lines):
    lines[i] = list(lines[i])

# Find carts
carts = []
y = 0
while y < len(lines):
    x = 0
    while x < len(lines[y]):
        if lines[y][x] == '<':
            carts.append(Cart([y, x], 0))
        if lines[y][x] == '>':
            carts.append(Cart([y, x], 2))
        if lines[y][x] == '^':
            carts.append(Cart([y, x], 1))
        if lines[y][x] == 'v':
            carts.append(Cart([y, x], 3))
        x += 1
    y += 1

for cart in carts:
    print(cart.pos, cart.heading, end='')
print()

z = 1
while move():
    carts.sort(key=cartsort)
    print('Move ', z, ': ', end='')
    for cart in carts:
        print(cart.pos, cart.heading, ', ', end='')
    print()
    z += 1
