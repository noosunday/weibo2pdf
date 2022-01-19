import requests
import datetime
import csv
import codecs


from pyquery import PyQuery as pq

#basic_info#

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'}

basic_url='https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&type=uid&value=1022058374&containerid=1076031022058374'

def get_since_id(since_id):
    #global since_id
    final_url = basic_url + '&since_id=' + str(since_id)
    since_id = requests.get(final_url, headers=headers).json().get('data').get('cardlistInfo').get('since_id')
    print(final_url,since_id)
    return since_id

std_transfer = '%a %b %d %H:%M:%S %z %Y'

def get_page(since_id):
    final_url = basic_url + '&since_id=' + str(since_id)

    results = requests.get(final_url, headers=headers).json().get('data').get('cards')

    for result in results:
        mblog = result.get('mblog')
        weibos = {}
        std_create_time = datetime.datetime.strptime(mblog.get('created_at'), std_transfer)
        new_time = datetime.datetime.strftime(std_create_time, '%Y{y}%m{m}%d{d} %H:%M:%S %A').format(y='年', m='月',
                                                                                                      d='日')

        weibos['created_at'] = new_time
        weibos['text'] = pq(mblog.get('text'))

        pics = mblog.get('pics')
        picture_id = ''
        if pics:
            for pic in pics:
                picture_url = pic.get('large').get('url')  # 得到原图地址
                picture_id += '<img src="' + picture_url + '" class="imagew"/> '
        weibos['pics'] = picture_id

        yield weibos
# since_id = '4686826197485196'
# get_page(since_id)
def main():
    since_id = ''
    for i in range(1, 3):
        print('page_{}'.format(i))

        weibos = get_page(since_id)
        f = codecs.open('data/weibo.csv', 'a+', encoding='utf-8-sig')
        writer = csv.writer(f)
        for weibo in weibos:
            a=weibo['created_at'],weibo['text'],weibo['pics']
            writer.writerow(a)
        f.close()

        since_id = get_since_id(since_id)
        print('since_id=',since_id)


if __name__=='__main__':
    main()