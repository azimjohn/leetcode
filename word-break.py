# https://leetcode.com/problems/word-break/

memory = {}

def wordBreak(word: str, words: list) -> bool:
    if word in memory:
        return memory[word]

    if not word:
        memory[word] = True
        return True

    start_words = [s for s in words if word.startswith(s)]
    if not start_words:
        memory[word] = False
        return False
    
    for s in start_words:
        remaining = word[len(s):]
        if wordBreak(remaining, words):
            memory[word] = True
            return True
    
    memory[word] = False
    return False


if __name__ == '__main__':
    cases = [
        [("cars", ["car", "ca", "rs"]), True],
        [("leetcode", ["leet", "code"]), True],
        [("applepenapple", ["apple", "pen"]), True],
        [("catsandog", ["cats", "dog", "sand", "and", "cat"]), False],
        [("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]), False]
    ]

    for case in cases:
        print("PASS" if wordBreak(*case[0])==case[1] else "FAIL")
