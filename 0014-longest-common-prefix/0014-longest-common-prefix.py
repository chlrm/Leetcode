class Solution(object):
    def longestCommonPrefix(self, strs):
        pref=strs[0]
        for i in strs[1:]:
            while not i.startswith(pref):
                pref=pref[:-1]
                
        return pref
        