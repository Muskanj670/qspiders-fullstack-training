def tower_of_hanoi(number_of_disk,source,auxiliary,destination, count = 1):
    if n == 1:
        print(f'{count}. Move disk {source} to {destination}')
        return

    tower_of_hanoi(number_of_disk - 1,source, destination,auxiliary, count+1)
    print(f'{count}. Move disk {source} to {destination}')
    tower_of_hanoi(number_of_disk - 1,auxiliary , source , destination, count+1)


n = int(input("Enter no of disk: "))
tower_of_hanoi(n,"A", "B","C")