p = int(input('p= '))
q = int(input('q= '))
print(f'n = {p*q}')
e = int(input('e= '))

n = p * q
o = (p - 1) * (q - 1)


def exgcd(a, b):  # 擴展歐幾里德
    if b == 0:
        x = 1
        y = 0
        return x, y
    else:
        x1, y1 = exgcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return x, y


def inverse(a, b):
    x, y = exgcd(a, b)
    return (x + b) % b


d = inverse(e, o)
print(f'd = {d}')

txt = input('plain text= ')


def en_num(t):  # translate data to int
    if (t == ' '):
        return ord(t) - 6
    return ord(t) - 65


if (len(txt) % 2):  # 不滿兩個字元的區塊補空白
    txt += ' '


def txt_num_list(txt):
    data = [en_num(txt[i]) * 100 + en_num(txt[i + 1])
            for i in range(0, len(txt), 2)]
    return data


M = txt_num_list(txt)
print('M = ', end='')
for i in range(len(M)):  # 轉換成數字的資料
    print('%04d' % M[i], end=' ')

print('')


def num_encrypt(M, e, n):
    data = [pow(M[i], e, n) for i in range(len(M))]
    return data


C = num_encrypt(M, e, n)
print('C = ', end='')
for i in range(len(C)):  # 加密後的資料
    print(C[i], end=' ')
print('')


def decrypt(c, d, n):  # 用d解密
    return [pow(c[i], d, n) for i in range(len(c))]


print('')
print('After decoding :', end='')
af = decrypt(C, d, n)
for i in range(len(af)):  # 解密後的資料
    print(af[i], end=' ')
