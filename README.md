# xtlb-rime

小兔两笔 Rime 版本

## 说明

码表来自：[小兔两笔输入法](http://xtlb.ys168.com/)

配置文件参考：[超强两笔RIME平台版](http://fds8866.ys168.com/)

## 日志
- 2020/2/11
	* reborn: 脚本生成dict.yaml，词库与原版一致

- 2019/7/5
	* init: 初始版本

## 使用

 下载这个 Repo，解压后放置 Rime 文件夹下
 >
    【中州韻】 /usr/share/rime-data/
    【小狼毫】 "安裝目錄\data"
    【鼠鬚管】 "/Library/Input Methods/Squirrel.app/Contents/SharedSupport/"
    
 输入法设定内选择“小兔两笔”即可。

### Linux fcitx-rime
```bash
git clone https://github.com/alluLinger/xtlb-rime.git
cd xtlb-rime
sudo ln -s xtlb.dict.yaml ~/.config/fcitx/rime/xtlb.dict.yaml
sudo ln -s xtlb.schema.yaml ~/.config/fcitx/rime/xtlb.schema.yaml
```
直接对源文件软链接，就无需每次修改进入rime目录。

### iOS iRime
1.AppStore 下载 iRime
2.在`设置->一般->键盘`内将 iRime 加上
3.打开电脑快传，将两个 .yaml 文件上传到根目录
4.下载并修改 `default.yaml` 文件，在 `schema_list`中添加 `- schema: xtlb`
5.iRime 在点击部署，然后选择小兔两笔方案

