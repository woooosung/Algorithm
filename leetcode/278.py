class Solution:
    def firstBadVersion(self, n: int) -> int:
        temp = int(n/2)
        if n==1:
            temp = 1
        length = n
        while length>=1:
            abc = isBadVersion(temp)
            if abc:
                if not isBadVersion(temp-1):
                    break
            if abc:
                temp = temp - int(length/2)
            else:
                temp = temp + int(length/2)
            length = int(length/2)+1
        
        return temp