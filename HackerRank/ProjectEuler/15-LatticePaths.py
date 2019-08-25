# 15. Lattice Paths
# Language: Python 3
# Testcases: 7/11

def nCrModpDP(n, r, p): 
    # The array C is going to store 
    # last row of pascal triangle 
    # at the end. And last entry  
    # of last row is nCr 
    C = [0] * (n + 1); 
  
    # Top row of Pascal Triangle 
    C[0] = 1;  
  
    # One by constructs remaining  
    # rows of Pascal Triangle from  
    # top to bottom 
    for i in range(1, (n + 1)): 
          
        # Fill entries of current  
        # row using previous row 
        # values 
        j = min(i, r);  
        while(j > 0): 
            C[j] = (C[j] + C[j - 1]) % p; 
            j -= 1; 
    return C[r]; 


T = int(input())
while(T > 0):
    M, N = [int(i) for i in input().split(' ')]
    num = [j for j in range(M+N, M+N - min([M,N]), -1)]
    den = [k for k in range(min([M,N]),0,-1)]
    
    # DP Function for calculating nCr mod, for huge number
    print(nCrModpDP(M+N, N, 1000000007))
    T-=1