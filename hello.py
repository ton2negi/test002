#
# 2019/07/27 作成
# 　～はじめてのPython～　いや～ん。照れちゃう///
#
print("hello world")
print("　～日本語も試してみるよ～")
print("途中で改行を入れてみるテスト。\n\
\tさてどう表示されることやら\n\
\t\tなるほど。こうなるのね。\n")

msg = """\
やっほー。
ダブルクォーテーションを３つ連続すると、
改行がそのまま反映されるらしいよ。
⇒preと同じだね！\
"""

print(msg)

# 「r」を付与することで「\」をエスケープ文字として判定しなくなる。便利！
print(r"インストール先は c:\code\python\bin です")

num = 18
print("My age is " + str(num))

# なんかスッゲー違和感。。。
str = "Flower"
print(str[1:4])
print(str[:3])
print(str[3:])
print(str[:])


# ステップ「3」が全く腑に落ちない。。。
#str = "京都府京都市左京区吉田本町"
str = "1234567890abc"
print(str)
print(str[1:12])
print(str[1:12:2])
print(str[1:12:3])


print(" *** powed by Python ***")
