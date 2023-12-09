from example import sum_after,sum_before #←テストする関数をインポート


def test_sum():
    """マトリックスNo1 ←テストを行うマトリックスの番号
    10点より下の点数がある場合 ←テストの内容
    """
    assert sum_before() == 55 #←assertを使用して結果が正しいことを確認する

    assert sum_after() == 55