class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev_key = ""
        
        for word in words:
            key = ''.join(sorted(word))
            
            if key != prev_key:
                result.append(word)
                prev_key = key
        
        return result