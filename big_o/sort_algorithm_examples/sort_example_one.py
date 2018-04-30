# Example one - Bubble Sort
# Time Complexity - Avg: O(n^2) Worst: O(n^2)
# Memory - O(1)
# Stability - Stable


def bubble_sort(arr):
    change = True # 変更し続けるかをchangeによって変える
    while change:
        change = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                # arr[i]の値を前に持ってくる(arr[i+1]のポジション)。そうすることで、次のarr[i]として使うことができる為、arr[i+2]と比較することができる。
                arr[i], arr[i+1] = arr[i+1], arr[i]
                change = True

    return arr


arr = [9,94,5,3,2]
print("Result >> ", bubble_sort(arr))

### プロセス ###
# 配列　＝　[5,4,3,2]
# まずwhile文でTrueの場合処理を実行し続ける。
# for文で配列を一つづつループするように設定
# if文を用いてindex[0](i=0)の時、[0]と[1]を比較する。
# [0]>[1]の場合、配列の順番を[[1],[0]]に置き換える。
# for文で配列の位置の置き換えを行ったので、change=Trueにする。
# 現在の配列の状態 = [4,5,3,2]
# for文でi=1の時、index[1]=[5]
# if文でindex[1]>index[2]時、(5,3)
# 置き換えで[4,3,5,2]となる。
# 繰り返し。。。
