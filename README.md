# 佣兵战纪 1-1

没啥技术含量的挂机脚本。代码仅供参考，理论上调整炉石窗口位置生效，脚本即可正常执行。

### demo

[BV1ou411Z7KJ](https://www.bilibili.com/video/BV1ou411Z7KJ)

### 环境

良心云2C4G8M轻量服务器，[购买链接](https://curl.qcloud.com/8izQ1J4o) （推广一下）

python 3.7.9

所需依赖

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python pyautogui numpy
```

屏幕分辨率 1280*1024

```
SetWindowPos(hwnd, HWND_TOPMOST, 365, 292, 548, 439, SWP_SHOWWINDOW);
```



编写参考 https://nga.178.com/read.php?tid=11838545
