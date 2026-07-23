f = open('./resource/it_news.txt', 'r', encoding='utf-8')

with open('./resource/context1.txt', 'w', encoding='utf-8') as f1:
    f1.write('I love python\n')

with open('./resource/context1.txt', 'a', encoding='utf-8') as f2:
    f2.write('I love java\n')