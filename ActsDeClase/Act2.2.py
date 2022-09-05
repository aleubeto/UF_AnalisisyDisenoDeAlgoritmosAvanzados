# Juan Carlos Ferrer Echeverría A01734794
# Alejandro Alfonso Ubeto Yañez A01734977
# Maximiliano Romero Budib      A01732008

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if (ord(arr[j][0]) > ord(arr[j + 1][0])):
                # sorting by using simultaneous assignment in python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

def substring(word):
    word = word[::-1]
    s = []
    for i in range(len(word)):
        if s == []:
            s.append(word[i])
        else:
            s.append(word[i] + s[i-1])
    # DACmergesort(s)
    print(s)
    bubble_sort(s)
    #quicksort(0,len(s)-1,s)
    
word = "analisis"
substring(word)
