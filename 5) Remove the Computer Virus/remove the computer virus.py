def removeVirus(files):

    words = files.split(" ")
    keptWords = [0, 1]

    for i, j in enumerate(words):
        if i == 0 or i == 1:
            continue

        if words[i].find("virus") != -1 and words[i].find("notvirus") == -1 and words[i].find("antivirus") == -1:
            continue
        elif words[i].find("malware") != -1:
            continue
        elif words[i].find("notvirus") != -1 or words[i].find("antivirus") != -1:
            keptWords.append(i)
        else:
            keptWords.append(i)

    returnFiles = ""
    for i in keptWords:
        returnFiles += words[i] + " "

    if keptWords == [0, 1] or files.strip() == "PC Files:" or files.strip() == "PC Files: Empty":
        returnFiles = "PC Files: Empty"

    return returnFiles.strip()

"""
me naming my virus "notvirus.exe"
at the end of this file is where youll find cursed code like wtf was i cooking

meow

weekly challenge - sloth bytes - Remove the Computer Virus
assumptions:
- string is in format "PC Files: <file names with no spaces>"
- bad people will appropiately name their viruses and malware and not be misleading

the challenge:
Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.

Examples
removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
output = "PC Files: spotifysetup.exe, dog.jpg"

removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
output = "PC Files: antivirus.exe, cat.pdf"

removeVirus("PC Files: notvirus.exe, funnycat.gif")
output = "PC Files: notvirus.exe, funnycat.gif")

Notes
Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.

Return "PC Files: Empty" if there are no files left on the computer.
"""

    # index = -2
    # indexCheck = []
    # toRemove = []
    # toNotRemove = []
    # indexCheck.append(files.find("virus"))
    # indexCheck.append(files.find("malware"))
    # indexCheck.append(files.find("notvirus"))
    # indexCheck.append(files.find("antivirus"))

    # while index == -2:
    #     print(indexCheck)
    #     if toRemove != []:
    #         indexCheck.append(files.find("virus", toRemove[-1][0] + 1))
    #         indexCheck.append(files.find("malware", toRemove[-1][0] + 1))
    #     elif toRemove == []:
    #         indexCheck.append(files.find("virus"))
    #         indexCheck.append(files.find("malware"))
        
    #     if toNotRemove != []:
    #         indexCheck.append(files.find("notvirus", toNotRemove[-1][0] + 1))
    #         indexCheck.append(files.find("antivirus", toNotRemove[-1][0] + 1))
    #     elif toNotRemove == []:
    #         indexCheck.append(files.find("notvirus"))
    #         indexCheck.append(files.find("antivirus"))

    #     if indexCheck[0] != -1:
    #         removeIndex = indexCheck[0]
    #         index = files.find("notvirus", indexCheck[0] - 3, indexCheck[0] + 5)
    #         if not (index == removeIndex - 3 and index != -1):
    #             toRemove.append([removeIndex, 1])
    #             removeIndex = -5

        
    #     print(indexCheck)

    #     if indexCheck[1] != -1:
    #         toRemove.append([indexCheck[1], 1])

    #     if indexCheck[2] != -1:
    #         toNotRemove.append([indexCheck[2], 1])

    #     if indexCheck[3] != -1:
    #         toNotRemove.append([indexCheck[3], 1])

    #     if indexCheck[0] == -1 and indexCheck[1] == -1 and indexCheck[2] == -1 and indexCheck[3] == -1:
    #         index = -1
    #     else:
    #         index = -2

    #     indexCheck = []
    
    # if toRemove != []:
    #     splitFiles = files.split(" ")
    #     totalLength = 10
    #     endList = []

    #     for i, j in enumerate(splitFiles):
    #         if i == 0 or i == 1:
    #             continue

    #         for m, n in enumerate(toRemove):
    #             if not (totalLength < m[1] < totalLength + len(1)):
    #                 endList.append(i)


    # return endList