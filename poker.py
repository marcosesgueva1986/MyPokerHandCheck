import collections
from collections import defaultdict

card_values_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

score_player1=0
score_player2=0


def flush(my_array):
	
	if my_array[0][1]==my_array[1][1] and my_array[0][1]==my_array[2][1] and my_array[0][1]==my_array[3][1] and my_array[0][1]==my_array[4][1]:
		return True
	return False



def royal_flush(cards):

	isflush=flush(cards)
	ten=False
	jack=False
	queen=False
	ace=False
	
	for v in cards:
		
		if v[0]=='T':
			ten=True
		elif v[0]=='J':
			jack=True
		elif v[0]=='Q':
			queen=True
		elif v[0]=='K':
			king=True
		elif v[0]=='A':
			ace=True
		else:
			return False
	
	if isflush and ten and jack and queen and ace:
		return True
	else:
		return False


def two_pairs(cards):
    values = [j[0] for j in cards]
    value_reps = defaultdict(lambda:0)
    for v in values:
        value_reps[v]+=1
        #print('value_reps',value_reps)	
    if sorted(value_reps.values())==[1,2,2]:
        return True
    else:
        return False



def straight(cards):
    
	mycard_values = [0] * len(cards)
	j=0
	for v in cards:
		#print('v0',v[0])
		#print('card_value:',card_values_dict[ str(v[0]) ] )
		#print('my j vble',j)
		mycard_values[j]=card_values_dict[ str(v[0]) ]
		j=j+1
	mycard_values=sorted(mycard_values)
	#print('Inside function straight:',mycard_values)
	if mycard_values[0]+1==mycard_values[1] and mycard_values[1]+1==mycard_values[2] and mycard_values[2]+1==mycard_values[3] and mycard_values[3]+1==mycard_values[4]:       
		return True
	else:
		return False
		

def straight_flush(cards):
	if flush(cards) and straight(cards):
		return True
	else:
		return False

		
def full_house(cards):
    values = [j[0] for j in cards]
    value_reps = defaultdict(lambda:0)
    for v in values:
        value_reps[v]+=1
        #print('value_reps',value_reps)	
    if sorted(value_reps.values())==[2,3]:
        return True
    else:
        return False


def one_pair(cards):
	values = [j[0] for j in cards]
	value_reps = defaultdict(lambda:0)
	for v in values:
		value_reps[v]+=1 
		
	if 2 in value_reps.values():
		
		#print('value_reps',value_reps)
		#print('value_reps.keys',value_reps.keys() )
		#print('value_reps.values',value_reps.values() )
		
		#print("INSIDE function one_pair, the value of card with the pair is:",  list(value_reps.keys() )[ list(value_reps.values()).index(2)]  )
		
		return True
	else:
		return False
		
def three_cards(cards):
    values = [j[0] for j in cards]
    value_reps = defaultdict(lambda:0)
    for v in values:
        value_reps[v]+=1 
        #print("values",values)
        #print('value_reps',value_reps)			
    if 3 in value_reps.values() :
        return True
    else:
        return False

def four_cards(cards):
    values = [j[0] for j in cards]
    value_reps = defaultdict(lambda:0)
    for v in values:
        value_reps[v]+=1 
        #print("values",values)
        #print('value_reps',value_reps)			
    if 4 in value_reps.values() :
        return True
    else:
        return False

def check_rank(cards):
	if royal_flush(cards):
		return 10
	elif straight_flush(cards):
		return 9
	elif four_cards(cards):
		return 8
	elif full_house(cards):
		return 7
	elif flush(cards):
		return 6
	elif straight(cards):
		return 5
	elif three_cards(cards):
		return 4
	elif two_pairs(cards):
		return 3
	elif one_pair(cards):
		return 2
	else:
		return 1


