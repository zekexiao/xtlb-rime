# xtlb-rime

小兔两笔 Rime 版本

## 日志
- 2019/12/28
	* update: x 学 -> 想

- 2019/9/9
	* update: d、j、m、z的首字现在为：d 的、j 就、m 们、z 在
	* fix:z 字母上的无用代码
- 2019/7/5
	* init: 初始版本

## 使用

 下载这个 Repo，解压后放置 Rime 文件夹下
 >
    【中州韻】 /usr/share/rime-data/
    【小狼毫】 "安裝目錄\data"
    【鼠鬚管】 "/Library/Input Methods/Squirrel.app/Contents/SharedSupport/"
    
 输入法设定内选择“小兔两笔”即可。

### Linux
```bash
git clone https://github.com/alluLinger/xtlb-rime.git
cd xtlb-rime
sudo ln -s xtlb.dict.yaml /usr/share/rime-data/xtlb.dict.yaml
sudo ln -s xtlb.schema.yaml /usr/share/rime-data/xtlb.schema.yaml
```
直接对源文件软链接，就无需每次修改进入rime目录。


## 说明

码表来自：[小兔两笔输入法](http://xtlb.ys168.com/)

配置文件参考：[超强两笔RIME平台版](http://fds8866.ys168.com/)
