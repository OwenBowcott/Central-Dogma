# The dictionary for the transation (this dictionary will store the DAN-amino acids mapping)
aa_d = {}
#while line:
#line[0] = key
#line: = answer

# the FASTA file (this list will store the FASTA file)
DNA_d = []

# the correct translation (is given for cross-checking)
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

#INPUT name of amino acid file (make sure that you keep the amino_acids.txt under Assignment8 folder)
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
#make sure to close the file after reading it
def get_amino_acids(name):
    aa_d = {}
    with open(name) as theFile:
        contents = theFile.read()
        lines = contents.split("\n")
        for i in lines:
            split = i.split(", ")
            if len(split[2:]) == 1:
                tup = (split[2])
            if len(split[2:]) == 2:
                tup = (split[2], split[3])
            if len(split[2:]) == 3:
                tup = (split[2], split[3], split[4])
            if len(split[2:]) == 4:
                tup = (split[2], split[3], split[4], split [5])
            if len(split[2:]) == 5:
                tup = (split[2], split[3], split[4], split[5], split[6])
            if len(split[2:]) == 6:
                tup = (split[2], split[3], split[4], split[5], split[6], split[7])
            aa_d[tup] = [split[0], split[1]]
        print(aa_d)
        return aa_d

#INPUT file name of the DNA file (make sure that you keep the DNA.txt under Assignment8 folder)
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
#make sure to close the file
def get_DNA(name):
    header = ""
    dna = ""
    with open(name) as theFile:
        contents = theFile.read()
        lines = contents.split("\n")
        for i in lines:
            if i == lines[0]:
                header = str(i)
            else:
                dna += str(i)
        lst = [header, dna]
        return lst

#INPUT FAST file
#RETURN a string representing the protein (convert the DNA to amino acids)
#using the dictionary
def translate(DNA_d):
    trans = ""
    for i in range(0, len(DNA_d[1]),3):
        temp = DNA_d[1][i:i+3]
        for keys in aa_d:
            tup = keys
            for key in keys:
                if temp == key:
                    ans = aa_d[tup]
                    trans += ans[1]
    return trans


    
# ! Important !

# To test the code of Problem-1, You may not run it directly in VSC (due to File not found error), 
# please follow the instructions below.

# 1. Open a new Terminal in VSC. 

# Run the below command in the terminal i.e. after typing in the command, hit enter
# 2. cd Assignment8

# Now run the a8.py in the newly opened terminal i.e. type the below command and hit enter
# 3. python3 a8.py

# It should print output on the terminal based on how much of the problem have you completed. Using this way
# of running, you can easily monitor your progress on this problem.


if __name__ == "__main__":
    '''for your use'''
    
    # #PROBLEM 1
    # #do not change file names
    fn1,fn2 = "amino_acids.txt","DNA.txt"
    aa_d = get_amino_acids(fn1)#,fn1
    DNA_d = get_DNA(fn2)#fn2
    protein = translate(DNA_d)

    print("Dictionary")
    print(aa_d)
    print("FASTA file")
    print(DNA_d)
    print("begin")
    print(protein)
    print(actual)
    print("end")
    print("Translations match:", str(protein == actual))

    #should return "PLHS"    
    print(translate(["nothing", "CCACTGCACTCA"]))

    #should returns "D-"
    print(translate(["nothing", "GACTAA"]))