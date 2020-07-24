'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
'''

secret = "1123"
guess = "0111"


def getHint(secret, guess):
    bull,cow=0,0
    dct_secret = {}
    dct_guess = {}
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            bull+=1

        else: # 1_23 and 0_11
            ### handleing dct_guess ####
            if guess[i] in dct_guess:
                dct_guess[guess[i]]+=1
            else:
                dct_guess[guess[i]] = 1

            ### handleing dct_secret ####    
            if secret[i] in dct_secret:
                dct_secret[secret[i]]+=1
            else:
                dct_secret[secret[i]]=1
                
    # counting cow         
    for i in dct_guess:
        if i in dct_secret:
            cow += min(dct_secret[i],dct_guess[i])
            
    print ('{}A{}B'.format(bull,cow))





getHint(secret, guess)



# 1. if when secret[i]==guess[i] , meaning, both index and value are paired, then bull +=1,
# 2. else when secret[i]!=guess[i]:
#      ### handleing dct_guess ####
#      a. if this element already in this dictionary as a key, we let this value +=1 represent how many times it showed.
#      b. else this element is a new key, then we let this key's value = 1
#      ### handleing dct_secret ####
#      c. repeat above procedure

#### so far 'bull' is counted, and dictionary apartfrom secret[i]=guess[i] is also builed
#### meaninng 1123 and 0111 are truncated as 1_23 and 0_11 ( here, _ do not hold a position, just for better looking)

# 3. for guess.key in dct_guess 
# ###('0' and '1' ---> dct_guess = {'0':1, '1':2})####
#    a. if guess.key in dct_secret
# ###('0' and '1' ---> dct_guess = {'1':1, '2':1，‘3’:1})####
#          we let cow + who ever minmum 
# ### in this case '1' is the common key,  dct_guess shows twice, while dct_secret shows only once,
# ### hence, the maxmum possible pair is decided by whoever minmum, then cow can only add 1

# 4. format printing
# ## version 1 : ('%dA%B')%(bull,cow)
# ## version 2 : ({}A{}B).format(bull,cow)