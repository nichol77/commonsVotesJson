# makeNetowrkJSON this script takes some downloaded CSV files from https://commonsvotes.digiminster.com and makes a new JSON suitable for displaying as a D3 force network graph
'''
    File name: makeNetworkJSON
    Author: Ryan Nichol
    Date created: 01/04/2019
    Date last modified: 01/04/2019
    Python Version: 2.7
'''


import csv
import json


voteNames=["No Deal","Common Market 2.0","EFTA and EEA","Customs Union",
           "Labour Plan","Revocation to avoid no deal","Referendum","Malthouse Plan B","Withdrawal Agreement"]
voteList=['inidcative/Division655.csv','inidcative/Division656.csv',
          'inidcative/Division657.csv','inidcative/Division658.csv',
          'inidcative/Division659.csv','inidcative/Division660.csv',
          'inidcative/Division661.csv','inidcative/Division662.csv','withdrawal/Division664.csv']

voteId=0
voteListOut=[]
for voteFile in voteList:    
    mpList=[]

    with open(voteFile, 'r') as csvFile:
        #Skip the first 10 lines
        for i in range(0,9):
            next(csvFile)
        reader = csv.DictReader(csvFile)
        idnum=8
        for row in reader:
            row["idnum"]=idnum
            idnum+=1
            mpList.append(row)
        csvFile.close()

    vote={"voteId":voteId,"mpList":mpList,"voteName":voteNames[voteId]}
    voteListOut.append(vote)
    voteId=voteId+1


outputThing={}
outputThing["nodes"]=[]
outputThing["links"]=[]


partyDict={ "Conservative":1, "Labour":2,"Independent":3,"Liberal Democrat":4,"Scottish National Party":5,"Democratic Unionist Party":6,"Plaid Cymru":7,"Sinn F?in":8, "Speaker":9, "Green":10}


firstTime=1
for vote in voteListOut:
    node={"id": vote["voteName"], "group": 0}
    nodeValue=0
    for mp in vote["mpList"]:
#        print mp
        if firstTime==1:
            try:
                group=partyDict[mp["Party"]]
            except (RuntimeError, TypeError, NameError, KeyError):
                group=11
            mpNode={"id": mp["Member"], "group": group, "value": 1}
            outputThing["nodes"].append(mpNode)                            
        
        link={"source": mp["Member"], "target": node["id"], "value": 1}
#        if mp["Vote"]=="Aye":
        if mp["Vote"]=="No":
            outputThing["links"].append(link)
            nodeValue=nodeValue+1

    node["value"]=nodeValue
    outputThing["nodes"].append(node)


    firstTime=0
 #       
    
#print (json.dumps(outputThing))
with open('mpVotesNo.json', 'w') as outfile:
    json.dump(outputThing, outfile)

    
#with open('mpVoteEdgeNo.csv', mode='w') as csv_file:
#    fieldnames = ["Source","Target","Type","Id","Label","timeset","Weight"]
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#    writer.writeheader()
#    edgeId=0
#    
#    for vote in voteListOut:
#        for mp in vote["mpList"]:
#            if mp["Vote"]=="No":
#                writer.writerow({"Source":mp["idnum"],"Target":vote["voteId"],"Type":"Undirected","Id":edgeId,"Label":"","timeset":"","Weight":1})
#                edgeId=edgeId+1
#    csv_file.close()
    
    

