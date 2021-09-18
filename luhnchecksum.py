# Link to kattis problem https://open.kattis.com/contests/qo87nq/problems/luhnchecksum

line1= int(input())

for x in range(line1):
    sum = 0
    z = 1
    num = int(input())
    string1 = str(num)
    myList = []
    for y in range(len(str(num))):
        intc = int(string1[y])
        myList.insert(y , intc)
    myList.reverse()    
    for l in range(1,len(str(num)),2):

        
        tempsum = myList[l] * 2
        if (tempsum > 9):
            rem = tempsum % 10
            tempsum = 1 + rem
            myList[l] = tempsum
        else:
            myList[l] = tempsum
        z += 2
    for k in range(len(str(num))):
        sum = sum + myList[k]
        
    if (sum % 10 ) != 0:
        print('FAIL')
    else:
        print('PASS')
