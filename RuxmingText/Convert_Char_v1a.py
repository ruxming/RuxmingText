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


def sample(idx=0):
    ret = ""
    initList = []
    x = "i am request,\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82"
    initList.append(x)
    x1 = b"\xE6\x88\x91\xE6\x98\xAF\xE8\xAF\xB7\xE6\xB1\x82"
    initList.append(x1)
    d = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1=82abcdef"
    initList.append(d)
    f = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1"
    initList.append(f)
    a = '\xE6\x88\x91' #
    initList.append(a)
    b = '=E3=80=90'
    initList.append(b)
    c = '开'
    initList.append(c)
    return initList[idx]
