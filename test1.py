# /usr/bin/python
# -*- coding: utf-8 -*-

import random

drawncards = []

# カードを引く
def choice_card():
    # トランプカード定義
    card_num = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    card_mark = ["club", "diamond", "heart", "spade"]

    is_repeat_choice = False
    choice_card = []
    while is_repeat_choice != True:
        choice_card = [random.choice(card_mark), random.choice(card_num)]
        #print choice_card    
        drawncards.append(choice_card)
        #print drawncards
        is_repeat_choice = check_overlap_card(choice_card)    
    return choice_card

# カードをダブらないようにチェックする
# かぶる:True or かぶらない:False 
def check_overlap_card(choice_card):
    i = 0
    choiced_mark = choice_card[0]
    choiced_num  = choice_card[1]
    while i < len(drawncards):
        drawn_mark = drawncards[i][0]
        drawn_num  = drawncards[i][1]
        if choiced_mark == drawn_mark:
            if choiced_num == drawn_num:
                return True
        i = i + 1
    return False

# カードを表示する
def print_card(card_list):
    i = 0
    #print card_list[0]
    while i < len(card_list):
        print card_list[i],
        i = i + 1

# 点数を計算する
def calc_score(card_list):
    i = 0
    score = 0
    while i < len(card_list):
        #print card_list
        card_num = card_list[i][1]
        #print card_num
        if card_num in ["J", "Q", "K"]:
            score = score + 10
        elif card_num == "A":
            score = score + 1
        else:
            score = score + int(card_num)
        #print score
        i = i + 1
    return score

# 勝ち負け判定
# 0 : player win
# 1 : dealer win
# 2 : draw
def judgment(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return 2
    elif player_score > 21  and dealer_score  21:
        return 1
    else:
        if player_score > dealer_score:
            return 0
        elif player_score < dealer_score:
            return 1
        else:
            return 2    

# 1. 52枚のカードを配る
# player : 2枚得る  dealer : 2枚得る（もう一枚は裏側）

# print choice_card
player_have_cards = []
player_have_cards.append(choice_card())
dealer_have_cards = []
dealer_have_cards.append(choice_card())

player_have_cards.append(choice_card())

print "player card is ",
print_card(player_have_cards)
print
print "dealer card is ",
print_card(dealer_have_cards)
print "['?', '?']"
dealer_have_cards.append(choice_card())

#drawncards = [['diamond', '4'], ['club', '5'], ['heart', '2'], ['diamond', '6']]
#print check_overlap_card(['diamond', '4'])
#print check_overlap_card(['diamond', '2'])
#print check_overlap_card(['club', '2'])

# 2. 3枚目以降のカードを引くか選択させる
is_player_draw_card = "yes"
count_player_drawn_card = 2

while (is_player_draw_card == "yes"):
    print "Do you draw one more card? Now, you draw " + str(count_player_drawn_card) + " cards."
    print "Please answer, yes or no ->",
    is_player_draw_card = raw_input()
    if is_player_draw_card == "yes":
        count_player_drawn_card = count_player_drawn_card + 1
        choiced_more_card = choice_card()
        print "player draw " + str(choiced_more_card)
        player_have_cards.append(choiced_more_card)
    else :
        print "player do not draw..."

    is_dealer_draw_card = random.randint(0,1)
    if is_dealer_draw_card == 1:
        print "dealer draw card.",
        choiced_more_card = choice_card()
        #print "dealer draw " + str(choiced_more_card)
        dealer_have_cards.append(choiced_more_card)
    else :
        print "dealer do not draw card."

# 3. 得点計算＆結果    
player_score = calc_score(player_have_cards)
dealer_score = calc_score(dealer_have_cards)

result = judgment(player_score, dealer_score)

print "Result -------------------"
print "player card is ",
print_card(player_have_cards)
print " score is " + str(player_score) + " point."
print "dealer card is ",
print_card(dealer_have_cards)
print " score is " + str(dealer_score) + " point."

if(result == 0):
    print "You Win!"
elif(result == 1):
    print "Dealer win. You Lose"
else:
    print "Draw"