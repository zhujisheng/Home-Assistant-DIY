"""Platform for sensor integration."""

from homeassistant.const import TEMP_CELSIUS
from homeassistant.components.sensor import SensorEntity


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up entry."""

    name = config_entry.data.get('name')
    value = config_entry.data.get('value')
    async_add_entities([ExampleSensor(name, value)])


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
