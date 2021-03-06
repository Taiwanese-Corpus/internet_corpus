from itertools import zip_longest

import yaml


夜市資料 = {
    '來源': (
        {'名': 'yukki',
            '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1436987021.A.521.html'},
        {'名': 'sunyen3m',
         '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1436987021.A.521.html'},
        {'名': '薛丞宏'}
    ),
    '資料': [
        ('今天生意好嗎!?', '今仔日生意干好!?', '今仔日生意敢好!?'),
        ('別講了!?看到國民黨就一肚子火', '賣貢這!?看丟顧面桶丟歸八肚火', '莫講這!?看著顧面桶就規腹肚火'),
        ('怎麼了!?', '西安抓!?', '是按怎!?'),
        ('你沒看新聞嗎!?就什麼國民黨那個老女人啊~要來我們這掃街拜票，今日都被他們搞得沒生意做!?',
         '你無看新聞嗎!?貢蝦咪顧面桶那個老查某啊~咩來溫這掃街拜票，今日攏呼他們搞得沒生意做!?',
         '你無看新聞嗎!?講啥物顧面桶那個老查某啊~欲來阮這掃街拜票，今仔日攏予𪜶舞到沒生意做!?'),
        ('阿伯!?這樣應該人更多才對啊!?', '阿伯!?這樣應該人更多才對啊!?', '阿伯!?按呢應該人較濟才著啊!?'),
        ('你台北人不懂啦!生意就已經難做了!還要來南部這邊亂!?要亂回去他們國民黨啦!今天都沒做到生意看到一群好像26過境的人在做秀，越想越氣...',
         '哩台北人哩無災啦!生意丟咧難做了!還要來南部這邊亂!?咩亂回去拎顧面桶亂啦!今仔日龍無做到生意看到一群好像26過境的人在做秀，越想越氣...',
         '你台北人你無知啦!生意就咧歹做矣!閣欲來南部這爿亂!?欲亂轉去𪜶顧面桶亂啦!今仔日攏無做到生意看到一群好像阿陸仔過境的人佇做秀，愈想愈氣…'),
        ('國民黨悲哀啊!被狗弄成這樣真正可憐啊!', '顧面桶悲哀啊!呼狗用成這樣真正可憐啊!', '顧面桶悲哀啊!予狗用做按呢真正可憐啊!'),
        ('今天前頭賣吃的才是可憐，人都進不來臉都很臭，我兒子看到情勢不對就先收早早回來，根本那個老女人是來亂的啊!!!',
         '今仔日頭前擺吃才是可憐人都進不來臉都很臭，溫兒子看到情勢不對就先收早早回來，根本那個老查某丟是來亂啊!!!',
         '今仔日頭前擺食的才是可憐人攏入袂來臉攏誠臭，阮後生看到情勢毋著就先收早早轉來，根本彼个老查某就是來亂啊!!!'),
        ('阿伯!她叫洪秀柱啦!', '阿伯!她叫洪秀柱啦!', '阿伯!伊叫洪秀柱啦!'),
        ('管她叫什麼!?反正那什麼柱的也不可能贏啦!?我不可能(投)給她，叫我投給國民黨想得美咧...',
         '管她叫蝦咪!?灰去蝦咪柱嘛無可能贏啦!?我無可能(當投)給她叫我投給顧面桶甲卡麥...',
         '管伊叫啥物!?橫直啥物柱嘛無可能贏啦!?我無可能(當投)予她叫我投予顧面桶食較䆀…'),
    ]
}


王嗆馬新聞資料 = {
    '來源': (
        {'名': '符芳碩',
            '網址': 'http://newtalk.tw/news/view/2015-09-10/64467'},
        {'名': '符芳碩',
            '網址': 'http://newtalk.tw/news/view/2015-09-10/64467'},
        {'名': '薛丞宏'}
    ),
    '資料': [
        ('我才不理他', '我咧採小伊', '我咧插潲伊'),
        ('我怎麼知道', '我奈ㄟ栽啊', '我哪會知影')
    ]
}

