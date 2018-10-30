# Imperative Stacks

def new_stack():
    return [0, [0] * 10, 10]

def push(arr, e):
    if (arr[0] == arr[2]):
        # I know I have to expand the array
        oldData = arr[1]
        newData = [0] * arr[2] * 2
        i = 0
        size = arr[2]
        while (i < size):
            newData[i] = oldData[i]
            i += 1
        newData[size] = e
        arr[1] = newData
        arr[2] = size * 2
        arr[0] = arr[0] + 1
    else:
        
            
    
