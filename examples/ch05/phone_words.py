''' 

This programs returns all possible words for 7 digit number without 0 or 1 digits corresponding to proper phone digits.

Written by Alex Chalyy on 12/22/2021.

'''

''' status = "FAIL"

#---------------------------------------------------------------------------------------------------------------------

def GetAllWords(c):

#   This method prints all possible appropriate words from a 7 digit string. 

    

#---------------------------------------------------------------------------------------------------------------------

while status != "PASS":
    word = input("Please enter a 7 digit string: ")
    if (len(word) == 7 and '0' not in word and '1' not in word and word.isdecimal()):
        status = "PASS"
GetAllWords(c) '''

# hashTable[i] stores all characters
# that correspond to digit i in phone
hashTable = ["", "", "abc", "def", "ghi", "jkl",
			"mno", "pqrs", "tuv", "wxyz"]

# A recursive function to print all
# possible words that can be obtained
# by input number[] of size n. The
# output words are one by one stored
# in output[]


def printWordsUtil(number, curr, output, n):
        if(curr == n):
            print(output)
            return

        # Try all 3 possible characters
        # for current digir in number[]
        # and recur for remaining digits
        
        ''' print("one")
        print(f"curr = {curr}")
        print(f"type(curr) = {type(curr)}")
        print(f"type(number) = {type(number)}")
        print(f"type(number[curr]) = {type(number[curr])}")
        print(f"number[curr] = {number[curr]}")
        print(f"hashTable[int(number[curr])] = {hashTable[int(number[curr])]}")
        print(f"len(hashTable[int(number[curr])]) = {len(hashTable[int(number[curr])])}")
        print(f"range(len(hashTable[int(number[curr])]) = {range(len(hashTable[int(number[curr])]))}") '''
        for i in range(len(hashTable[int(number[curr])])):
            #print("two")
            output.append(hashTable[int(number[curr])][i])
            printWordsUtil(number, curr + 1, output, n)
            output.pop()
            if(int(number[curr]) == 0 or int(number[curr]) == 1):
                return

# A wrapper over printWordsUtil().
# It creates an output array and
# calls printWordsUtil()


def printWords(number, n):
	printWordsUtil(number, 0, [], n)

def getNumber():

    #   This method asks user for a 7 digit number that does not have 0/1.

    status = "FALSE"

    while status == "FALSE":
        number = input("Please enter a 7 digit number without 1 or 0: ")
        if number.find("0") == -1 and number.find("1") == -1 and len(number) == 7 and number.isdecimal():
            status = "TRUE"
    #print("here")
    return int(number)

# Driver function
if __name__ == '__main__':
        #number = [2, 3, 4]
        number = getNumber()
        n = len(str(number))
        printWords(str(number), n)

    # This code is contributed by prajmsidc
