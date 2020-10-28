# MyPokerHandCheck

To execute this code, download the 2 files in the repository (the .py file with the code, and the .txt file with the text file that contains the poker hands). Then, execute it on the command line by "python poker.py"
The result returns one line in the command line with the result/score of the checks of all the hands in the .txt for the player1 and player

NOTE: As discussed with Simon, the logic of the code checks first the highest rank, if both player have the same rank,the logic checks the highest cards for the rank, and if it's still similar (e.g both players have only 1pair of the same value), then it checks the highest card in the remaining cards, if it's still the same value for both players it's a tie, nobody wins.
