import random
def tree_display(k):
    N = 2*k + 1

    stem = '|'
    stem_width = k // 4
    stem_height = k // 6
    for n in range(1, N, 2):
        l = (N - n) // 2
        r = l
        c = '^'
        ornament = 'Q'

        if n==1:
            c = '*'
        leafs = c*n

        if n>3:
            max_ornaments = max(1, n // 12)

            positions = random.sample(range(1, n - 1), max_ornaments)

            for i in positions:

                deviate = random.randint(-2,2)
                i2 = n - i + deviate
                if (leafs[i-1]==c  and  leafs[i+1] ==c):
                    leafs = leafs[:i] + ornament + leafs[i+1:]
                if i2>=1 and i2<=n-2:
                    if (leafs[i2-1]==c  and  leafs[i2+1] ==c):
                        leafs = leafs[:i2] + ornament + leafs[i2+1:]
        print(' ' * l + leafs + ' ' * r)
    if k >5:
        y = (N-stem_width)//2
        z= " "*y + stem*stem_width + " "*y
        for i in range(stem_height):
            print(z)

while True:
    n = int(input("Tree Height: "))
    tree_display(n)

