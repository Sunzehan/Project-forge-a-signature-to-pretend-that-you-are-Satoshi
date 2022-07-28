import math
import random

#定义基本运算

    #判断互素
def Relatively_Prime(a, b):
    while a != 0:
        a, b = b % a, a
    return b

    #求最大公因子
def Gcd(a, m):
    if Relatively_Prime(a, m) != 1 and Relatively_Prime(a, m) != -1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m

    #椭圆曲线点的加法
def Add(m, n):
    if (m == 0):
        return n
    if (n == 0):
        return m
    he = []
    if (m != n):
        if (Relatively_Prime(m[0] - n[0], p) != 1 and Relatively_Prime(m[0] - n[0], p) != -1):
            return 0
        else:
            k = ((m[1] - n[1]) * Gcd(m[0] - n[0], p)) % p
    else:
        k = ((3 * (m[0] ** 2) + a) * Gcd(2 * m[1], p)) % p
    x = (k ** 2 - m[0] - n[0]) % p
    y = (k * (m[0] - x) - m[1]) % p
    he.append(x)
    he.append(y)
    return he

    #定义椭圆曲线点的数乘
def Multiply(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = Add(t, l)
        n = n - 1
    return t

#1. ECDSA——sign
def Ecdsa_Sign(m, n, G, d,k):
    e = hash(m)
    R = Multiply(k, G)
    r = R[0] % n
    s = (Gcd(k, n) * (e + d * r)) % n
    return r, s

#2. ECDSA——vrfy
def Ecdsa_Verify(m, n, G, r, s, P):
    e = hash(m)
    w = Gcd(s, n)
    v1 = (e * w) % n
    v2 = (r * w) % n
    w = Add(Multiply(v1, G), Multiply(v2, P))
    if (w == 0):
        print('false')
        return False
    else:
        if (w[0] % n == r):
            print('true')
            return True
        else:
            print('false')
            return False

#3. 泄露k导致密钥泄露
def k_Leaking(r,n,k,s,m):
    r_reverse=Gcd(r,n)
    e=hash(m)
    d=r_reverse * (k*s-e)%n
    return d

#4. 重用k导致密钥泄露
def k_Reuse(r1,s1,m1,r2,s2,m2,n):
    e1=hash(m1)
    e2=hash(m2)
    d=((s1 * e2 - s2 * e1) * Gcd((s2 * r1 - s1 * r1), n)) % n
    return d

#5. 使用相同k，可互相计算密钥
def Use_the_Same_k(s1,m1,s2,m2,r,d1,d2,n):
    e1=hash(m1)
    e2=hash(m2)
    d2_1 = ((s2 * e1 - s1 * e2 + s2 * r * d1) * Gcd(s1 * r, n)) % n
    d1_1 = ((s1 * e2 - s2 * e1 + s1 * r * d2) * Gcd(s2 * r, n)) % n
    if(d2==d2_1 and d1_1==d1):
        print("密钥合法计算成功！")
        return 1
    else:
        print("密钥非法计算错误！")
        return 0

#6.不验证m的验证算法
def Verify_without_m(e, n, G, r, s, P):
    w = Gcd(s, n)
    v1 = (e * w) % n
    v2 = (r * w) % n
    w = Add(Multiply(v1, G), Multiply(v2, P))
    if (w == 0):
        print('false')
        return False
    else:
        if (w[0] % n == r):
            print('true')
            return True
        else:
            print('false')
            return False

#7.伪装攻击者身份，被认定为Satoshi
def Pretend(r, s, n, G, P):
    u = random.randrange(1, n - 1)
    v = random.randrange(1, n - 1)
    r1 = Add(Multiply(u, G), Multiply(v, P))[0]
    e1 = (r1 * u * Gcd(v, n)) % n
    s1 = (r1 * Gcd(v, n)) % n
    Verify_without_m(e1, n, G, r1, s1, P)

#8.Schnorr_Sign签名
def Schnorr_Sign(m, n, G, d,k):
    R = Multiply(k, G)
    e = hash(str(R[0]) + m)
    s = (k + e * d) % n
    return R, s

#9.Schnorr_Sign签名、ecdsa签名使用相同的d，k，导致密钥泄露
def Schnorr_and_ECDSA(r1, s1, R, s2, m, n):
    e1 = int(hash(m))
    e2 = int(hash(str(R[0]) + m))
    d = ((s1 * s2 - e1) * Gcd((s1 * e2 + r1), n)) % n
    return d
