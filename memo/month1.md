# モデルの評価

## モデルの評価指標一覧
The scoring parameter: defining model evaluation rules¶
https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

## ROC AUC

### 予測スコアからROC AUCを算出する
sklearn.metrics.roc_auc_score
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html

## CV

### クロスバリデーションの実行と結果の算出
sklearn.model_selection.cross_validate
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html

## GridSearch

### Scikit-learn系のモデルのハイパーパラメータ取得
sklearn.svm.SVC
https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.get_params


現場体験談

- オリジナルデータを使ってEDAした方が傾向をつかみやすい
- 平均と分散は必ず見る
- 主成分分析をして可視化させることをする、このデータからこういう特徴がありますね、としてから相手に説明をするために算出する。特徴が100-200個ある場合は、気をつける。
- 時系列データは、人の行動には偏りがある。例えば、金融系で言えば人の心理等でやすいものに偏るよる傾向がある、給与でも低い年収が多かったりして、偏っている。
    - これを把握してから、対数変換して、データ解析がしやすいようにしていく
- サンプルデータ数は、40000件以上にする、列は、EDAして絞っていくことがある、レコード数は絞らない方が良い、できれば全件読み込ませたい
- 型を指定してインポートしないとハングしてしまうため、型指定はちゃんとする

- ハイパーパラメータチューニングは最終的に行う。
    - 基本的に絶対にCV 5-10までは絶対に試す
        - CV5とCV7とCV10を使い、その平均値を算出する