# coding: utf-8
from numpy.random import randint
from numpy.random import choice
words='''
麥當勞
摩斯
私房麵
餐研社
自助餐
左撇子
金鰭
敏忠
米塔
就是棒
八角
學生餐
多果
里克
加賀
八方
蘭亭
樂山
甘泉
吃自己
凡提斯
便利店'''
phrase = words.split("\n")
n = randint(3,5) 

for i in range(n):
    k = randint(2,3) 
    egg = choice(phrase,k)
    ham = " ".join(egg)
    print(ham)
