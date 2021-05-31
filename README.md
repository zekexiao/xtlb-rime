# xtlb-rime

小兔两笔 Rime 版本

## 说明

码表来自：[小兔两笔输入法](http://xtlb.ys168.com/)

配置文件参考：[超强两笔RIME平台版](http://fds8866.ys168.com/)

## 日志

- 2021/5/31
   * update: 更新词库到原版6.0，
   * add: 添加了一些自用词库到xtlb.ext，可在xtlb.dict.yaml中删除import_table
   * update: 更新了'/'和'\'在中文状态下的符号都是'、'

- 2020/2/11
	* update: 脚本生成dict.yaml，词库与原版一致

- 2019/7/5
	* init: 初始版本

## 使用

 下载这个 Repo，解压后放置 Rime 文件夹下
 >
    【中州韻-fcitx】 "~/.config/fcitx/rime/"
    【中州韻-ibus】 "~/.config/ibus/rime/"
    【小狼毫】 "%APPDATA%\Rime"
    【鼠鬚管】 "~/Library/Rime"
    
 输入法设定内选择“小兔两笔”即可。

### Linux fcitx-rime
```bash
git clone https://github.com/alluLinger/xtlb-rime.git
cd xtlb-rime
sudo ln -s $PWD/xtlb.dict.yaml ~/.config/fcitx/rime/xtlb.dict.yaml
sudo ln -s $PWD/xtlb.ext.dict.yaml ~/.config/fcitx/rime/xtlb.ext.dict.yaml
sudo ln -s $PWD/xtlb.schema.yaml ~/.config/fcitx/rime/xtlb.schema.yaml
```
直接对源文件软链接，就无需每次修改进入rime目录。

### iOS iRime
- AppStore 下载 iRime
- 在`设置->一般->键盘`内将 iRime 加上
- 打开iRime内的`电脑快传`，将两个 .yaml 文件上传到根目录
- 下载并修改 `default.yaml` 文件，在 `schema_list`中添加 `- schema: xtlb`
- iRime 在点击部署，然后选择小兔两笔方案

