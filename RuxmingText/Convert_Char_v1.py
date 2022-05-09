import binascii
DEBUG = False

def hexStr_to_str(hex_str):
    hex = hex_str.encode('utf-8')
    if(DEBUG):print("hex",hex)
    # hex = hex_str
    str_bin = binascii.unhexlify(hex)
    return str_bin.decode('utf-8')


def str_to_hexStr(string): # '开'
    str_bin = string.encode('utf-8')
    if(DEBUG):print("encode", type(str_bin), str_bin) #  <class 'bytes'> b'\xe5\xbc\x80'
    ret = binascii.hexlify(str_bin)
    if(DEBUG):print("hexlify", type(ret), ret)  # <class 'bytes'> b'e5bc80'
    ret = ret.decode('utf-8')
    if(DEBUG):print("hexStr", type(ret), ret)  # <class 'str'> e5bc80
    return ret  # e5bc80

def Obtain16Char(input, symb=r'=' ):
    ret = ""; to3 = ""; count=0
    idx = 0
    try:
        for ary in input:
            if(DEBUG):print(idx, "ary>", type(ary), ary, symb)
            if(ary == symb):
                ret += input[idx+1] + input[idx+2]
                if(DEBUG):print(len(input),"ret>", ret, input[idx+1])
            idx += 1
    except Exception as ex:
        print(ex)
    return ret.replace(symb,'')

def Validate16Char(input, symb=r'=' ):
    ret = ""; count=0
    idx = 0
    try:
        for ary in input:
            if(DEBUG):print(idx, "ary>", type(ary), ary, symb)
            if(ary == symb):
                count += 1
                if(DEBUG): print(len(input),"ret>", ret, input[idx+1])
                if(len(input)>(idx+1)):
                    if (len(input) > (idx +2)):
                        if( input[idx-3] == symb):
                            if(input[idx-6] == symb ):
                                if(count==3):
                                    ret += input[idx-5] + input[idx-4] + input[idx-2] + input[idx -1] + input[idx + 1] + input[idx + 2]
                                    count = 0
            idx += 1
    except Exception as ex:
        print(ex)
    return ret.replace(symb,'')

if __name__ == '__main__':
    x = "i am request,\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82"
    x1 = b"\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82"
    d = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1=82abcdef"
    f = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1"
    a = '\xE6\x88\x91' #
    b = '=E3=80=90'
    c = '开'
    print(str_to_hexStr(c)) # e5bc80
    print(hexStr_to_str("e38090"))

    a = a.replace(r'\x','')
    b = b.replace(r'=','')
    print(b)
    print(hexStr_to_str(b))

    e = Obtain16Char(d, r'=')
    print("Obtain16Char>", e)
    print(hexStr_to_str(e))

    f = Validate16Char(f, r'=')
    print("Validate16Char>", f)
    print(hexStr_to_str(f)) # 我是请

    x = Validate16Char(x.replace('\\',''),  r'x')  # Not work, æ x
    print("Validate16Char>", x)
    print(hexStr_to_str(x))

    x1 = b"\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82"
    aa = ''.join(['%02x' % b for b in x1])
    print(aa)  # e68891e698afe8afb7e6b182


    data = b'\x820\xb100\x03\xc3\xb4'
    print('type(data) = ', type(data))
    # type(data) =  <class 'bytes'>
    aa = ''.join(['%02x' % b for b in data])
    print(aa) # 8230b1303003c3b4
    lst = list(data)
    print(lst)
    print(type(lst[0]))
    # [130, 48, 177, 48, 48, 3, 195, 180]
    # <class 'int'>
    tmp = data.hex()
    print(type(tmp), tmp)
    # <class 'str'> 8230b1303003c3b4

    strr = '8230b1303003c3b4'
    num = bytes.fromhex(strr)
    print(type(num), num)
    # <class 'bytes'> b'\x820\xb100\x03\xc3\xb4'