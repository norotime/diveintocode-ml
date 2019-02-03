# -*- coding: utf-8 -*-
import numpy as np

def train_test_split(X, y, train_size=0.8,):
    """
    学習用データを分割する。

    Parameters
    ----------
    X : 次の形のndarray, shape (n_samples, n_features)
      学習データ
    y : 次の形のndarray, shape (n_samples, )
      正解値
    train_size : float (0<train_size<1)
      何割をtrainとするか指定

    Returns
    ----------
    X_train : 次の形のndarray, shape (n_samples, n_features)
      学習データ
    X_test : 次の形のndarray, shape (n_samples, n_features)
      検証データ
    y_train : 次の形のndarray, shape (n_samples, )
      学習データの正解値
    y_test : 次の形のndarray, shape (n_samples, )
      検証データの正解値
    """    
    # 1. Xにyを列方向に結合
    y = np.reshape(y, [len(y), 1])

    Xy = np.hstack((X, y))

    # 2.Xyをランダムにシャッフル
    np.random.shuffle(Xy)

    # 3. 列方向にX, yへ垂直分割
    X, y = np.vsplit(Xy, [Xy.shape[1]-1])

    # 4. 引数の比率でトレーニングとテストへ水平分割
    X_train, X_test = np.vsplit(X, [int(len(X)*train_size)])
    y_train, y_test = np.vsplit(y, [int(len(y)*train_size)])
    
    # 5. 戻り値
    return X_train, X_test, y_train, y_test