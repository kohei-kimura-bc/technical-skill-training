# ループが終わった後にループが終了しましたと出力する
for _ in range(100):
    print(_)
    # 強制終了する場合は、elseは処理されない
    # if _ == 10:
    #     break

else:
    print("ループが終了しました")
