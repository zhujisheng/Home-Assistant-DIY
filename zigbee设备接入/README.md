
# (1) 架构介绍及硬件设备准备

## zigbee通讯协议

- 短距离通讯
- 低功耗
- 低带宽

## 架构

<img src=images/zigbee2mqtt.JPG width=90%>

- zigbee2mqtt官网：https://www.zigbee2mqtt.io/

## cc2531

  <img src=images/cc2531.jpg width=25%>

- zigbee2mqtt支持各种zigbee dangle(adapter)
- cc2531是最常见的zigbee芯片
- zigbee dangle需要烧写固件，不同的dangle烧写固件的方法是不同的

## 烧写cc2531 zigbee dangle

有各种烧写cc2531的方法，这儿选择一种只需要树莓派+连接器的方案。

1. 安装`wiringpi`

    `sudo apt-get install wiringpi`

2. 下载烧写程序和固件

    - 烧写程序(https://github.com/jmichault/flash_cc2531.git)

        `git clone https://github.com/jmichault/flash_cc2531.git`

    - 固件(https://github.com/Koenkk/Z-Stack-firmware/raw/master/coordinator/Z-Stack_Home_1.2/bin/default/CC2531_DEFAULT_20190608.zip)

        ```
        wget https://github.com/Koenkk/Z-Stack-firmware/raw/master/coordinator/Z-Stack_Home_1.2/bin/default/CC2531_DEFAULT_20190608.zip

        unzip CC2531_DEFAULT_20190608.zip
        ```

3. 硬件连接

    ```
    cc2531 dangle           树莓派
    pin 1 (GND)     -->    pin 39 (GND)
    pin 7 (reset)   -->    pin 35
    pin 3 (DC)      -->    pin 36
    pin 4 (DD)      -->    pin 38

    pin 2           -->    pin 1 或 pin 17 (3.3v电源)
    ```

    <img src=images/Raspberry-CC2531.jpg width=70%>

4. 烧写

- 查看芯片id

  `./cc_chipid -m 200`

- 备份

  `./cc_read save.hex -m 200`

- 擦除

  `./cc_erase -m 200`

- 烧写

  `./cc_write CC2531ZNP-Prod.hex  -m 200`

# (2) zigbee2mqtt安装与配置

## 安装add-on `Mosquitto broker`

- 采用缺省配置，不需要做任何修改
- 使用HomeAssistant的用户名和密码进行访问

## 在HomeAssistant中配置mqtt

- 在集成界面中完成

  注意：`启用发现`需要勾选

- 在`configuration.yaml`中完成

    ```yaml
    mqtt:
      broker: 127.0.0.1
      username: HomeAssistant的用户名
      password: HomeAssistant的密码
      discovery: true
    ```

## 安装与配置add-on `Zigbee2mqtt`

- 添加仓库`https://github.com/danielwelch/hassio-zigbee2mqtt`

- 仅需要修改配置中mqtt的用户名和密码，设置为HomeAssistant的用户名和密码

- 启动前，记得将zigbee dangle插入usb口

## zigbee设备接入

- 在`zigbee2mqtt`的web界面上点击`permit join`
- 重置zigbee设备
- 设备接入后，`Disable join`

## HomeAssistant中后续的配置

- 设置实体的隐藏、名称、图标
- 在自动化中进行配置

# (3) ZHA组件

## HomeAssistant中常用的几种连接zigbee设备的方式

- 设备厂商的网关（比如小米网关、Ikea的网关）
    + 通过HomeAssistant中的专用组件接入（比如[Xiaomi Aqara Gateway](https://www.home-assistant.io/integrations/xiaomi_aqara/)）
    + 仅支持厂家的zigbee设备
    + 可能需要通过隐秘的方法获得连接的key
- 支持Homekit的网关（比如小米多模网关）
    + 可通过[HomeKit Controller](https://www.home-assistant.io/integrations/homekit_controller/)组件接入
- zigbee2mqtt
    + 将zigbee协议转化成mqtt协议，通过mqtt组件接入HomeAssistant
    + 连接环节多，配置复杂
- deCONZ
    + zigbee网关硬件仅支持RaspBee或ConBee
    + 通过[deCONZ add-on](https://github.com/home-assistant/addons/tree/master/deconz)和[deCONZ组件](https://www.home-assistant.io/integrations/deconz/)接入
- ZHA
    + 直接通过HomeAssistant的[Zigbee Home Automation组件](https://www.home-assistant.io/integrations/zha/)接入
    + 无需安装额外的add-on或软件
    + 支持的硬件（zigbee网关和zigbee设备）比较广泛

    <img src=images/zha.png width=70%>

硬件兼容性

https://zigbee.blakadder.com/zha.html

## CC2531准备

- 参见前面的视频，进行烧写
- 插入HomeAssistant所在机器的USB口
- 重启HomeAssistant

## 配置ZHA

一般情况下，仅需要选择对应的网关硬件设备，其余的都能自动完成。

如果手动设置，参见：https://www.home-assistant.io/integrations/zha/#configuration---gui

## 添加zigbee设备

注：一些小米的zigbee设备，在添加过程中，需要不断按动按钮。

## 事件与自动化

注：小米开关，不会添加为二进制传感器，但按动后会生成事件。