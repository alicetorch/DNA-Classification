def convert(i):
    file = open("ChrB01_0&1.txt","r")
    lines = file.readlines()
    a = ""
    for line in lines:
        line = line.split()[2]
        a = a+line[i]
    return a+"\n"

def writeNewFile(text):
    file = open("DNAconverted.txt","w")
    file.write(text)
    file.close()
            

def main():
    text = ""
    for i in range(36):
        newForm = convert(i)
        print(newForm)
        text = text+newForm+"\n"
 #   writeNewFile(text)
    
      
    
main()

