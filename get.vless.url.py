from bagbag import * 

db = Tools.MySQL("localhost")

urls = []
for i in db.Table("proxy_pool_proxies").Where("url", "like", 'vless%').Get():
    urls.append('forward=' + i['url'])

File("glider.conf").Append('\n' + '\n'.join(urls))