#本文件用于检测攻击是否成功
a = 2
b = 2
p = 17
m = 'hello'
m_1="world"
G = [5, 1]
n = 19
k=2
d = 5
P = Multiply(d, G)#计算公钥

print("1.测试 sign and vrfy algorithm：")
print("\n")
r,s=Ecdsa_Sign(m,n,G,d,k)
print("签名:",r,s)
print("验证结果：")
Ecdsa_Verify(m,n,G,r,s,P)


print("2.由于k被敌手获取导致密钥泄露：")
print("\n")
if (d == k_Leaking(r,n,k,s,m)):
    print("验证成功")

print("3.k的多次使用导致主密钥泄露：")
print("\n")
r_1,s_1=Ecdsa_Sign(m_1,n,G,d,k)
r_2,s_2=Ecdsa_Sign(m,n,G,7,k)
if (d == k_Reuse(r,s,m,r_1,s_1,m_1,n)):
    print("验证成功")

print("4. 使用相同k，可以成功互相计算密钥：")
print("\n")
print("验证结果为：")
Use_the_Same_k(s_1,m_1,s_2,m,r,5,7,n)

print("5. 检验r和-s是否为有效签名：")
print("\n")
print("测试结果为：")
Ecdsa_Verify(m,n,G,r,-s,P)

print("6. 是否可以成功伪装为Satoshi:")
print("\n")
print("伪装是否成功：")
Pretend(r,s,n,G,P)

print("7. Schnorr_Sign签名、ecdsa签名使用相同的d，k，导致密钥泄露：")
print("\n")
r3,s3=Schnorr_Sign(m,n,G,d,k)
d2=Schnorr_and_ECDSA(r,s,r3,s3,m,n)
print("破解是否成功：")
print(d == d2)
