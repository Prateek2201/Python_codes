Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> id(num)
1819108592
>>> name='prateek'
>>> id(name)
6319616
>>> a=10
>>> b=a
>>> id(a)
1819108672
>>> id(b)
1819108672
>>> b
10
>>> a
10
>>> id(10)
1819108672
>>> k=10
>>> id(k)
1819108672
>>> a=9
>>> id(a)
1819108656
>>> id(b)
1819108672
>>> k=a
>>> id(k)
1819108656
>>> b=8
>>> id(b)
1819108640
>>> id(10)
1819108672
>>> PI=3.14
>>> PI
3.14
>>> PI=3.15
>>> type(PI)
<class 'float'>
>>> 
