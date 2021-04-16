"""Platform for sensor integration."""
import voluptuous as vol

from homeassistant.const import TEMP_CELSIUS
from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required("name"): str,
    vol.Optional("value", default=24.5): float,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""

    if config:
        name = config.get("name")
        value = config.get("value")

    add_entities([ExampleSensor(name, value)])


class ExampleSensor(SensorEntity):
    """Representation of a sensor."""

    def __init__(self, name, value):
        """Initialize the sensor."""
        self._state = None
        self._name = name
        self._value = value

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    def update(self):
        """Fetch new state data for the sensor.
        """
        self._state = self._value
