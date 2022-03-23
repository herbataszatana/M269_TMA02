"""
Code file for M269 20J TMA02 Question 3.
Student version 1: 20/03/20
"""

def getMiddle(aNumber):
    """
    Return the middle two digits of integer aNumber if it has
    an even number of digits, otherwise return the single middle digit.

    Do NOT change this function.
    """
    numString = str(aNumber)
    midPoint = len(numString) // 2
    if (len(numString) % 2) == 0:
        middle = int(numString[midPoint - 1:midPoint+1])
    else:
        middle = int(numString[midPoint])
    return middle

def hashMidSquare(aNumber, tableSize):
    """
    Return the hash code for aNumber for a hash table of the given size,
    using the mid-square method.

    Do NOT change this function.
    """
    numberSquared = aNumber * aNumber
    midSequence = getMiddle(numberSquared)
    hashNumber = midSequence % tableSize
    return hashNumber



# Question 3(a)
# -------------

def stringHash(aString, tableSize):
    """
    Return the hash code for aString for a hash table of the given size,
    following the method explained in Question 3(a).
    """
    x = 0
    hash = 0
    for i in range(len(aString)):
        ascii_code = ord(aString[i])
        x = x + ascii_code
    hash =(hashMidSquare(x, tableSize))
    return hash

# Question 3(b)
# -------------

def createTable(tableSize):
    """Return a list of length tableSize, with all items being None."""
    table = []
    for i in range(0, tableSize):
        table.append(None)
    return table



# Question 3(c)
# -------------
#

def addItem(aString, aHashTable):
    added= ''
    i = 1
    stop = False
    h = (stringHash(aString, len(aHashTable)))
    k = len(aHashTable) -1
    while not stop:
        if aHashTable[h] == None:
            aHashTable[h] = aString
            stop = True
            added= 'yes'
            
        else:
            if i < k:
                h = (stringHash(aString, len(aHashTable)) + (i**2))%len(aHashTable)
                i = i + 1
                added= 'no'
            else:
                break
                added= 'no'
    if added == 'no':
        return True
    else:
        return False

