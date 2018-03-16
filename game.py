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
    while dealer.score() < player.score():
        card = deck.next_card()
        dealer.take_card(card)

        print('\nDealer:')
        dealer.show_position()

        if pause:
            sleep(2)

    if dealer.score() > 21:
        print('\nDealer is busted - you won!')
        return

    if player.score() > dealer.score():
        print('\nYou won!')
    else:
        print('\nYou lost...')

    return


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
        player.drop_cards()
        dealer.drop_cards()

        deal(deck=deck, dealer=dealer, player=player, pause=True)

        reply = raw_input('\nWould you like to play again? (y/n): ')
        game_on = reply[:1].lower() == 'y'

    print('\nIt was good to see you here {}, good bye'.format(player.name))


def auto_deal(deck, dealer, player, strategy):

    # player take 2 cards
    player.take_card(deck.next_card())
    player.take_card(deck.next_card())

    while strategy.take_new_card(player):
        player.take_card(deck.next_card())

    # get out busted player
    if player.score() > 21:
        return 0

    # dealer take 2 cards
    dealer.take_card(deck.next_card())
    dealer.take_card(deck.next_card())

    while dealer.score() < player.score() and dealer.score() < 21:
        dealer.take_card(deck.next_card())

    # define winner
    if dealer.score() > 21:
        return 1
    if player.score() > dealer.score():
        return 1
    return 0


def test_strategy(strategy, num_of_games):

    player = Person('Player')
    dealer = Person('Dealer')
    results = []

    while num_of_games > 0:

        deck = get_new_deck()

        player.drop_cards()
        dealer.drop_cards()

        # final_result is 1 in case of a win and 0 in case of loss or draw
        final_result = auto_deal(deck, dealer, player, strategy)
        results.append(final_result)

        num_of_games -= 1

    return results


def auto_play(num_of_games):

    thresholds = [14, 15, 16, 17, 18, 19, 20]

    for threshold in thresholds:

        strategy = Strategy(score=threshold)

        results = test_strategy(strategy=strategy,
                                num_of_games=num_of_games)

        print('\nPlayer threshold: {}'.format(threshold))

        total_wins = sum(results)
        win_percent = total_wins * 100 / num_of_games

        print('Winning percent: {}%'.format(win_percent))


if __name__ == '__main__':

    choice = raw_input('Would you like Manual or Auto game? {m/a): ')

    if choice[:1].lower() == 'm':
        play()
    else:
        num_of_games = raw_input('Please, enter the numnber of games you\'d like to simulate: ')
        try:
            nog = int(num_of_games)
            auto_play(num_of_games=nog)
        except:
            print('Sorry, {} is not a number, good bye'.format(num_of_games))