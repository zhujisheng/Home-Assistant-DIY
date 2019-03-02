### 本项目对应于《HomeAssistant智能家居实战篇》系列视频内容中的文档。
[网易云课堂地址](https://study.163.com/course/introduction.htm?courseId=1006189053&share=2&shareId=400000000624093)

## 视频目录
- 入门准备篇
	- 硬件环境准备——安装树莓派
	- 系统环境设置——树莓派基础配置
	- 安装Samba和JupyterNotebook
	- 基于树莓派安装HomeAssistant
	- HomeAssistant自启动如何配置
- 组件接入基础篇
	- 让设备发声——朗读文字
	- 让设备看到——使用手机摄像头做监控
	- 将消息发送给你的邮箱
	- 接入硬件产品——小米多功能网关
	- 接入自定义组件-和风天气
- 操作进阶篇
	- 配置目录、hass命令与升级
	- 操作界面与Lovelace
	- 设置地理位置与界面语言
	- 实体显示属性自定义
	- 手机访问HA
	- StatesUI界面优化——分组与分页
- 补充篇章
	- Linux下的常用命令
	- Linux下的文本编辑
	- YAML文件格式
	- Python虚拟环境
- 公网访问篇
	- 申请Amazon免费云主机
	- ssh隧道构建
	- frp隧道构建
	- 免费为HA配上域名与HTTPS网站证书
	- nginx代理
- 设备位置追踪篇
	- 设备定位准备知识与Ping检测
	- nmap网络扫描、黑客、小米wifi路由器
	- 蓝牙音箱与蓝牙设备扫描
	- 使用iCloud随时定位苹果手机
- 自动化篇
	- 编写简单脚本——执行系列动作
	- 编写简单自动化规则
	- 模板——嵌入配置文件中的程序
	- 事件与事件消息接收
	- 前端输入组件+packages配置
	- 语音+音乐+灯光闹钟
- 设备接入篇(1)
	- 太阳、月亮、季节和潮汐
	- 天气与预报——yr、DarkSky、……
	- 红外遥控——博联RM系列产品
	- 红外遥控——小米万能遥控器
	- 文件夹监测——FolderWatcher
- 各种摄像头接入篇
	- 支持MJPEG的摄像头与图片抓取
	- RTSP协议摄像头与ffmpeg
	- ONVIF协议摄像头
	- 有线树莓派CSI与USB摄像头
	- 小米的大方摄像头
	- 天气预报与交通状况图——另类摄像头
- 人脸识别篇
	- DLib配置与pip安装
	- 本地DLib人脸探测
	- 本地DLib人脸识别
	- 微软人脸特征检测
	- 微软人脸识别与验证
	- Facebox-在docker中运行人脸识别
- 设备接入篇（2）
	- YeeLight智能灯
	- 云端的自动化——IFTTT(1)
	- 云端的自动化——IFTTT(2)
	- 系统性能监控——SystemMonitor
	- 以不同的音色播报文字——百度tts
- 使用苹果设备语音控制篇
	- 通过Homekit与苹果Siri连接(1)
	- 通过Homekit与苹果Siri连接(2)
	- 捷径与HA的接口调用
	- 在HA中完成语音文字处理——chrome语音控制
	- 苹果设备语音控制全自由定制
- 数据记录篇
	- 历史数据基础概念
	- 数据组件的配置、mysql数据库及其它
- AppDaemon与DashBoard
	- 安装、配置与初步运行
	- DashBoard配置(1)
	- DashBoard配置(2)
	- 制作App——一个最简单的样例
	- 制作App——应用callback
- Node-RED篇
	- Node-RED安装与初体验
	- Node-RED配置
	- HomeAssistant节点(1)
	- HomeAssistant节点(2)
	- 一些样例：闹钟、自动湿度控制、门铃
- 树莓派GPIO口设备连接篇
	- 直连树莓派的LED(1)——NodeRED接入/HA中rpi_gpio_pwm组件
	- 直连树莓派的LED(2)——HA 中的shell_command/binary_sensor.command_line/light.template
	- 直连树莓派的温湿度传感器
- MQTT篇
	- 服务器安装与最简单的智能灯
	- 主题格式、状态反馈、调试……
	- QoS、retain、last_will、自动配置……
- DIY智能硬件ESP8266篇
	- ESP8266——固件烧录与连接
	- ESP8266上的MicroPython使用
	- 连接ESP8266的DHT温湿度传感器
	- ESP8266完成各种功能
	- 典型样例讲解：光照传感器与智能灯
	- ESPHome——不编程，集成ESP8266
- 成为HomeAssistant开发者
	- 组件的工作原理
	- 程序样例：二维码识别组件
	- Python程序员的成长与代码规范
	- 把你的代码贡献给组织
- IOS App的使用
	- IOS App——连接、定位与通知消息
	- iBeacon定位
	- 多媒体通知与静态文件Web服务
- Lovelace定制界面
	- 理解Lovelace页面的结构
	- Lovelace中的卡片
- 抓取Internet信息作为传感器
	- 即时股票行情——使用sensor.rest
	- 各种网站页面元素——sensor.scrape组件
- 自己动手做一个智能音箱
	- DIY智能音箱（1）——整体架构、硬件安装
	- DIY智能音箱（2）——snowboy、speech_recognition
	- DIY智能音箱（3）——完成主程序架构
	- DIY智能音箱（4）——与HomeAssistant交互
	- 完善（1）——更好的音色、更多的指令
	- 完善（2）——准确回答任意问题
	- 完善（3）——自定义唤醒词与敏感度
	- 完善（4）——使用微软语音识别服务
	- 最后一课——积木构建智慧空间
- 加餐
	- 使用TensorFlow进行物体识别

## 我们的追求
1. 真实<br>
照着操作肯定行，过程不做省略

2. 不断更新<br>
随HomeAssistant更新而更新，新版本的新操作方式、内容及时更新到视频与参考文档中

3. 快节奏<br>
重点展现实践操作过程。如果不是仅追求效果的话，需要自己补充对应的知识。实践——思考——学习

4. 精心选择的实践与操作内容<br>
全面、避免不成熟的技术方向、避免陷入超出知识体系范畴之外的坑中

5. 便宜、实用<br>
几百元的硬件投入，就可以实践几乎所有的视频内容
