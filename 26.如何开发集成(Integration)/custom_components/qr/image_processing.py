"""
Support for the demo image processing.
作为自定义组件，本程序放置在配置目录下
custom_components/qr/image_processing.py中
"""
import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.core import split_entity_id
from homeassistant.components.image_processing import (
    ImageProcessingEntity, CONF_SOURCE, CONF_ENTITY_ID, CONF_NAME)

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the demo image processing platform."""
    entities = []
    for camera in config[CONF_SOURCE]:
        entities.append(QrEntity(
            camera[CONF_ENTITY_ID], camera.get(CONF_NAME)
        ))

    add_entities(entities)

class QrEntity(ImageProcessingEntity):
    """QR image processing entity."""

    def __init__(self, camera_entity, name):
        """Initialize QR image processing entity."""
        super().__init__()

        self._camera = camera_entity
        if name:
            self._name = name
        else:
            self._name = "QR {0}".format(
                split_entity_id(camera_entity)[1])
        self._state = None

    @property
    def camera_entity(self):
        """Return camera entity id from process pictures."""
        return self._camera

    @property
    def state(self):
        """Return the state of the entity."""
        return self._state

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    def process_image(self, image):
        """Process image."""
        import io
        from pyzbar import pyzbar
        from PIL import Image

        stream = io.BytesIO(image)
        img = Image.open(stream)

        barcodes = pyzbar.decode(img)
        if barcodes:
            self._state = barcodes[0].data.decode("utf-8")
        else:
            self._state = None
