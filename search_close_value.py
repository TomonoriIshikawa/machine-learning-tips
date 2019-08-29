# リスト要素と対象値の差分を計算し最小値のインデックスを取得
idx = np.abs(np.asarray(list) - num).argmin()
return list[idx]