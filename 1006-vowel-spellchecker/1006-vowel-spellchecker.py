class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(word: str) -> str:
            return "".join('*' if ch in vowels else ch for ch in word)
        
        exact_words = set(wordlist)
        case_map = {}
        vowel_map = {}
        
        for word in wordlist:
            lower_word = word.lower()
            case_map.setdefault(lower_word, word)
            vowel_map.setdefault(devowel(lower_word), word)
        
        res = []
        for q in queries:
            if q in exact_words:
                res.append(q)
            elif q.lower() in case_map:
                res.append(case_map[q.lower()])
            elif devowel(q.lower()) in vowel_map:
                res.append(vowel_map[devowel(q.lower())])
            else:
                res.append("")
        return res