import random

#>>>>>点数を初期化
score = 0
#ここに出題する文字列を入力しよう
questionlist = 'マイクロソフト', "Microsoft", "Python"

#>>ここを編集<< コンソールに文字列を表示
print("アナグラムを表示するから答えを入力してね")
#>>ここを編集<< コンソールに文字列を表示
print(str(len(questionlist)) + "問 出題するよ")

#>>ここを編集<< questionlistに文字列がある間繰り返し
for qtext in questionlist:
#出題する文字列を並べ替え
    squestion = ''.join(random.sample(qtext, len(qtext)))

#>>ここを編集<< コンソールにsquestionを表示
    print(squestion)
#>>ここを編集<< コンソールから回答の文字列を入力
    sanswer = input("答えは? = ")

#>>ここを編集<< 正解と回答が同じかどうか判断
    if qtext == sanswer:
#>>ここを編集<< コンソールに正解という文字列を表示
        print("正解!!")
#>>>>>点数を加算
        score += 1
#>>ここを編集<< 上記の判断が一致しない場合
    else:
#>>ここを編集<< コンソールにハズレの文字列を表示
        print("ハズレ～ 答えは " + qtext + " だよ")
#>>>>>コンソールに点数を表示
print(str(score) + "問 正解でした")
