# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    match = False
    M = len(pat)
    N = len(txt)
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            print ("Found pattern at index", str(i-j))
            match = True
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    if not match:
        print("No match")
 
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
 


transOne = open("transmission1.txt", "r")
transTwo = open("transmission2.txt", "r")
mcodeOne = open("mcode1.txt", "r")
mcodeTwo = open("mcode2.txt", "r")
mcodeThree = open("mcode3.txt")

transOne = transOne.read()
transTwo = transTwo.read()
mcodeOne = mcodeOne.read()
mcodeTwo = mcodeTwo.read()
mcodeThree = mcodeThree.read()

transOne = transOne.upper()
transTwo = transTwo.upper()
mcodeOne = mcodeOne.upper()
mcodeTwo = mcodeTwo.upper()
mcodeThree = mcodeThree.upper()

print(transOne)
print(mcodeOne)
#mcodeOne es el patron a encontrar, transOne es el string donde esta el patron
KMPSearch(mcodeOne, transOne)

print(transOne)
print(mcodeTwo)

KMPSearch(mcodeTwo, transOne)

print(transOne)
print(mcodeThree)

KMPSearch(mcodeThree, transOne)

#Archivo 2
print(transTwo)
print(mcodeOne)

KMPSearch(mcodeOne, transTwo)

print(transTwo)
print(mcodeTwo)

KMPSearch(mcodeTwo, transTwo)

print(transTwo)
print(mcodeThree)

KMPSearch(mcodeThree, transTwo)
 
# This code is contributed by Bhavya Jain