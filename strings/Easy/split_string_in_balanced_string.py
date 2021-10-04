""""
QUESTION :

Balanced  strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s , split it in the maximum number of balanced string.

Return the maximum amount of split balanced strings.
link: https://leetcode.com/problems/split-a-string-in-balanced-strings/


** ** ** ** ** *APPROACH ** ** ** ** ** **
We will traverse through the string and increase the count if L is found and decrease if R is found, so after a certain
 point when both are equal (i.e L and R) count would be 0 and we will again start with the next character

"""

def StringSplit(s) -> int:
    #Initializing count to 0  to keep a track of  adjacent L and R
     #res to store the total number of substrings
    current = 0
    res = 0
    for i, c in enumerate(s):
        if c=='L':
            current+=1
        else:
            current-=1
        #If count is equal to 0 , we have successfully found one substring
		#Hence we will increase result by 1
        if current == 0: res += 1
    return res


s = input("Enter a string : ")
print("The number of substrings formed is : ",StringSplit(s))

"""
Time complexity : O(N) where N is the length of the string 

OUTPUT :
Enter a string : LRLRLLRRLR
The number of substrings formed is :  4


"""