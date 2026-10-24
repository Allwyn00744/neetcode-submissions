class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        ana_dict={}
        for c in s :
            if c in ana_dict:
                ana_dict[c] +=1
            else:
                ana_dict[c]=1 
        for char1 in t :
            if char1 in ana_dict:
                ana_dict[char1] -=1
             
        for i,j in ana_dict.items():
            if j != 0:
                return False
        return True

            
        



        