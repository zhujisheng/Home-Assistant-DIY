本镜像文件为树莓派的tf卡镜像，内容是`hassio`系统（基于`hassos`），其中已经安装好了HomeAssistant以及一些常用的Add-on。

## 烧写

- 解压缩`xxxx-xx-xx-raspberrypi-hassos-hachina.zip`
- 使用烧写工具（例如`Etcher`）将img文件烧写到tf卡上

## 配置WIFI

- 在`boot`分区上建立`CONFIG`目录，在其中建立`network`目录，在其中建立`my-network`文件。
- `my-network`文件具体格式可参考下载的`CONFIG/network/my-network`文件。根据你的实际情况，修改其中的`my_ssid`和`my_password`。

## 配置ssh访问

- 在`boot`分区上建立`CONFIG`目录，在其中建立文件`authorized_keys`。
- `authorized_keys`文件可参考下载的`CONFIG/authorized_keys`，如果直接使用，在putty中通过配置下载的`hachina_image.ppk`文件进行访问（将putty的`connection`-`SSH`-`Auth`-`private key`配置为此文件）。
- 如果你要生成自己的访问密钥，参考：https://developers.home-assistant.io/docs/operating-system/debugging#generating-ssh-keys
- 访问端口为`22222`
- 使用`root`用户登录，登录后输入命令`login`

## 配置PulseAudio连接蓝牙音箱

- ssh登录到系统

- 蓝牙音箱连接，运行命令`bluetoothctl`

  ```
  scan on
  pair <your mac address>
  trust <your mac address>
  connect <your mac address>
  discoverable on
  pairable on
  default-agent 
  ```

- 在前端`集成`中添加`PulseAudio`，选择对应的蓝牙设备
- 也可以在`configuration.yaml`文件中配置

```yaml
# configuration.yaml样例
media_player:
  - platform: pulseaudio
    name: xxxxxx
    sink: alsa_output.0.iec958-stereo
```

其中，sink可以通过命令`docker exec homeassistant pactl list sinks short`查看