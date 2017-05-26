import string


"""



"""


def cleanFile(text_file):
    with open(text_file,"r") as fin, open("MatchSquads-2015_final.txt","w") as fout:
        flag = 0
        temp = ""
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END MATCH" not in var and "NEXT TEAM" not in var and "..." not in var and "Substitutes" not in var:
                if flag == 0:
                    temp = ""
                    temp += var
                    flag = 1
                elif flag == 1:
                    if "Goalkeeper" in var or "Defender" in var or "Midfielder" in var or "Forward" in var:
                        temp = temp + " " + var
                        flag = 0
                        fout.write(temp + '\n')
                    else:
                        temp = temp + " " + var
            else:
                fout.write(var + '\n')

    fin.close()
    fout.close()



def removeSquadNumbers():
    # Removing squad numbers
    with open("MatchSquads-2015_final.txt", "r") as fin, open("MatchSquads_2015-final.txt", "w") as fout:
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END,MATCH" not in var and "NEXT,TEAM" not in var and "..." not in var and "Substitutes" not in var:
                x = var.split(',')
                x.pop(0)
                new_var = ""
                for y in x:
                    if new_var == "":
                        new_var = y
                    else:
                        new_var = new_var + "," + y
                fout.write(new_var + '\n')
            else:
                fout.write(var + '\n')

    fin.close()
    fout.close()


def identifyPlayerNames():
    with open("MatchSquads_2015-final.txt","r") as fin, open("MatchSquads-2015_final.txt","w") as fout:
        for line in fin:
            var = str(line)
            var = var.rstrip('\n')
            if "Positions" not in var and "END,MATCH" not in var and "NEXT,TEAM" not in var and "..." not in var and "Substitutes" not in var:
                x = var.split(',')
                new_var = ""
                for y in x:
                    if "'" not in y and "Goalkeeper" not in y and "Defender" not in y and "Midfielder" not in y and "Forward" not in y:
                        if new_var == "":
                            new_var = new_var + y
                        else:
                            new_var = new_var + " " + y
                    else:
                        new_var = new_var + "," + y
                fout.write(new_var + '\n')
            else:
                fout.write(var + '\n')



#Text file open
#ratings_file = open("PlayerRatings-2013-Final.txt","r")

#cleanFile("MatchSquads-2015.txt")
#removeSquadNumbers()
identifyPlayerNames()


