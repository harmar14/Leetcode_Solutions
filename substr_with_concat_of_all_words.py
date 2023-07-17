class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if s is None or len(s) == 0 or words is None or len(words) == 0:
            return []

        res = []

        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        word_length = len(words[0])
        full_length = word_length * len(words)

        for i in range(len(s) - full_length + 1):
            current = s[i:i + full_length]
            met_dict = {}
            idx = 0
            j = 0
            while idx < len(words):
                part = current[j:(word_length+j)]
                if part in met_dict:
                    met_dict[part] += 1
                else:
                    met_dict[part] = 1
                j += word_length
                idx += 1
            if words_dict == met_dict:
                res.append(i)

        return res
