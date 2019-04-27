#include "driver/i2s.h"

const uint16_t BUFFER_SIZE = 512;
const uint16_t SAMPLE_RATE = 16000;
i2s_config_t i2s_config = {
  .mode = (i2s_mode_t)(I2S_MODE_MASTER | I2S_MODE_RX | I2S_MODE_PDM),
  .sample_rate = SAMPLE_RATE,
  .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT,
  .channel_format = I2S_CHANNEL_FMT_ONLY_RIGHT,
  .communication_format = I2S_COMM_FORMAT_PCM,
  .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1,
  .dma_buf_count = 32,
  .dma_buf_len = 32
};
i2s_pin_config_t pin_config = {
  .bck_io_num = -1,
  .ws_io_num = GPIO_NUM_19,
  .data_out_num = -1,
  .data_in_num = GPIO_NUM_22
};

void setup() {
  Serial.begin(115200);
  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &pin_config);
}

void loop() {
  int16_t buf[BUFFER_SIZE];
  unsigned int read_num;

  i2s_read(I2S_NUM_0, buf, BUFFER_SIZE*2, &read_num, portMAX_DELAY);

  for (int i = 0; i < BUFFER_SIZE; i++) {
    //buf[i] = (buf[i]-966)*64;
    Serial.println(buf[i]);
  }
}

