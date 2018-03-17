# Blackjack Strategy Tester

This project is an attempt to test some simple strategies for playing Blackjack.

The game has two participants, the Player and the Dealer and it could be played in two modes:
 
 1. __Manual mode__ where the user decides to take or not the next card by clicking 'y' or 'n' keys, and 
 2. __Auto mode__ where a preconfigured strategy decides what to do next. Auto mode allows to play tens of thousand games and see if the strategy is able to provide good results.
 
 So far I implemented a simple strategy that is based on a maximum score acquired during a game. For example, the Player woulid get a new card if the score is less than 16 or stop otherwise.
 
 Every game starts with a brand new shuffled deck. As far as I could see, this is the most generic scenario that provides a good collection of data that could be used for statistical analysis.
 
 The game could be played from command line by running ```game.py``` 
 
 

