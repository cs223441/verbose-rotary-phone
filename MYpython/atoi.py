'''
8. String to Integer (atoi)
Medium
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algor+      ithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is 
negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, 
integers less than -231 should be clamped 
to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:

Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.


Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
Constraints:

-231 <= x <= 231 - 1

#if integer's length is less than -231 then block it to -231 , similarly if integer's length is greater than 230 then block it to 230
#ignore " space "
#make "0032" --> 32
#make 0032+/-///*42--> 32*///+/-42
#if a-z or A-Z have found then stop 
'''
"""
#@solution
def atoi(a):
    l=[]
    kl=[]
    for k in a:
        if k=='a' or k=='b'or k=='c'or k=='d'or k=='e'or k=='f'or k=='g'or k=='h'or k=='i'or k=='j'or k=='k'or k=='l'or k=='m'or k=='n'or k=='o'or k=='p'or k=='q'or k=='r'or k=='s'or k=='t'or k=='u'or k=='v'or k=='w'or k=='x'or k=='y'or k=='z'or k=='A'or k=='B'or k=='C'or k=='D'or k=='E'or k=='F'or k=='G'or k=='H'or k=='I'or k=='J'or k=='K'or k=='L'or k=='M'or k=='N'or k=='O'or k=='P'or k=='Q'or k=='R'or k=='S'or k=='T'or k=='U'or k=='V'or k=='W'or k=='X'or k=='Y'or k=='Z':
            break
        else:
            l.append(k)
    
    for c in l:
        if c==' ':
            continue
        elif c=='+':
            continue
        else:
            kl.append(c)
    
    ss=""
    for c in range(len(kl)):
      ss=ss+kl[c]
    
    ss=int(ss)
    print(f"ans:{ss}")
    print(f"datatype:{type(ss)}")
    
atoi("   42")
"""