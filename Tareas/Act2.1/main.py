#long hash(string s) {
#    const int p = 3;
#    const int m = 1000000009;
#    long hash = 0;
#    long pow = 1;
#    for (for every character c in s) {
#        hash = (hash + (c - 'a' + 1) * pow) % M;
#        pow = (pow * p) % M;
#    }
#    return hash;
#}
#https://iq.opengenus.org/string-hashing/

def hash(s) :
    p = 3
    m = 1000000009
    haash = 0
    pod = 1
    for c in s:
        haash = (haash + (ord(c) - ord("a") + 1) * pod) % m
        pod = (pod * p) % m
    return haash

print(hash("opengenus"))