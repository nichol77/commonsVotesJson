

import csv



voteList=['inidcative/Division655.csv','inidcative/Division656.csv',
          'inidcative/Division657.csv','inidcative/Division658.csv',
          'inidcative/Division659.csv','inidcative/Division660.csv',
          'inidcative/Division661.csv','inidcative/Division662.csv']

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

    vote={"voteId":voteId,"mpList":mpList}
    voteListOut.append(vote)
    voteId=voteId+1


with open('mpVoteEdgeNo.csv', mode='w') as csv_file:
    fieldnames = ["Source","Target","Type","Id","Label","timeset","Weight"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    edgeId=0
    
    for vote in voteListOut:
        for mp in vote["mpList"]:
            if mp["Vote"]=="No":
                writer.writerow({"Source":mp["idnum"],"Target":vote["voteId"],"Type":"Undirected","Id":edgeId,"Label":"","timeset":"","Weight":1})
                edgeId=edgeId+1
    csv_file.close()
    
    

