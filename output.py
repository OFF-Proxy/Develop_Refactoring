def output(input_string, horison,vertical):
    if not (5 <= len(input_string) <= 10):
        raise ValueError("文字列は5文字以上10文字以下である必要があります。")
    
    if not input_string.isalpha():
        raise ValueError("文字列にはアルファベット(a～z, A～Z)のみ使用できます。")
    
    result = (input_string * horison + '\n') * vertical
    return result.strip()
print(output("testcode",3,4))