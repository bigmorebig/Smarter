# coding=utf-8
import random,re,os

#随机选取一个机器人
def rand_robot(content):
    id_group = re.findall("'id':\ '(\w+)'",str(content))
    return random.choice(id_group)

#随机选取知识库id
def rand_knowledge_id(content):
    id_group = re.findall("'id':\ (\d+)",str(content))
    return random.choice(id_group)

#返回不同类型下的云内容id
def culture_content_id(content,type):
    b = re.split('},{', str(content))
    for i in range(len(b)):
        if re.findall("'type':\ (\d)", b[i])[0] == str(type):
            return re.findall("'contentId':\ '(\w+)'", b[i])[0]
        else: return True

#随机选取一个机器人,返回主要机器人列表
def rand_robot_main(content):
    id_group = re.findall("'isMainAi':\ (\d+)",str(content))
    return random.choice(id_group) == 0

#查看主要机器人列表，判断是否为主要机器人
def rand_robot_onemain(list):
    return random.choice(list) == 0

#随机选择n个值
def rand_group_key(start,end):
    return random.randrange(start,end)

#随机选择一个值
def rand_one_key(key):
    return random.choice(key)

#列表为空返回true
def space_null(list):
    return list == []

#随机取n个值
def rand_many_key(n):
    string = '那是不是越低级的程序越难学，越高级的程序越简单？表面上来说，是的，但是，在非常高的抽象计算中，高级的Python程序设计也是非常难学的，所以，高级程序语言不等于简单'
    return ''.join(random.sample(string,n))

#随机提取频道id
def rand_channel_id(content):
    id_list = []
    finnal_list = []
    channel_id_group = re.findall("'contentUrl':\ '(.+?)',\ 'id':\ '(\w+)'",str(content))
    for i in range(len(channel_id_group)):
        id_list.append(re.findall("'id':\ '(\w+)'",str(channel_id_group[i])))
    for n in range(len(id_list)):
        if id_list[n]:
            finnal_list.append(id_list[n])
    return random.choice(finnal_list)[0]

#随机提取作者id
def rand_auther_id(content):
    id_list = []
    finnal_list = []
    channel_id_group = re.findall("'authorName':\ '(\w+)',\ 'id':\ '(\w+)'",str(content))
    for i in range(len(channel_id_group)):
        id_list.append(re.findall("'id':\ '(\w+)'",str(channel_id_group[i])))
    for n in range(len(id_list)):
        if id_list[n]:
            finnal_list.append(id_list[n])
    return random.choice(finnal_list)[0]

#随机选取地址
def rand_addr(content):
    id_group = re.findall("'addr':\ (.+?)",str(content))
    return random.choice(id_group) == 0

#随机选取area_id
def rand_area_id(content):
    id_group = re.findall("'uid':\ (\w+)",str(content))
    return random.choice(id_group) == 0

#随机选取频道类型id
def rand_channel_type_id(content):
    id_group = re.findall("'channelTypeId':\ (\d+)",str(content))
    return random.choice(id_group)

#随机选取频道标题
def rand_channel_title(content):
    id_group = re.findall("'title':\ '(.+?)'",str(content))
    return random.choice(id_group)

#取一个随机数字
def rand_num(num):
    return random.randint(1,num)

print(os.environ['password'])