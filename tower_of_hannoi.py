def TowerOfHanoi(n, source, destination, auxiliary, push, pop):
    if n == 1:
        pop.append(source)
        push.append(destination)
        return push, pop
    push, pop = TowerOfHanoi(n - 1, source, auxiliary, destination, push, pop)
    
    pop.append(source)
    push.append(destination)
    push, pop = TowerOfHanoi(n - 1, auxiliary, destination, source, push, pop)
    return push, pop


def main():
    n = int(input())
    push = []
    pop = []
    push, pop = TowerOfHanoi(n, 1, 3, 2, push, pop)
    print(len(push))
    for i in range(len(push)):
        print(pop[i], push[i])

main()
 