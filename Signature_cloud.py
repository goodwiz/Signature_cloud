#coding=utf8

# Author:WiZ
# 2018/04/25

import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

# 获取自己的用户信息，返回自己的属性字典
itchat.auto_login(True)

it = itchat.get_friends()
# print(it)
temp = 0

provi = []

# 事先建立文件用于存储签名
f = open('a.txt','w')

for i in it:
    # print(i.Province)
    provi.append(i.Province)
    # if i.Province == '辽宁':
    #     print('昵称:',i.NickName,'姓名:',i.RemarkName, 'Sex:', i.Sex, '签名:', i.Signature, '城市:',i.Province)
    # print('昵称:',i.NickName,'姓名:',i.RemarkName, 'Sex:', i.Sex, '签名:', i.Signature, '城市:',i.Province)
    f.write(i.Signature+' ')
    temp = temp + 1

# 输出好友的个数
print ('Myfriends number is :',temp-1)

f.close()

# 收集好友的来自的城市信息
# d1 =dict()
# isfirst = 0
# for i in provi:
#     if str(i) not in d1:
#         d1[str(i)] = 1
#     else:
#         d1[str(i)] = d1[str(i)] + 1
# for i in d1:
#     print(i,d1[i])
#     print(i)
# print(d1)

itchat.run(True)

