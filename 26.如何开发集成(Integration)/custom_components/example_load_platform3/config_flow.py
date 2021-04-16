"""Config flow for Example Load Platform integration -3"""
import logging
import voluptuous as vol

from homeassistant import config_entries

DOMAIN = 'example_load_platform3'

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example Load Platform integration -3."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is None:     # 用户还未输入
            DATA_SCHEMA = vol.Schema(
                {vol.Required('name'): str,
                vol.Optional('value', default=26.66): float}
                )
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )
        else:     # 用户已经输入
            try:
                return self.async_create_entry(title="Load Platform Example3", data=user_input)
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
