# Project-forge-a-signature-to-pretend-that-you-are-Satoshi
ECDSA未检查签名邮件时，伪造合法签名使得你可以被认为是Satoshi

椭圆曲线数字签名算法
-
简单来说，与DSA本质上区别不大，在原DSA生成 r r r的地方引入了椭圆曲线以及一些其他参数的变化

公私钥的生成

私钥

    随机取一个在 ( 1 ， n − 1 ) 区间上的整数da作为私钥
    
    这里的n是选取椭圆曲线上的order，也就是椭圆曲线加密方程的模数，之后提到的n都是这个

公钥

    Q = da ∗ G ，其中Q是公钥，也就是说这里公钥是通过私钥生成的，而G是椭圆曲线上的基点。
    
    注意这个等式的乘法不是普通的乘法，是椭圆曲线加密中的乘法

**数字签名sign**

    生成一个临时密钥k 

    计算 P = k ∗ G其中P是椭圆曲线上的一个点

    取P点的x坐标， r ≡ x (mod n) 

    使用SHA1函数计算message的哈希值，使用H(m)表示，注意这个哈希值需要转换为数值型

    s ≡ k^(-1)∗ (H(m)+dA∗r)(mod n) 

而(r,s)即为sign算法的输出结果

代码运行指导
-
关于Attack_process文件是进行攻击的具体实行，进行签名伪造，伪造自己的身份为Satoshi
而testing文件则是用于签名伪造结果的验证，检测攻击是否成功，其运行结果的检测截图位于下方
而ECDSA.py文件则是一个通用的ECC椭圆曲线加密的模型代码


测试运行结果截图
-
![图片](https://user-images.githubusercontent.com/107350922/181413797-6448dca0-d553-42ae-8bcf-c36b13721a8c.png)
