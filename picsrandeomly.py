import random
import vk
import time
import json

file = open('./config_pics.json')
config = json.load(file)

session = vk.Session(access_token=config['token_vk']) # Авторизация Вк через токен
vk_api = vk.API(session)

last_post_id = 0      # ИД последнего поста в групе
rand_post_url = []    # переменная для 
owner_id = 0

def read_group ():                                            # ИД Групы в вк
    how_lines = len(config['group_ids'])
    id_group = config['group_ids'] [random.randint(0,how_lines-1)]
    print('id group in vk: ', id_group)
    return id_group

def offset_rand (offset ):              #отдельная функция для рандома
    offset = random.randint(3000,offset)
    return offset

def first_post (owner_id): 
    wall_posts = vk_api.wall.get(owner_id = owner_id, offset = 1, count = 1, v = 5.81)   # считывание последнего поста или пред последнего если есть закреплённый
    for post in wall_posts['items']:
        last_post_id = post['id']
        return last_post_id

def fing_post(owner_id,last_post_id):                                         # поиск поста зарандомленого поста по ид
    offset = offset_rand(last_post_id)
    wall_posts = vk_api.wall.get(owner_id= owner_id, offset = offset, count = 100, v = 5.81)
    exist = "#your_pile_of_music@the_pile" #isluchenie
    time.sleep(1)
    print("****", offset)
    #print(wall_posts)
    if wall_posts['items'] != []:
        #print ("True")
        for post in wall_posts['items']:
            if post['text'] != exist:
                offset+=1 
                if "attachments" in post:
                    for attachments in post ['attachments']:
                        if attachments ['type'] == 'photo':
                            for photo in attachments ['photo'] ['sizes']:
                                if photo ['type'] == 'z' :
                                    rand_post_url.append (photo ['url']  + '\n')
    else : fing_post(owner_id,last_post_id)               
    return rand_post_url

def start ():
    owner_id = read_group()
    time.sleep(1)
    last_post_id = first_post (owner_id)
    fing_post(owner_id,last_post_id)
    url_pics = rand_post_url[random.randint(0,len(rand_post_url)-1)]
    print('this link find in vk: ', url_pics)
    return url_pics

#print(start())    