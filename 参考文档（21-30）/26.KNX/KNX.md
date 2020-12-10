
# (1) 家庭总线部署方案与KNX

1. 家庭总线部署的基本概念

   优点：稳定性、灵活性

2. KNX总线物理线路

   <img src=images/knx_bus.png width=80%>

3. 标准化

   <img src=images/knx_logo.png width=30%>

4. 大型工程与ETS软件

   <img src=images/knx_project.png width=60%>

5. 物理地址与组地址

   <img src=images/knx_address.png width=50%>

6. 非TP1接入

   <img src=images/knx_access.png width=70%>

# (2) 使用IP Router接入HomeAssistant

1. IPRouter的作用

   <img src=images/knx_iproute.png width=80%>
 
2. IPRouter硬件连接与配置

   <img src=images/knx_iproute2.png width=50%>

3. Routing与Tunneling

   <img src=images/knx_routing_tunneling.png width=80%>

4. 在HomeAssistant中配置KNX

5. 获得目标组地址

6. 在HomeAssistant中配置KNX设备

### 【参考】

- KNX组件配置说明

  https://www.home-assistant.io/integrations/knx/

- 配置

    ```yaml
    knx:
    #  routing:
    #    local_ip: '192.168.3.241'
      tunneling:
        host: '192.168.3.232'
        port: 3671
        local_ip: '192.168.3.241'
      fire_event: true
      fire_event_filter: ["*/*/*"]
      light:
        - name: 客厅灯带
          address: '1/5/233'
          state_address: '1/5/233'
        - name: 客厅水滴灯
          address: '1/6/65'
          state_address: '1/6/65'
        - name: 客厅吊灯
          address: '1/6/81'
          state_address: '1/6/81'
          brightness_address: '1/6/81'
    ```


# (3) 使用ncn5120模块-USB连接模式

1. 整体连接结构

   <img src=images/knx_usblink.png width=80%>

2. 硬件连接（USB口连接模式）

   <img src=images/knx_usblink2.png width=60%>

3. 安装knxd

```sh
# 安装必要的基础库
sudo apt-get install git-core build-essential

# 获得源代码
git clone https://github.com/knxd/knxd.git

# 编译
cd knxd
git checkout master（有些环境下此命令可能要改成git checkout deb）
dpkg-buildpackage -b -uc
# 如果在安装过程中，如果提示缺失的库，就安装此库

# 安装
cd ..
sudo dpkg -i knxd_*.deb knxd-tools_*.deb
```

4. KNXD配置

   - KNXD启动参数（编辑`/etc/knxd.conf`文件）

     USB连接模式

     ```
     -e 0.0.1 -E 0.0.2:8 -D -R -T -S -b ncn5120:/dev/ttyUSB0:19200
     -D：自动发现
     -R：IP routing接口
     -T：IP tunneling接口
     ```

    - 将用户knxd，加入组dialout

      `sudo adduser knxd dialout`

5. 配置HomeAssistant与运行

### 【参考】

- KNXD软件

  https://github.com/knxd/knxd

- SCSGate

  https://translate.google.com/translate?hl=en&sl=it&tl=en&u=http%3A%2F%2Fguidopic.altervista.org%2Feibscsgt%2Finterface.html

  https://www.home-assistant.io/components/scsgate/

# (4) 使用ncn5120模块-WIFI连接模式

1. 整体连接结构

   <img src=images/knx_wifilink.png width=80%>

2. 硬件连接(WIFI连接模式)

   <img src=images/knx_wifilink2.png width=30%>
   <img src=images/knx_wifilink3.png width=30%>
   <img src=images/knx_wifilink4.png width=30%>

3. NodeMCU 32S配置

4. knxd配置修改

   TCP连接模式

   `-e 0.0.1 -E 0.0.2:8 -D -R -T -S -b ncn5120tcp:192.168.31.248:5120`

5. 操作演示

# (5) 使用ncn5120模块-在hassio中快速配置

<img src=images/knx_link.png width=80%>

1. 硬件连接

   参考前面两个视频的内容，使用usb或者wifi连接方式都可以

2. 增加add-on仓库

   `https://github.com/da-anda/hass-io-addons`

   `https://github.com/zhujisheng/hass-io-addons`

3. 配置

    ```ini
    address: 0.0.1
    client_address: '0.0.2:10'
    interface: tpuart
    device: /dev/ttyACM0
    usb_filters: ''
    custom_config: |-
      [main]
      addr = 0.0.1
      client-addrs = 0.0.2:10
      connections = server,A.tcp,interface
      logfile = /dev/stdout

      [A.tcp]
      server = knxd_tcp

      [server]
      server = ets_router
      tunnel = tunnel
      router = router
      discover = true
      name = knxd

      [interface]
      driver = ncn5120
      ip-address = 192.168.1.3
      dest-port = 5120
      #device = /dev/ttyUSB0
      #baudrate = 19200
    ```

4. 在HomeAssistant中配置KNX设备

    ```yaml
    knx:
      tunneling:
        host: '127.0.0.1'
        port: 3671
        local_ip: '127.0.0.1'
      fire_event: true
      fire_event_filter: ["*/*/*"]
      light:
        - name: 卧室射灯
          address: '1/6/9'
          state_address: '1/6/9'
        - name: 客厅灯带
          address: '1/5/233'
          state_address: '1/5/233'
    ```
