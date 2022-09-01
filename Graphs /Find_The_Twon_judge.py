# def findJudge( n, trust):
#         if len(trust) < n-1:
#             return -1
#         trust_scores = [0]*(n+1)
        
#         for outgoing , incoming in trust:
#             trust_scores[outgoing]-=1
#             trust_scores[incoming]+=1
#         for i , score in enumerate(trust_scores[1:],1):
#             if score == n-1:
#                 return i
#         return -1
def findJudge(n, trust):
    """
:type n: int
:type trust: List[List[int]]
:rtype: int
"""
    '''
        Always remember a town Judge is someone who will not trust anyone,
        but everyone will trust him.

        so in the trusued list it will town judge will always have 0 count 
        and in the trusted arr he will be trusted by everyone except him (n-1).
    '''
    trust_a = [i for i, j in trust] #trusrted
    trust_b = [j for i, j in trust] #Trusted by list
    for i in range(1, n + 1):
        if trust_a.count(i) == 0 and trust_b.count(i) == n - 1:
            return i
    return -1

# Test Case 1: - 
  
n = 2 
trust = [[1,2]]

# Test Case 2: -

# n = 3
# trust = [[1,3],[2,3],[3,1]]

print(findJudge( n ,trust))