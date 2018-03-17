# Blackjack Strategy Tester

This project is an attempt to test some simple strategies for playing Blackjack.

The game simulates two participants, the Player and the Dealer and it could be played in two modes:
 
 1. __Manual mode__ where the user decides for the Player to take or not the next card by clicking 'y' or 'n' keys, and 
 2. __Auto mode__ where a preconfigured strategy decides for the Player what to do next. Auto mode allows to play tens of thousand games and see if the strategy is able to provide good results.
 
To begin with, I implemented a simple strategy that is based on a maximum score acquired during a game. For example, if threshold is set to 16 then the Player woulid get a new card only if Player's own score is less than 16 and stop otherwise.
 
Each game starts with a brand new shuffled deck. As far as I could see, this is the most generic scenario that provides a good collection of data that could be used for statistical analysis.
 
So far after running 100,000 games I've got the following results: 

|__Threshold__| 14| 15| 16| 17| 18| 19| 20|
|------------:|---|---|---|---|---|---|---|
|__Winnings__|40.95%|42.58%|43.54%|43.21%|41.27%|37.41%|30.41%|
 

If the logic in my coding is correct, this means that if the Player relies only on a max threshold, in the long run there is no chance to win the Dealer. In other words, this is not a winning strategy.  

(more strategies to be added...)

The game could be played from command line by running ```game.py```