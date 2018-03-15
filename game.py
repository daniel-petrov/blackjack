from deck import Deck
from person import Person
from strategy import Strategy
from time import sleep


def get_new_deck():

    deck = Deck()
    deck.shuffle()
    return deck


def deal(deck, dealer, player, pause=False):

    # player
    while deck.cards_left() != 0:
        reply = raw_input('\nNew card? (y/n) ')

        if 'y' in reply.lower():
            card = deck.next_card()
            player.take_card(card)

            print('\nYou:')
            player.show_position()

            if player.score() > 21:
                print('You are busted!')
                return
        else:
            break

    # dealer
    while deck.cards_left() != 0:
        card = deck.next_card()
        dealer.take_card(card)

        print('\nDealer:')
        dealer.show_position()

        if dealer.score() > 21:
            print('Dealer is busted! You won!')
            return

        if dealer.score() >= 18:
            break

        if pause:
            sleep(2)

    if player.score() > dealer.score():
        print('\nYou won!')
    else:
        print('\nYou lost...')

    return


def auto_deal(deck, dealer, player, strategy, dealer_theshold):

    # player
    player.take_card(deck.next_card())
    player.take_card(deck.next_card())

    while strategy.take_new_card(player):
        player.take_card(deck.next_card())

    # get out busted player
    if player.score() > 21:
        return 'dealer'

    # dealer
    dealer.take_card(deck.next_card())
    dealer.take_card(deck.next_card())

    while dealer.score() < player.score() and dealer.score() < 21:
        dealer.take_card(deck.next_card())

    # define winner
    if dealer.score() > 21:
        return 1
    if player.score() > dealer.score():
        return 1
    if player.score() == dealer.score():
        return 0
    return 0


def play():

    player_name = raw_input('Hi there!\nWhat\'s your name: ')
    print('Hello {}, it\'s good to see you here!'.format(player_name))

    reply = raw_input('Would you like to play Black Jack? (y/n) ')
    game_on = reply[:1].lower() == 'y'

    if not game_on:
        print('Thank you for visiting us {}, good bye'.format(player_name))
        exit(0)

    player = Person(player_name)
    dealer = Person('Dealer')

    while game_on:

        deck = get_new_deck()
        player.drop_card()
        dealer.drop_card()

        deal(deck=deck, dealer=dealer, player=player, pause=True)

        reply = raw_input('\nWould you like to play again? (y/n): ')
        game_on = reply[:1].lower() == 'y'

    print('\nIt was good to see you here {}, good bye'.format(player.name))


def test_strategy(strategy, num_of_games, dealer_threshold):

    player = Person('Player')
    player_results = []
    dealer = Person('Dealer')
    dealer_results = []

    while num_of_games > 0:

        deck = get_new_deck()

        player.drop_card()
        dealer.drop_card()

        winner = auto_deal(deck, dealer, player, strategy, dealer_threshold)

        if winner == 'player':
            player_results.append(1)
            dealer_results.append(0)
        elif winner == 'dealer':
            dealer_results.append(1)
            player_results.append(0)
        else:
            dealer_results.append(0)
            player_results.append(0)

        num_of_games -= 1

    return (dealer_results, player_results)




if __name__ == '__main__':

    # play()
    thresholds = [14, 15, 16, 17, 18, 19, 20]

    num_of_games = 100000

    for dealer_threshold in thresholds:

        for player_threshold in thresholds:

            strategy = Strategy(score=player_threshold)

            player_wins, dealer_wins = test_strategy(strategy=strategy,
                                                     num_of_games=num_of_games,
                                                     dealer_threshold=dealer_threshold)

            # print('\nPlayer: {}'.format(player_wins))
            # print('Dealer: {}'.format(dealer_wins))

            print('\n\nDealer threshold: {}'.format(dealer_threshold))
            print('Player threshold: {}'.format(player_threshold))

            # print('\nPlayer wins: {}'.format(sum(player_wins)))
            # print('Dealer wins: {}'.format(sum(dealer_wins)))

            player_total = sum(player_wins)
            dealer_total = sum(dealer_wins)

            # winner = 'Player' if player_total > dealer_total else 'Dealer'

            # if player_total > dealer_total:
            #     winner = 'Player'
            #     percent = player_total * 100 / (player_total + dealer_total)
            # else:
            #     winner = 'Dealer'
            #     percent = dealer_total * 100 / (player_total + dealer_total)
            #
            # print('\nWinner: {}'.format(winner))
            # print('Percent: {}%'.format(percent))

            win_percent = dealer_total * 100 / num_of_games
            print('Winning percent: {}%'.format(win_percent))