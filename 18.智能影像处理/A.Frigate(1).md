# Frigate(1)

## camera与image_processing集成

<img src="images/ha_camera.png" width="40%">

视频流保存/智能处理对硬件的要求比较特殊：
- 大容量硬盘
- 高性能计算

## Frigate是什么？

Frigate是带物体识别功能的本地NVR(Network Video Recorder)系统。

<img src="images/frigate.png" width="60%">


## 安装与配置

Frigate一般以docker容器的方式安装运行；也可以是HomeAssistant Supervisor下的Add-on

- 安装

    add-on仓库：`https://github.com/blakeblackshear/frigate-hass-addons`

    *如果你想以标准的docker容器方式安装运行frigate，参见：https://blakeblackshear.github.io/frigate/installation#docker*

- MQTT服务

- `frigate.yml`

    ```yaml
    # frigate.yml配置样例
    mqtt:
      host: 192.168.3.7
      user: pi
      password: hachina123
    cameras:
      my_camera1:
        record:
          enabled: True
        snapshots:
          enabled: True
        objects:
          track:
            - person
            - car
            - dog
        ffmpeg:
          inputs:
            - path: rtsp://admin:VEERAZ@192.168.3.216/
              roles:
                - detect
                - rtmp
                - clips
                - record
        detect:
          width: 1280
          height: 720
          fps: 5
    detectors:
      cpu1:
        type: cpu
    ```

    *详细的配置说明，请参见：[https://blakeblackshear.github.io/frigate/](https://blakeblackshear.github.io/frigate/)*
    