def winner_rank(cards_player1, cards_player2):
	global score_player1
	global score_player2
	rank_player1=check_rank(player1)
	rank_player2=check_rank(player2)
	
	
	if rank_player1 > rank_player2:
		score_player1+=1
		#print("Player1 wins, rank",rank_player1, " Player1 score:", score_player1," Player2 score:", score_player2)
	elif rank_player1 < rank_player2:
		score_player2+=1
		#print("Player2 wins, rank",rank_player2, " Player1 score:", score_player1," Player2 score:", score_player2)
	else:
		#print("Same rank(",rank_player1 ,")both players, checking highest card in rank...")
		highest_card_rank(rank_player1, cards_player1, cards_player2 )
	
	
def highest_card_rank(rank, cards_player1, cards_player2 ):

	global score_player1
	global score_player2
	
	values1 = [j[0] for j in cards_player1]
	value_reps1 = defaultdict(lambda:0)
	for v in values1:
		value_reps1[v]+=1 
		
	values2 = [h[0] for h in cards_player2]
	value_reps2 = defaultdict(lambda:0)
	for w in values2:
		value_reps2[w]+=1
	
	
	#print('values reps player1: ',value_reps1 )
	#print('values reps player2: ',value_reps2 )
	
	if rank==2: #check the highest card in the pair
		highest_card_player1=card_values_dict[str(list(value_reps1.keys() )[ list(value_reps1.values()).index(2)] ) ]
		highest_card_player2=card_values_dict[str(list(value_reps2.keys() )[ list(value_reps2.values()).index(2)] )]
		#print("Comparing cards, highest card player1 value:", highest_card_player1 )
		#print("Comparing cards, highest card player2 value:", highest_card_player2 )
		
	
	elif rank==4 or rank==7: #check the highest card in the triple
		highest_card_player1=card_values_dict[str(list(value_reps1.keys() )[ list(value_reps1.values()).index(3)] )] 
		highest_card_player2=card_values_dict[str(list(value_reps2.keys() )[ list(value_reps2.values()).index(3)] )]
		#print("Comparing cards, highest card player1 value:", highest_card_player1 )
		#print("Comparing cards, highest card player2 value:", highest_card_player2 )
		
	elif rank==8: #check the highest card in the cuadruple
		highest_card_player1=card_values_dict[str(list(value_reps1.keys() )[ list(value_reps1.values()).index(4)] )]
		highest_card_player2=card_values_dict[str(list(value_reps2.keys() )[ list(value_reps2.values()).index(4)] )]
		#print("Comparing cards, highest card player1 value:", highest_card_player1 )
		#print("Comparing cards, highest card player2 value:", highest_card_player2 )
		
	elif rank==1 or rank==5 or rank==6 or rank==9: #check highest card of the 5
	
		mycard_values1 = [0] * len(cards_player1)
		j=0
		for v in cards_player1:
			mycard_values1[j]=card_values_dict[ str(v[0]) ]
			j=j+1
			
		mycard_values1=sorted(mycard_values1)
		highest_card_player1=mycard_values1[4]
		second_highest_card_player1=mycard_values1[3]
		
		
		
		mycard_values2 = [0] * len(cards_player2)
		j=0
		for w in cards_player2:
			mycard_values2[j]=card_values_dict[ str(w[0]) ]
			j=j+1
			
		mycard_values2=sorted(mycard_values2)
		#print("sorted_cards player2",mycard_values2)
		highest_card_player2=mycard_values2[4]
		second_highest_card_player2=mycard_values2[3]
		
		#print("Comparing cards, highest card player1:", highest_card_player1 )
		#print("Comparing cards, highest card player2:", highest_card_player2 )
	

	elif rank==3: #check the highest pair among the 2 pairs
		#print('inside rank3')
		
		#print('value_reps1:',value_reps1)
		extracted_card1=card_values_dict[ str(list(value_reps1.keys() )[ list(value_reps1.values()).index(1)] )  ]
		value_reps1.pop( list(value_reps1.keys() )[ list(value_reps1.values()).index(1)] ) 
		#print('value_reps1 after deleting one card:',value_reps1)
		#print('extracted_card1:',extracted_card1)
		
		#print('value_reps2:',value_reps2)
		extracted_card2=card_values_dict[ str(list(value_reps2.keys() )[ list(value_reps2.values()).index(1)] )  ]
		value_reps2.pop( list(value_reps2.keys() )[ list(value_reps2.values()).index(1)] ) 
		#print('value_reps2 after deleting one card:',value_reps2)
		#print('extracted_card2:',extracted_card2)
		
		
		mycard_values1 = [0] * len(value_reps1.keys() )
		j=0
		for v in value_reps1.keys():
			mycard_values1[j]=card_values_dict[ str(v[0]) ]
			j=j+1
			
		mycard_values1=sorted(mycard_values1)
		highest_card_player1=mycard_values1[-1]
		
		
		
		mycard_values2 = [0] * len(value_reps2.keys())
		j=0
		for w in value_reps2.keys():
			mycard_values2[j]=card_values_dict[ str(w[0]) ]
			j=j+1
			
		mycard_values2=sorted(mycard_values2)
		#print("sorted_cards player2",mycard_values2)
		highest_card_player2=mycard_values2[-1]
		
		#print("Comparing cards, highest card player1:", highest_card_player1 )
		#print("Comparing cards, highest card player2:", highest_card_player2 )
		
		
	
	else:
		print("---ERROR --- Rank not valid" )
	
	#comparing highest card in the rank
	if highest_card_player1 > highest_card_player2:
		score_player1+=1
		#print("Player1 wins, Player1 score:", score_player1  , "Player2 score:", score_player2 )
	elif highest_card_player1 < highest_card_player2:
		score_player2+=1
		#print("Player2 wins, Player1 score:", score_player1  , "Player2 score:", score_player2 )
	else: #3rd check
		#print("Same high card both players, checking the highest card in the remaining cards...")
	
		
		
		if rank==1: #I check the second highest card in the remaining cards
			extracted_card1=second_highest_card_player1
			extracted_card2=second_highest_card_player2
			#print('Highest remaining card Player1 value:',extracted_card1)
			#print('Highest remaining card Player2 value:',extracted_card2)
		
		if rank==3: #I already discarded cards in the prev function
			
			print()
			#print('Highest remaining card Player1 value:',extracted_card1)
			#print('Highest remaining card Player2 value:',extracted_card2)
			
		elif rank==2: #I discard the cards in the pair
		
			#print('value_reps1:',value_reps1)
			value_reps1.pop( list(value_reps1.keys() )[ list(value_reps1.values()).index(2)] ) 
			#print('value_reps1 after deleting one card:',value_reps1)
			#print('extracted_card1:',extracted_card1)
			
			#print('value_reps2:',value_reps2)
			value_reps2.pop( list(value_reps2.keys() )[ list(value_reps2.values()).index(2)] ) 
			#print('value_reps2 after deleting one card:',value_reps2)
			#print('extracted_card2:',extracted_card2)
			
			
			mycard_values1 = [0] * len(value_reps1.keys() )
			j=0
			for v in value_reps1.keys():
				mycard_values1[j]=card_values_dict[ str(v[0]) ]
				j=j+1
				
			mycard_values1=sorted(mycard_values1)
			extracted_card1=mycard_values1[-1]  #last value in the sorted array
			
			
			
			mycard_values2 = [0] * len(value_reps2.keys())
			j=0
			for w in value_reps2.keys():
				mycard_values2[j]=card_values_dict[ str(w[0]) ]
				j=j+1
				
			mycard_values2=sorted(mycard_values2)
			#print("sorted_cards player2",mycard_values2)
			extracted_card2=mycard_values2[-1]
			
			
		elif rank==4 or rank==7: #I discard the triple cards
		
			#print('value_reps1:',value_reps1)
			value_reps1.pop( list(value_reps1.keys() )[ list(value_reps1.values()).index(3)] ) 
			#print('value_reps1 after deleting one card:',value_reps1)
			#print('extracted_card1:',extracted_card1)
			
			#print('value_reps2:',value_reps2)
			value_reps2.pop( list(value_reps2.keys() )[ list(value_reps2.values()).index(3)] ) 
			#print('value_reps2 after deleting one card:',value_reps2)
			#print('extracted_card2:',extracted_card2)
			
			
			mycard_values1 = [0] * len(value_reps1.keys() )
			j=0
			for v in value_reps1.keys():
				mycard_values1[j]=card_values_dict[ str(v[0]) ]
				j=j+1
				
			mycard_values1=sorted(mycard_values1)
			extracted_card1=mycard_values1[-1]
			
			
			
			mycard_values2 = [0] * len(value_reps2.keys())
			j=0
			for w in value_reps2.keys():
				mycard_values2[j]=card_values_dict[ str(w[0]) ]
				j=j+1
				
			mycard_values2=sorted(mycard_values2)
			#print("sorted_cards player2",mycard_values2)
			extracted_card2=mycard_values2[-1]		
		
		elif rank==8:  #I discard the cards in the cuadruple
		
			#print('value_reps1:',value_reps1)
			value_reps1.pop( list(value_reps1.keys() )[ list(value_reps1.values()).index(4)] ) 
			#print('value_reps1 after deleting one card:',value_reps1)
			#print('extracted_card1:',extracted_card1)
			
			#print('value_reps2:',value_reps2)
			value_reps2.pop( list(value_reps2.keys() )[ list(value_reps2.values()).index(4)] ) 
			#print('value_reps2 after deleting one card:',value_reps2)
			#print('extracted_card2:',extracted_card2)
			
			
			mycard_values1 = [0] * len(value_reps1.keys() )
			j=0
			for v in value_reps1.keys():
				mycard_values1[j]=card_values_dict[ str(v[0]) ]
				j=j+1
				
			mycard_values1=sorted(mycard_values1)
			extracted_card1=mycard_values1[-1]
			
			
			
			mycard_values2 = [0] * len(value_reps2.keys())
			j=0
			for w in value_reps2.keys():
				mycard_values2[j]=card_values_dict[ str(w[0]) ]
				j=j+1
				
			mycard_values2=sorted(mycard_values2)
			#print("sorted_cards player2",mycard_values2)
			extracted_card2=mycard_values2[-1]		
		
		
		
		
		else:#it's a tie,nobody wins, do nothing
			tie=1
			#print("---ERROR in else, 3rd check CARDS player1:", cards_player1,  " cards player2:" , cards_player2)
				
		
		
		#print("3rd check, Comparing the remaining cards, highest card player1 value:", extracted_card1 )
		#print("3rd check, Comparing the remaining cards, highest card player2 value:", extracted_card2 )
		
		if extracted_card1 > extracted_card2:
			score_player1+=1
			#print("Player1 wins, Player1 score:", score_player1  , "Player2 score:", score_player2 )
		elif extracted_card1 < extracted_card2:
			score_player2+=1
			#print("Player2 wins, Player1 score:", score_player1  , "Player2 score:", score_player2 )
		else: #it's a tie,nobody wins, do nothing
			tie=1
			#print("There's a tie in the hand, nobody wins:", score_player1  , "Player2 score:", score_player2 ,  " CARDS player1:", cards_player1,  " cards player2:" , cards_player2)

		

#-------------------------------

f=open('poker-hands.txt','r')
#my_line=f.readline().rstrip().split(' ')

for line in f:
	#print("Reading line in while loop" )
	my_line=line.rstrip().split(' ')
	player1 = my_line[:len(my_line)//2]
	player2= my_line[len(my_line)//2:]
	#print(player1)
	#print(player2)

	winner_rank(player1, player2)
	#print("END  OF LINE---")

print("Player1 score:", score_player1  , "Player2 score:", score_player2 )	
f.close()

