import numpy as np

def getList():
    file = open('DNAconverted.txt','r')
    list = []

    lines = file.readlines()
    for line in lines:
        if len(line)<100:
            continue
        else:
            line = line.strip("\n").strip(" ")
            onlyNum = line[0:]
            length = len(onlyNum)
            print(length)
            list.append(onlyNum)
    
    return list, length
def writeFile(newMatrix):

    np.savetxt('Matrix1.csv',newMatrix,delimiter = ',')
def main():
    list,length = getList()
    comaSepList = []
    for eachPart in list:
        comaSep = []
        for i in range(length):
            eachNum = eachPart[i]
            comaSep.append(eval(eachNum))
        comaSepList.append(comaSep)

    array = np.array(comaSepList)

    print repr(array)
    writeFile(array)
    
            
main()
