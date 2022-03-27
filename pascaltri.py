"""
利用Python探究杨辉三角中一个性质的程序
Author FeletexGee
Version 0.2-20220326
基本上完成了i18n
"""
import sys,math
sys.setrecursionlimit(100000)#设置递归最大深度为10e5，防止错误.
"""
用组合数定义对将用到的组合数函数进行定义.实际上该算法效率较低.(挖坑)
"""
def com(a,b):
    if (a == b) or (a == 0):
        return 1
    elif a == 1:
        return b
    else:
        return math.factorial(b)/(math.factorial(b-a)*math.factorial(a))
line_term=int(input("> Enter line number of Pascal tri. required to be evaluated: "))#输入所需验证杨辉三角行数
if line_term<8:
    print("[Error]Invalid parameter:Line number should not less than 8!")#异常处理
    exit()
current_line=0
current_item=0
for current_line in range (8,line_term+1):#对行数进行迭代
    """
    下面根据行数的奇偶进行分类讨论.
    """
    if current_line % 2==0:
        item_term=(current_line//2)+1
    else:item_term=(current_line//2)+2
    for current_item in range (2,item_term):#对系数（项数）进行迭代
        a1=com(current_item-2,current_line-1)
        a2=com(current_item-1,current_line-1)
        a3=com(current_item,current_line-1)
        if (2*a2==a1+a3):#等差数列验证
            print("  Line",current_line,"Item",current_item-1,"to",current_item+1,":",a1," ",a2," ",a3)
print("> Evaluation completed.")#岩石的重量，令人安心