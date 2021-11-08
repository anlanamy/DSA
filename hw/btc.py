'''
1：上面validate和find_nonce的复杂度分别是多少？它们是什么关系？分别属于NP还是P？
2: 如果想把“Alice send .1 coins to Kate”改成“Alice send 100 coins to Kate”，计算一个新nonce来保持“块哈希”值不变，算法复杂度是多少？
'''

import hashlib
def bthash(unicode):
    return hashlib.sha256(unicode.encode("utf8")).hexdigest()

hash_result = bthash("""戏剧中叔父克劳迪谋害了丹麦国王--哈姆雷特的父亲，篡了王位，并娶了国王的遗孀葛簇特；
王子哈姆雷特因此为父王之死向叔父复仇。剧本细致入微地刻画了伪装的、真实的疯癫 —— 
从悲痛欲绝到假装愤怒 —— 探索了背叛、复仇、乱伦、堕落等主题""")
print("hash of《哈姆雷特介绍》：{}".format(hash_result))

difficulty_bits = 4
difficulty = 2 ** difficulty_bits
target = 2 ** (256 - difficulty_bits)
print("Difficulty is {}({} bits),\nless than:{:>64x}".format(
    difficulty, difficulty_bits, target))
#
# 核心问题，求解nonce，满足条件： 
#     Curr_hash = hash(transactions + nonce + Prev_hash) < target
#
def validate(transactions, nonce):
    block = transactions + [nonce] + ["前一个块哈希:13b1b06...76d3d"]
    hash_result = bthash(str(block))
    print("nonce {:>3}:{}".format(nonce, hash_result))
    if int(hash_result, 16) < target:
        return True
    else :
        return False
    
def find_nonce(transactions):               #挖矿过程
    ntries = 256
    for nonce in range(ntries):             #随机数
        if validate(transactions, nonce):
            print("A new block mined with nonce {}".format(nonce))
            return nonce
    else:
        print("Failed in ntries:{}".format(ntries))
        return None

if __name__ == "__main__":
    transactions = ["Alice sends .5 coins to Bob",
             "Bob sends 2 coins to John",
             "Alice send .1 coins to Kate",
             "John send 1 coins to Miselle",
             "Miselle send 2 coins to Alice",
               "矿工(光头强)被奖励一个coin"]
    nonce = find_nonce(transactions)
    if nonce:
        print("光头强成功开采出了一个区块，获得一个比特币奖励。")

