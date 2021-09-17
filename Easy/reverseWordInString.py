# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution(object):
    def reverse(self,word):
        chars = list(word)  
        l,r = 0,len(word)-1
        while l<=r:
            chars[l],chars[r] = chars[r],chars[l]  # swapping
            l += 1
            r -= 1
        return ''.join(chars)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        res=[]
        for word in words:
            reversed_word = self.reverse(word)
            res.append(reversed_word)
        response = " ".join(res)
        return response