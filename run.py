#!.\venv\Scripts\python3
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import psycopg2
from  psycopg2.extras import DictCursor
cdn = '''
    dbname='d7et8bul0cl1jj'
    host='ec2-54-221-215-228.compute-1.amazonaws.com'
    user='zvqlglufakjwgd'
    password='a4a95ee1c08805901d03182a3e7831267da09903cadf3d24ad49321a47ba52f0'
    port='5432'
'''
conn = psycopg2.connect(cdn)

vk_session = vk_api.VkApi(token="923f78afbe360da5c6c85651afc6928cde519831c60cb005496003c8d14281a7c4d2ed660a00618c77f66")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "185825170")
for event in longpoll.listen(): #Проверка действий
    if event.type == VkBotEventType.MESSAGE_NEW:  # последняя строчка
        # проверяем не пустое ли сообщение нам пришло
        if event.obj.text == 'start':
            if event.from_user:
                curs = conn.cursor()
                curs.execute("INSERT INTO heroes(name) VALUES(%s)", (event.obj.from_id,))
                conn.commit()
            if event.from_chat:
                curs = conn.cursor()
                curs.execute("INSERT INTO heroes(name) VALUES(%s)" ,(event.obj.from_id,))
                conn.commit()
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    random_id=get_random_id(),
                    message='Ждите блять, не работает еще'
                )
        if event.obj.text != '':
            # проверяем пришло сообщение от пользователя или нет
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Жди блять, не работает еще'
                )
            if event.from_chat:
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    random_id=get_random_id(),
                    message='Ждите блять, не работает еще'
                )