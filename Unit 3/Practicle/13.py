def towerOfHanoi(N , source, destination, auxiliary):
    if N==1:
        print("Move disk 1 from source",source,"todestination",destination)
    return towerOfHanoi(N-1, source, auxiliary, destination)
        print("Move disk",N,"from source",source,"todestination",destination)
        towerOfHanoi(N-1, auxiliary, destination, source)
# Driver code
N = 3
towerOfHanoi(N,'A','B','C')
