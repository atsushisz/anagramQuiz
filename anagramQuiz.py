import random

#ここに出題する文字を入力しよう
questionlist = 'マイクロソフト', "Microsoft", "Python", "舞子高校"

#>>ここを編集<< コンソールに文字列を表示
xxxxx("アナグラムを表示するから答えを入力してね")
#>>ここを編集<< コンソールに文字列を表示
xxxxx(str(len(questionlist)) + "問 出題するよ")

#>>ここを編集<< questionlistに文字列がある間繰り返し
xxx qtext in questionlist:
#出題する文字列を並べ替え
    squestion = ''.join(random.sample(qtext, len(qtext)))

#>>ここを編集<< コンソールにsquestionを表示
    xxxxx(squestion)
#>>ここを編集<< コンソールから回答の文字列を入力
    sanswer = xxxxx("答えは? = ")

#>>ここを編集<< 正解と回答が同じかどうか判断
    xx qtext == sanswer:
#>>ここを編集<< コンソールに正解という文字列を表示
        xxxxx("正解!!")
#>>ここを編集<< 上記の判断が一致しない場合
    xxxx:
#>>ここを編集<< コンソールにハズレの文字列を表示
        xxxxx("ハズレ～ 答えは " + qtext + " だよ")
