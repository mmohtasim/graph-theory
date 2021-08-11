# unsorted_degrees = list(map(int, input("Enter degrees(space separated):").split()))
unsorted_degrees = [5,4,3,3,2,1]

degrees = sorted(unsorted_degrees, reverse= True)
if degrees[0] > len(degrees) - 1 or any(n < 0 for n in degrees):
    print("NON Graphic")
else:
    while sum(degrees) > 0:
        for i in range(degrees[0]):
            degrees[i+1] = degrees[i+1] - 1
        degrees.pop(0)
        degrees.sort(reverse=True)
        print(degrees)
        if(any(n < 0 for n in degrees)):
            print("NON Graphic")
            break
        if sum(degrees) == 0:
            print("Graphic")