王嗆馬ptt資料 = [
    {
        '來源': (
            {'名': '薛丞宏'},
            {'名': 'gogohorse',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441866838.A.5E4.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('我才不理他', '哇勒彩小尹', '我咧插潲伊'),
        ]
    },
    {
        '來源': (
            {'名': '薛丞宏'},
            {'名': 'darling520',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441866838.A.5E4.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('我才不理他馬英九', '娃嘞擦洨液罵陰久', '我咧插潲伊馬英九'),
        ]
    },
    {
        '來源': (
            {'名': '薛丞宏'},
            {'名': 'linceass',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441866838.A.5E4.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('我才不理他勤', '挖勒菜洨伊勒', '我咧插潲伊咧'),
        ]
    },
]


民主政治還要殺人字詞 = {
    '種類': '字詞',
    '來源': (
        {'名': '自由時報',
         '網址': 'http://news.ltn.com.tw/news/politics/breakingnews/1440958'},
        {'名': '自由時報',
         '網址': 'http://news.ltn.com.tw/news/politics/breakingnews/1440958'},
        {'名': '薛丞宏'}
    ),
    '資料': [
        ('剛才', '塌嘟仔', '頭拄仔'),
    ]
}
民主政治還要殺人語句 = {
    '來源': (
        {'名': '自由時報',
         '網址': 'http://news.ltn.com.tw/news/politics/breakingnews/1440958'},
        {'名': '自由時報',
         '網址': 'http://news.ltn.com.tw/news/politics/breakingnews/1440958'},
        {'名': '薛丞宏'}
    ),
    '資料': [
        ('救人哦', '救郎哦', '救人哦')
    ]
}

台鐵退票收4成資料 = [
    {
        '來源': (
            {'名': 'IronWolf',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441944941.A.FF0.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('', '哇三小', ''),
        ]
    },
    {
        '來源': (
            {'名': 'darling520',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441944941.A.FF0.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('', '哇你老木哇', ''),
        ]
    },
    {
        '來源': (
            {'名': 'arcc',
             '網址': 'https://www.ptt.cc/bbs/Gossiping/M.1441944941.A.FF0.html'},
            {'名': '薛丞宏'}
        ),
        '資料': [
            ('', '夕賀', ''),
        ]
    },
]

你也懂台語字資料 = [
    {
        '來源': (
            {'名': 'Liz',
             '網址': 'http://liztaigi.blogspot.tw/2015/08/blog-post_31.html'},
            {'名': 'Liz',
             '網址': 'http://liztaigi.blogspot.tw/2015/08/blog-post_31.html'},
        ),
        '資料': [
            ('', '您真了不起，簡直就是聖人！', ('你真了不起，bē輸ná聖人leh！',
                                   'Lí tsin liáu-put-khí, bē-su ná sìng-jîn--leh!')),
            ('', '哩金料不key，美蘇納性臨咧！', ('你真了不起，bē輸ná聖人leh！',
                                     'Lí tsin liáu-put-khí, bē-su ná sìng-jîn--leh!')),
        ]
    },
]


# print(yaml.dump(夜市資料, default_flow_style=False, allow_unicode=True))
夜市輸出資料 = {
    '版權': '無版權',
    '種類': '語句',
    '語言腔口': '閩南語',
    '著作所在地': '臺灣',
    '著作年': '2015',
    '下層': [],
}
for 規組語句資料 in 夜市資料['資料']:
    這組資料 = []
    for 第幾層, (來源, 語句資料) in enumerate(zip_longest(夜市資料['來源'], 規組語句資料)):
        if 第幾層 == 0:
            新資料 = {
                '來源': 來源,
                '外語語言': '華語',
                '外語資料': 語句資料,
            }
        else:
            新資料 = {
                '來源': 來源,
                '文本資料': 語句資料,
            }
        這組資料.append(新資料)
    夜市輸出資料['下層'].append({'相關資料組':這組資料})

with open('柱柱姊掃街變成來亂的.yaml', 'w') as 檔案:
    yaml.dump(夜市輸出資料, 檔案, default_flow_style=False, allow_unicode=True)
