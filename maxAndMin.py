largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest == None :
        largest = num
    else:
        if largest < num :
            largest = num

    if smallest == None :
        smallest = num
    else :
        if smallest > num :
            smallest = num

print("Maximum is", largest)
print("Minimum is",smallest)
