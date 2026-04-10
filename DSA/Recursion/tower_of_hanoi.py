def tower_of_hanoi(number_of_disk,source,auxiliary,destination):
    if number_of_disk == 1:
        print(f'Move disk from {source} to {destination}')
        return

    tower_of_hanoi(number_of_disk - 1,source, destination,auxiliary)
    print(f'Move disk from {source} to {destination}')
    tower_of_hanoi(number_of_disk - 1,auxiliary , source , destination)

n = int(input("Enter no of disk: "))
tower_of_hanoi(n,"A", "B", "C")