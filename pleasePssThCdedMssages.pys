import functools

def pleasePssThCdedMssages(array):
    thisList = l[:]
    listLength = len(thisList)
    thisList.sort(reverse = True)
    total = sum(thisList)
    remainder = total % 3
    elementRemoved = 0
    if (remainder == 0):
        newNumber = functools.reduce(lambda total, i: 10 * total + i, thisList, 0)
        return newNumber
    else:
        i = listLength - 1
        while (i >= 0):
            if ((thisList[i] % 3) == remainder):
                thisList.remove(thisList[i])
                elementRemoved = 1
                break
            i -= 1
        if not elementRemoved:
            remainder = 3 - remainder
            removedCount = 0
            i = listLength - 1
            while (i >= 0):
                if ((thisList[i] % 3) == remainder):
                    thisList.remove(thisList[i])
                    removedCount += 1
                    if (removedCount >= 2):
                        break
                i -= 1
    newNumber = functools.reduce(lambda total, i: 10 * total + i, thisList, 0)
    return newNumber
