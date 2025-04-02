class Solution(object):
    def combinationSum3(self, k, n):
        def backtrack(start,k,n,path):
            if k==0 and n==0:
                result.append(path)
                return
            for i in range(start,10):
                if i>n:
                    break
                backtrack(i+1,k-1,n-i,path+[i])
        result=[]
        backtrack(1,k,n,[])
        return result