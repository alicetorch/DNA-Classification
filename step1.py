def openFile():
    file  = open("ChrB01.txt","r")
    lines = file.readlines()
    return lines

def DNApart(lines):
    list = ""
    for DNA in lines:
        noAs = DNA[-37:].count("A")
        noTs = DNA[-37:].count("T")
        noCs = DNA[-37:].count("C")
        noGs = DNA[-37:].count("G")
        if noAs > 0 and noTs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("A","1").replace("T","0")
        if noAs > 0 and noCs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("A","1").replace("C","0")
        if noAs > 0 and noGs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("A","1").replace("G","0")
        if noTs > 0 and noCs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("T","1").replace("C","0")
        if noTs > 0 and noGs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("T","1").replace("G","0")
        if noCs > 0 and noGs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("C","1").replace("G","0")
        if noAs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("A","1")
        if noTs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("T","1")
        if noCs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("C","1")
        if noGs > 0:
            DNA = DNA[:-37] + DNA[-37:].replace("G","1")
        list = list + DNA
    return list

def writeNewFile(newDNA):
    file = open("ChrB01_0&1.txt","w")
    file.write(newDNA)
    file.close()
            
def main():
    #open the file
    lines = openFile()
    #count DNA
    newDNA = DNApart(lines)
    #write new file
    writeNewFile(newDNA)
    
main()

