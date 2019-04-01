# getCSVFromCommonVotes this script downloadeds a CSV files from https://commonsvotes.digiminster.com
'''
    File name: getCSVFromCommonVotes
    Author: Ryan Nichol
    Date created: 01/04/2019
    Date last modified: 01/04/2019
    Python Version: 2.7
'''

baseURL='https://commonsvotes.digiminster.com/Divisions/DownloadCSV/'
import sys, getopt
import urllib2
import mpVotesLib
import json

def main(argv):
    division= ''
    outputdir = '.'
    makejson = False
    makenodes= False
    title=''
    try:
        opts, args = getopt.getopt(argv,"hjnd:o:t:",["division=","odir=","json","nodes","title="])
    except getopt.GetoptError:
        print 'test.py -d <division number> -o <outputdir> [-j]'
        sys.exit(2)
    for opt, arg in opts:        
        if opt == '-h':
            print 'test.py -d <divison number> -o <outputdir>'
            sys.exit()
        elif opt in ("-d", "--divison"):
            division = arg
        elif opt in ("-o", "--odir"):
            outputdir = arg
        elif opt in ("-t", "--title"):
            title = arg
        elif opt in ("-j","--json"):
            makejson=True
        elif opt in ("-n","--nodes"):
            makenodes=True
    print 'Division is ', division
    print 'Output directory is ', outputdir

    if division=="":
        print "You need to specify which division to download"
        print "For a list of recent division see https://commonsvotes.digiminster.com"
        sys.exit()

    url=baseURL+division
    print "Trying to download CSV from:",url
    response = urllib2.urlopen(url)
    data = response.read()
    #    print(data)
    if(makejson):
        outfile=outputdir+"/division"+division+".json"
        print "Writing JSON",outfile
        outputThing=mpVotesLib.getAyeNoLists(data,title)        
        with open(outfile, 'w') as jsonfile:
            json.dump(outputThing, jsonfile)
            
        if(makenodes): 
            outputNodes={}
            outputNodes["nodes"]=mpVotesLib.getMPNodeList(data)
            nodefile=outputdir+"/mpNodes.json"
            print "Writing JSON",nodefile
            with open(nodefile, 'w') as jsonfile:
                json.dump(outputNodes, jsonfile)
            
        
    else:
        outfile=outputdir+"/division"+division+".csv"
        print "Writing CSV",outfile
        with open(outfile, mode='w') as csv_file:
            csv_file.write(data)
            csv_file.close()

    


    

        
if __name__ == "__main__":
   main(sys.argv[1:])
   print mpVotesLib.Party.Conservative,"or",mpVotesLib.getPartyIndex("Conservative")
