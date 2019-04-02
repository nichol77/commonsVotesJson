#!/bin/bash

for ind in `seq 268 669`; do python getCSVFromCommonVotes.py -d $ind -j; done

python getCSVFromCommonVotes.py -d 655 -j -t "No Deal"
python getCSVFromCommonVotes.py -d 656 -j -t "Common Market 2.0"
python getCSVFromCommonVotes.py -d 657 -j -t "EFTA and EEA"
python getCSVFromCommonVotes.py -d 658 -j -t "Customs Union"
python getCSVFromCommonVotes.py -d 659 -j -t "Labour Plan"
python getCSVFromCommonVotes.py -d 660 -j -t "Revocation to avoid"
python getCSVFromCommonVotes.py -d 661 -j -t "Referendum"
python getCSVFromCommonVotes.py -d 663 -j -t "Exit Day Ammendment"
python getCSVFromCommonVotes.py -d 664 -j -t "Withdrawal Agreement"
python getCSVFromCommonVotes.py -d 666 -j -t "Customs Union"
python getCSVFromCommonVotes.py -d 667 -j -t "Common Market 2.0"
python getCSVFromCommonVotes.py -d 668 -j -t "Confirmatory public vote"
python getCSVFromCommonVotes.py -d 669 -j -t "Parliamentary Supremacy"
