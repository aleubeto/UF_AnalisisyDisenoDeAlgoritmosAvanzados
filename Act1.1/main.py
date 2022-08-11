#Mergesort recursivo que ordene de mayor a menor
def DACmergesort(n, array):
    if (n>1):
        mid = n//2
        left_array = array[0:mid]
        right_array = array[mid+1:n-1]
        
    DACmergesort(len(left_array),left_array)
    DACmergesort(len(left_array),left_array)
        

        
    
