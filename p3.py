import random
card_num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_type = ["♧", "♢", "♡", "♤"]
all_card = [ a + b for a in card_type for b in card_num] #全てのカードの文字列を格納
random.shuffle(all_card)
all_card2=[] #全てのカードの数値を格納

#カードの文字列を数値に変換してall_card2に格納
i=0
while i < 52:
    if "A" in all_card[i]:
        all_card2.append(11)
        i+=1
    elif "2" in all_card[i]: 
        all_card2.append(2)
        i+=1
    elif "3" in all_card[i]:
        all_card2.append(3)
        i+=1
    elif "4" in all_card[i]:
        all_card2.append(4)
        i+=1
    elif "5" in all_card[i]:
        all_card2.append(5)
        i+=1
    elif "6" in all_card[i]:
        all_card2.append(6)
        i+=1
    elif "7" in all_card[i]:
        all_card2.append(7)
        i+=1
    elif "8" in all_card[i]:
        all_card2.append(8)
        i+=1
    elif "9" in all_card[i]:
        all_card2.append(9)
        i+=1
    elif "10" in all_card[i]:
        all_card2.append(10)
        i+=1
    elif "J" or "Q" or "K" in all_card[i]:
        all_card2.append(10)
        i+=1
    else:
        print("error")

#カードの文字列(♡2,♢Aなど)
all_card_player = all_card[0:25]
all_card_dealer = all_card[25:]
#カードの数値
all_card_player2 = all_card2[0:25]
all_card_dealer2 = all_card2[25:]

#手札の表示
print("あなたの手札：",all_card_player[0:2])
print("ディーラーの手札：",all_card_dealer[0:2])
player_score = all_card_player2[0] + all_card_player2[1]
dealer_score = all_card_dealer2[0] + all_card_dealer2[1]

#追加でカードを引く処理
add ="y"
i = 0
j = 0
while add =="y":
    print("追加でカードを引きますか？ 引く：y 引かない：n")
    add = input()
    if add == "y":
        i+=1
        print("あなたはカードを引きました")
        print("あなたの手札：",all_card_player[0:2+i])
        player_score = player_score + all_card_player2[1+i]
    else:
        print("あなたはカードを引きません")
    
    if dealer_score <= 16 and add == "y":
        j+=1
        print("ディーラーがカードを引きます")
        print("ディーラーの手札：",all_card_dealer[0:2+j])
        dealer_score = dealer_score + all_card_dealer2[1+j]
    elif dealer_score <= 16 and add == "n":
        while dealer_score <= 16:
            j+=1
            print("ディーラーがカードを引きます")
            print("ディーラーの手札：",all_card_dealer[0:2+j])
            dealer_score = dealer_score + all_card_dealer2[1+j]
    elif dealer_score > 16:
        print("ディーラーはカードを引きません")
    elif add == "n" and dealer_score >16:
        break


#手札の合計を表示
print("あなたの手札合計：",player_score)
print("ディーラーのの手札合計：",dealer_score)

#判定
if player_score == dealer_score:
    print("判定：引き分けです")
elif player_score > 21 and dealer_score > 21:
    print("判定：引き分けです")
elif player_score <= 21 and dealer_score > 21:
    print("判定：あなたの勝ちです")
elif player_score > 21 and dealer_score <= 21:
    print("判定：ディーラーの勝ちです")
elif player_score > dealer_score:
    print("判定：あなたの勝ちです")
else:
    print("判定：ディーラーの勝ちです")
        