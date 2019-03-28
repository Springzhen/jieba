#encoding:utf-8
import requests,json,sys,time
requests.adapters.DEFAULT_RETRIES = 5

def entrs(data):
    data = json.dumps(data)
    return data

def get_web_data(url, content):
    r = requests.post(url,content)
    if r.status_code==200:
        return r.text
    else:
        return u'请求失败'

def wordsegment(inputdata):
    url = 'http://192.168.10.87:8760/segment'
    content = {'input':inputdata}
    outdata = get_web_data(url, content)
    outlist = json.loads(outdata)
    return outlist

if __name__ == '__main__':
    inputdata = u'''我是中国人郭亚强110程佳颖艾滋病t恶性肿瘤及胃部恶性肿瘤10123
    '''
    data = wordsegment(inputdata)
    print ('data',str(data))