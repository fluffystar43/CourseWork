from bs4 import BeautifulSoup as bs
import codecs

# https://javarush.ru/groups/posts/2560-vvedenie-v-java-fx
doc = bs(codecs.open('article.html', encoding='utf-8', mode='r').read(), 'html.parser')

# Извлечение данных из статьи
title = doc.select('h1.post-head__title')[0].decode_contents().strip()
author = doc.select('div.user-short-info-card__name')[0].decode_contents().strip()
date = doc.select('span.post-meta-panel__value')[0].decode_contents().strip()
city = doc.select('div.user-short-info-card__location')[0].decode_contents().strip()
views = doc.select('span.post-meta-panel__value')[1].decode_contents().strip()

# Вывод на экран
print('Название статьи:', title)
print('Автор статьи:', author)
print('Дата опубликования статьи:', date)
print('Город пользователя:', city)
print('Количество просмотров:', views)

# Извлечение данных о комментариях
comments = []
for node in doc.select('div.comment-wrap'):
    author = node.select('a.user')[0].decode_contents().strip()
    text = node.select('div.view-text')[0].decode_contents().strip()        
    comments.append({'text': text, 'author': author})
    
# Вывод информации по комментариям
print('Комментариев в статье: ', len(comments))
print('Самый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])

# Самый активный комментатор
commentators = {}
for comment in comments:
    if comment['author'] in commentators:
        commentators[comment['author']] += 1
    else:
        commentators[comment['author']] = 1
most_active = max(commentators, key=commentators.get)
print('Самый активный:', most_active, ', комментариев:', commentators[most_active])