# Usage

**AssetDeduplication.py**

Here's a text file called "demo.txt" that reads:

```html
demo.com
xxx.com
yyy.com
```

How to use AssetDeduplication.py ?

Example:

```shell
python .\AssetDeduplication.py -l .\demo.txt -p "8888,9999" -P "http,https"
```

Result:

```html
http://xxx.com:8888
http://xxx.com:9999
http://yyy.com:8888
http://yyy.com:9999
http://demo.com:8888
http://demo.com:9999
https://xxx.com:8888
https://xxx.com:9999
https://yyy.com:8888
https://yyy.com:9999
https://demo.com:8888
https://demo.com:9999
```

