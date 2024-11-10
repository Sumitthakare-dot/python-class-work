#WAP to accept scores of two team
#(example india,pakistan )and make a decision who won the match
score1=int(input("Enter score of india"))
score2=int(input("Enter score of pakistan"))
 
if(score1>score2):
    print("india won the match")
elif(score2>score1):
    print("pakistan won the match")     
else:
    print("Match draw")    