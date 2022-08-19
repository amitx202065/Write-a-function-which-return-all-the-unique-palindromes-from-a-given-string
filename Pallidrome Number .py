def expand(s, low, high, palindromes):
    while low >= 0 and high < len(s) and s[low] == s[high]:
 
        # push all palindromes into a set
        palindromes.add(s[low: high + 1])
        low = low - 1
        high = high + 1
def findPalindromicSubstrings(s):
    palindromes = set()
 
    for i in range(len(s)):
 
        # find all odd length palindrome with `s[i]` as a midpoint
        expand(s, i, i, palindromes)
        expand(s, i, i + 1, palindromes)
    print(palindromes, end='')
if __name__ == '__main__':
 
    s = 'google'
    findPalindromicSubstrings(s)