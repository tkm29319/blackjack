import random
#カードのシャッフル
card_num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_type = ["♧", "♢", "♡", "♤"]
all_card = [ a + b for a in card_type for b in card_num] 
random.shuffle(all_card)
#手札の表示
print("あなたの手札：",all_card[0:2])
print("ディーラーの手札：",all_card[2:4])
    
#手札の計算
i=0
while i < 52:
    if "A" in all_card[i]:
        all_card[i]=1
        i+=1
    elif "2" in all_card[i]: 
        all_card[i]=2
        i+=1
    elif "3" in all_card[i]:
        all_card[i]=3
        i+=1
    elif "4" in all_card[i]:
        all_card[i]=4
        i+=1
    elif "5" in all_card[i]:
        all_card[i]=5
        i+=1
    elif "6" in all_card[i]:
        all_card[i]=6
        i+=1
    elif "7" in all_card[i]:
        all_card[i]=7
        i+=1
    elif "8" in all_card[i]:
        all_card[i]=8
        i+=1
    elif "9" in all_card[i]:
        all_card[i]=9
        i+=1
    elif "10" in all_card[i]:
        all_card[i]=10
        i+=1
    elif "J" or "Q" or "K" in all_card[i]:
        all_card[i]=10
        i+=1
    else:
        print("error")

print("あなたの手札合計：",all_card[0] + all_card[1])
print("ディーラーのの手札合計：",all_card[2] + all_card[3])
print("カードを追加で引きますか？：y or n")
        
