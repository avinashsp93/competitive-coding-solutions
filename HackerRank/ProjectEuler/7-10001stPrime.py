# 7. 10001st Prime
# Language: Python 3
# Testcases: 5/5

T = int(input())
def SieveOfEratosthenes(n): 
       
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
       # a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    return prime
  
# Driver function 
prime = SieveOfEratosthenes(104730)
prime[0] = False
prime[1] = False
prime_dict = {}

count = 0
for i in range(0, len(prime)):
    if(prime[i] == True):
        prime_dict[count] = i
        count+=1
while(T>0):
    N = int(input())
    print(prime_dict[N-1])
    T-=1
