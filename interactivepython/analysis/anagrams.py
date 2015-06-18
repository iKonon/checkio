'''
One string is an anagram of another if the second is simply a rearrangement of the first. 
For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. 
For the sake of simplicity, we will assume that the two strings in question are of equal length 
and that they are made up of symbols from the set of 26 lowercase alphabetic characters. 
Our goal is to write a boolean function that will take two strings and return whether they are anagrams.
'''

def anagram_solution_checkoff(s1,s2):
    '''
    Our first solution to the anagram problem will check to see that each character in the first string actually occurs in the second. 
    If it is possible to "checkoff" each character, then the two strings must be anagrams. 
    Checking off a character will be accomplished by replacing it with the special Python value None. 
    
    To analyze this algorithm, we need to note that each of the n characters in s1 
    will cause an iteration through up to n characters in the list from s2. 
    Each of the n positions in the list will be visited once to match a character from s1. 
    The number of visits then becomes the sum of the integers from 1 to n, this can be written as
    sum_{i=1}^n i = n(n+1)/2 = 1/2 n^2 + 1/2 n
    As n gets large, the n^2 term will dominate the n term and the 1/2 can be ignored. Therefore, this solution is O(n^2).
    '''
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def anagram_solution_sort_strings(s1,s2):
    '''
    Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different, 
    they are anagrams only if they consist of exactly the same characters. 
    So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string 
    if the original two strings are anagrams. 
    We can use the built-in sort method on lists by simply converting each string to a list at the start.
    
    At first glance you may be tempted to think that this algorithm is O(n), 
    since there is one simple iteration to compare the n characters after the sorting process. 
    However, the two calls to the Python sort method are not without their own cost. 
    Sorting is typically either O(n^2) or O(n log n), so the sorting operations dominate the iteration. 
    In the end, this algorithm will have the same order of magnitude as that of the sorting process.
    '''
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

def anagram_solution_brute_force(s1,s2):
    '''
    A brute force technique for solving a problem typically tries to exhaust all possibilities. 
    For the anagram detection problem, we can simply generate a list of all possible strings using the characters from s1 
    and then see if s2 occurs. 
    However, there is a difficulty with this approach. When generating all possible strings from s1, 
    there are n possible first characters, n-1 possible characters for the second position, n-2 for the third, and so on.   
    The total number of candidate strings is n*(n-1)*(n-2)*...*3*2*1, which is n! 
    Although some of the strings may be duplicates, the program cannot know this ahead of time 
    and so it will still generate n! different strings.

    It turns out that n! grows even faster than 2^n as n gets large. 
    In fact, if s1 were 20 characters long, there would be 20!=2,432,902,008,176,640,000 possible candidate strings. 
    If we processed one possibility every second, it would still take us 77,146,816,596 years to go through the entire list. 
    This is probably not going to be a good solution.
    '''
    pass

def anagram_solution_linear(s1,s2):
    '''
    Our final solution to the anagram problem takes advantage of the fact 
    that any two anagrams will have the same number of a's, the same number of b's, the same number of c's, and so on. 
    In order to decide whether two strings are anagrams, we will first count the number of times each character occurs. 
    Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character. 
    Each time we see a particular character, we will increment the counter at that position. 
    In the end, if the two lists of counters are identical, the strings must be anagrams.
    
    Again, the solution has a number of iterations. However, unlike the first solution, none of them are nested. 
    The first two iterations used to count the characters are both based on n. 
    The third iteration, comparing the two lists of counts, always takes 26 steps since there are 26 possible characters in the strings. 
    Adding it all up gives us T(n)=2n+26 steps. That is O(n). We have found a linear order of magnitude algorithm for solving this problem.
    
    Note: Although the last solution was able to run in linear time, 
    it could only do so by using additional storage to keep the two lists of character counts. 
    '''
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

if __name__ == '__main__':
    print(anagram_solution_checkoff('abcd','dcba'))
    print(anagram_solution_sort_strings('abcde','edcba'))
    print(anagram_solution_linear('apple','pleap'))