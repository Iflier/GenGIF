
# 说明 </br>

本脚本是一个从视频文件中提取固定帧间隔的工具，借助[imageio](http://imageio.readthedocs.io/en/latest/userapi.html)第三方工具包生成一个.gif文件</br>

## 各依赖包版本说明 </br>

Python: `3.5.2`</br>
Opencv: `3.4.1`</br>
imageio: `2.3.1`</br>

## 用法说明 </br>

CMD: >> python -i 20</br>
表示从视频中提取的帧间隔为每20帧保留一个</br>
-i (或者 --interval)的取值范围为range(5, 21)</br>


# License
GPL V2.0
