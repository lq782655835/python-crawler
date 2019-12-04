
# Python

## Python Basic Data Struct

1. String: '12'
1. List: [1, 2]
    * list(obj) 将对象强制转成list，比如 list(range(5))
    * list.append(obj) 在列表尾追加 obj
    * list.insert(index,obj) index索引处插入 obj
    * list.pop(obj=list[-1]) 移除列表中的元素(默认最后一个)
    * list.remove(obj) 移除obj匹配的第一个对象
1. Dict: {'a': 1, 'b': 2}
    * keys()
    * values()
    * items()
1. Tuple: (2, 3) 括号常可以省略
1. Set: {1, 2}

## Python Web Frame

Django 是一个重量级的框架,Flask是一个轻量型的框架;

Django是基于中间件的一个大型框架。框架本身的内容相当丰富，基础部分：模版引擎、ORM、表单、路由分发这些标配，还有不少的中间件：登陆、后台管理，这些还是官方中间件。

Flask 本身相当于一个内核，其他几乎所有的功能都要用到扩展（邮件扩展Flask-Mail，用户认证Flask-Login，数据库Flask-SQLAlchemy），都需要用第三方的扩展来实现。

## Python2 与Pyton3区别

### [python2](https://docs.python.org/2/library/urllib.htmls)和[python3](https://docs.python.org/3/library/urllib.request.html)中的urllib

在Python3中包urllib2归入了urllib中，所以要导入urllib.request，并且要把urllib2替换成urllib.request

``` python
# python2
import urllib2

url = 'http://www.jianshu.com/trending/weekly?page={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
request = urllib2.Request(url=url, headers=headers)
html = urllib2.urlopen(request)
print html.read()

# python3
import urllib.request

url = 'http://www.jianshu.com/trending/weekly?page={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
request = urllib.request.Request(url=url, headers=headers)
# urllib.request.urlopen(url,data,timeout) :第一个参数url，第二个参数是访问url要传送的数据，第三个参数是设置超时的时间
html= urllib.request.urlopen(request)
print(html.read())
```

## Python Crawler Frame

* [pyspider](http://docs.pyspider.org/en/latest/Quickstart/), example: https://cuiqingcai.com/2652.html

国内网速经常pip下载超时失败，可转为国内的镜像：

``` bash
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/ pyspider

# 如果同时安装了2.x和3.x python，3需要按照如下安装包
sudo python3 -m pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/ pyspider
```

* 阿里云 mirrors.aliyun.com/pypi/simple…
* 中国科技大学 pypi.mirrors.ustc.edu.cn/simple/
* 豆瓣(douban) pypi.douban.com/simple/
* 清华大学 pypi.tuna.tsinghua.edu.cn/simple/
* 中国科学技术大学 pypi.mirrors.ustc.edu.cn/simple/

> python2路径： /Users/xxx/Library/Python/2.7/lib/python/site-packages/
> python3路径：/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/bin
