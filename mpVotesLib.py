# mpVotesLib.py some sueful definition and functions for playing with politcal data
'''
    File name: mpVotesLib.py
    Author: Ryan Nichol
    Date created: 01/04/2019
    Date last modified: 01/04/2019
    Python Version: 2.7
'''


class Party:
     Conservative = 1
     Labour = 2
     Independent = 3
     LiberalDemocrat = 4
     SNP = 5
     DUP = 6
     PlaidCymru=7
     SinnFein=8
     Green=9
     Speaker=10
     Unknown=11

def getPartyIndex(partyString):
    return {
        "Conservative":Party.Conservative,
        "Labour":Party.Labour,
        "Independent":Party.Independent,
        "Liberal Democrat":Party.LiberalDemocrat,
        "Scottish National Party":Party.SNP,
        "Democratic Unionist Party":Party.DUP,
        "Plaid Cymru":Party.PlaidCymru,
        "Sinn F?in":Party.SinnFein,
        "Green Party":Party.Green,
        "Speaker":Party.Speaker}.get(partyString,Party.Unknown) 



def getMPNodeList(csvStringFromWebsite):
    import csv
    #Skip the first 10 lines
    reader = csv.DictReader(csvStringFromWebsite.splitlines()[9:])

    nodeList=[]
    
    for row in reader:
        node={"id": row["Member"], "group": getPartyIndex(row["Party"]), "value": 1}
        nodeList.append(node)
    return nodeList

def getAyeNoLists(csvStringFromWebsite,title=''):
    import csv
    ayeList=[]
    noList=[]

#    print csvStringFromWebsite.splitlines()[0]
    actualDivisionList=[int(s) for s in csvStringFromWebsite.splitlines()[0].split() if s.isdigit()]
#    print actualDivision
    if title=='':
        title=csvStringFromWebsite.splitlines()[3]
    print "Working title",title
        
    #Skip the first 10 lines
    reader = csv.DictReader(csvStringFromWebsite.splitlines()[9:])

    for row in reader:
        link={"source": row["Member"], "target": title, "value": 1}
        if(row["Vote"]=="Aye"):
            ayeList.append(link)
        elif(row["Vote"]=="No"):
            noList.append(link)
    

    return { "ayes":ayeList, "noes":noList, "title":title, "division":actualDivisionList[0]}

     
if __name__ == "__main__":
    print Party.Conservative
