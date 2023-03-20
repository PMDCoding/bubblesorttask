
def bubble_sort(any_list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,len(any_list)-1):
            if any_list[i] > any_list[i+1]:
                temp = any_list[i]
                any_list[i] = any_list[i+1]
                any_list[i+1] = temp
                sorted = False
    return any_list
