# https://leetcode.com/problems/word-break-ii

def wordBreak(word: str, words: list) -> list:
    if not word:
        return ['']

    start_words = [s for s in words if word.startswith(s)]
    if not start_words:
        return []

    sentences = []
    for s in start_words:
        remaining = word[len(s):]
        remaining_sentences = wordBreak(remaining, words)
        sentences.extend([(s+' '+rs).strip() for rs in remaining_sentences])

    return sentences


if __name__ == '__main__':
    cases = [
        [("cars", ["car", "ca", "rs"]), ["ca rs"]],
        [("leetcode", ["leet", "code"]), ["leet code"]],
        [("applepenapple", ["apple", "pen"]), ["apple pen apple"]],
        [("catsanddog", ["cats", "dog", "sand", "and", "cat"]), ["cats and dog", "cat sand dog"]],
        [("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]]
    ]

    for case in cases:
        result = set(wordBreak(*case[0]))
        expected = set(case[1])
        print("PASS" if result==expected else "FAIL", result)
