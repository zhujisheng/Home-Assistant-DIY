#include "esphome.h"

#ifdef ESP32
#include "AudioOutputI2S.h"
#else
#include "AudioOutputI2SNoDAC.h"
#endif
#include "AudioFileSourceHTTPStream.h"
#include "AudioGeneratorMP3.h"


class ESPAudioComponent : public Component, public CustomAPIDevice, public BinarySensor {
  private:
    bool tryClosing = false;
    const char * toPlay = nullptr;
    AudioGeneratorMP3 *mp3;
    AudioFileSourceHTTPStream *file = nullptr;
#ifdef ESP32
    AudioOutputI2S *out;
#else
    AudioOutputI2SNoDAC *out;
#endif

  public:
    void setup() override {
#ifdef ESP32
      out = new AudioOutputI2S(0,1);
#else
      out = new AudioOutputI2SNoDAC();
#endif
      mp3 = new AudioGeneratorMP3();
      file = new AudioFileSourceHTTPStream();

      register_service(&ESPAudioComponent::on_play_media, "play_media", {"url"});
      //register_service(&ESPAudioComponent::on_stop_media, "stop_media");

      publish_state(false);
    }

    void loop() override
    {
      if (mp3->isRunning())
      {
        if (!mp3->loop() || tryClosing)
        {
          ESP_LOGD("custom", "Closing");
          mp3->stop();
          publish_state(false);
          tryClosing = false;
        }
      }
      else if(tryClosing)
      {
        ESP_LOGD("custom", "Try close, but already stopped");
        tryClosing = false;
      }
      else if(toPlay)
      {
        ESP_LOGD("custom", "Openning %s", toPlay);
        if(file->open(toPlay))
        {
          if ( mp3->begin(file, out) )
            publish_state(true);
          else
            ESP_LOGD("custom", "Begin play error");
        }
        else
          ESP_LOGD("custom", "Open file error");
        toPlay = nullptr;
      }
      else
      {
        delay(500);
      }

      yield();
    }

    void on_stop_media() {
      ESP_LOGD("custom", "Stopping media");
      tryClosing = true;
    }

    void on_play_media(std::string url) {
      ESP_LOGD("custom", "Starting to play media");
//      if (mp3->isRunning())
//        mp3->stop();
      toPlay = url.c_str();
    }
};