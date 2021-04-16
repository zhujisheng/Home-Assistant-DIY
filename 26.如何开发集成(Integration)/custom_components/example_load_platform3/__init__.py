"""Example Load Platform integration -3."""
import voluptuous as vol

def setup(hass, config):
    """Your setup of the integrate."""

    return True


async def async_setup_entry(hass, config_entry):
    """Set up Load Platform from a config entry."""

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            config_entry, 'sensor'
        )
    )

    return True


async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""

    await hass.config_entries.async_forward_entry_unload(config_entry, 'sensor')

    return True
