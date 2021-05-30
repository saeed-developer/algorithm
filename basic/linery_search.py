list = [x for x in range(100)]
def search(lst, target):
    index = 0
    while index <= len(lst) - 1:
        if lst[index] == target:
            print(index)
            index = len(lst)
        else:
            index += 1
            
search(list, 15)
