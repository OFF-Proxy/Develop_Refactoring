import random


def repeat_string(input_string, horison,vertical):
    # 文字列が5文字以上10文字以下であるかチェック
    """引数の文字列を指定した回数繰り返す

    Args:
        input_string (str): 繰り返す文字列
        horison (int): 横方向に繰り返す回数
        vertical (int): 縦方向に繰り返す回数

    Raises:
        ValueError: 文字列は5文字以上10文字以下である必要があります。
        ValueError: 文字列にはアルファベット(a～z, A～Z)のみ使用できます。

    Returns:
        _type_: _description_
    """
    if not (5 <= len(input_string) <= 10):
        raise ValueError("文字列は5文字以上10文字以下である必要があります。")
    
    # 文字列がアルファベットのみかチェック
    if not input_string.isalpha():
        raise ValueError("文字列にはアルファベット(a～z, A～Z)のみ使用できます。")
    
    # 文字列を横に最初の数値分、縦に次の数値分繰り返す
    result = (input_string * horison + '\n') * vertical
    return result.strip() #TODO:strip　末尾の改行を削除
print(repeat_string("testcode",random.randint(0,10),random.randint(0,10)))