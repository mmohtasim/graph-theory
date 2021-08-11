n = map(int,input("Enter n:"))
unsorted_degrees = list(map(int, input("Enter degrees(space separated):").split()))
# unsorted_degrees = [5,5,5,5,5,5]

degrees = sorted(unsorted_degrees, reverse= True)
degrees_copy = degrees.copy()
is_graphic = None
if degrees[0] > len(degrees) - 1 or any(n < 0 for n in degrees):
    is_graphic = False
else:
    while sum(degrees) > 0:
        for i in range(degrees[0]):
            degrees[i+1] = degrees[i+1] - 1
        degrees.pop(0)
        degrees.sort(reverse=True)
        if(any(n < 0 for n in degrees)):
            is_graphic = False
            break
        if sum(degrees) == 0:
            is_graphic = True
print(is_graphic)
edges = list()
slide = 0
if is_graphic:
    while sum(degrees_copy) > 0:
        for i in range(degrees_copy[slide]):
            edges.append((slide+1,slide+i+2))
            degrees_copy[slide+i+1] = degrees_copy[slide+i+1] - 1 
        degrees_copy[slide] = 0
        slide = slide + 1
        if(any(n < 0 for n in degrees_copy)):
            break

for a,b in edges:
    print(a,b)