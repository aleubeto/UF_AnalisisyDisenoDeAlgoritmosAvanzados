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
            return(i-j)
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
        return ''
 
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
         
         
#Función de la parte 2 para buscar mcode espejeado
def output2(transmission, mcodeList):
    espejeado = [[],[]]
    for i in mcodeList:
        if KMPSearch(i[::-1],transmission) != '':
            espejeado[0].append(KMPSearch(i[::-1],transmission)+1)
            espejeado[1].append(KMPSearch(i[::-1],transmission)+len(i)+1)
    if len(espejeado[0])>0:
        first_found = espejeado[0].index(min(espejeado[0]))
        return f'{espejeado[0][first_found]} {espejeado[1][first_found]}'
    else:
        return 'No match'       

#Función de la parte 3 que genera los substrings de un archivo 
def substrings(txt):
    txt = txt[::-1]
    s = []
    for i in range(len(txt)):
        if s == []:
            s.append(txt[i])
        else:
            s.append(txt[i] + s[i-1])
    return(s)


#Función de parte 3 que busca el substring mayor de un archivo (transmission1) en otro (transmission2)
def compare(txt1, txt2):
    pat_list = substrings(txt1)
    beginning = 0
    ending = 0
    max = ''
    for i in range(len(pat_list)):
        for j in range(len(txt2)):
            if pat_list[i] == txt2[j:j+len(pat_list[i])]:
                if len(pat_list[i]) > len(max):
                    beginning = j + 1
                    ending = j+len(pat_list[i])
                    max = pat_list[i]

    print(f"Inicial:{beginning}       Final:{ending}     Substring:/{max}/")

transOne = open("transmission1.txt").read().upper()
transTwo = open("transmission2.txt").read().upper()
mcodeOne = open("mcode1.txt").read().upper()
mcodeTwo = open("mcode2.txt").read().upper()
mcodeThree = open("mcode3.txt").read().upper()


#transmission1.txt Parte 1
print("\nParte 1")
print(f"{True if KMPSearch(mcodeOne, transOne) != '' else False} {KMPSearch(mcodeOne, transOne)}")
print(f"{True if KMPSearch(mcodeTwo, transOne) != '' else False} {KMPSearch(mcodeTwo, transOne)}")
print(f"{True if KMPSearch(mcodeThree, transOne) != '' else False} {KMPSearch(mcodeThree, transOne)}")

#transmission2.txt Parte 1
print(f"{True if KMPSearch(mcodeOne, transTwo) != '' else False} {KMPSearch(mcodeOne, transTwo)}")
print(f"{True if KMPSearch(mcodeTwo, transTwo) != '' else False} {KMPSearch(mcodeTwo, transTwo)}")
print(f"{True if KMPSearch(mcodeThree, transTwo) != '' else False} {KMPSearch(mcodeThree, transTwo)}")

#Parte 2
print("\nParte 2")
mcodeList = [mcodeOne, mcodeTwo, mcodeThree]
print(output2(transOne,mcodeList))
print(output2(transTwo,mcodeList))

#Parte 3
print("\nParte 3")
compare(transOne, transTwo)