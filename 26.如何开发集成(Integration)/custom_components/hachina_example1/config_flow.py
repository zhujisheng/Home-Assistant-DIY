"""Config flow for HAChina Example1."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import async_generate_entity_id

from .const import DOMAIN, CONF_VALUE, DEFAULT_VALUE   # pylint:disable=unused-import

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hachina Example1."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is None:     # 用户还未输入
            DATA_SCHEMA = vol.Schema(
                {vol.Required(CONF_NAME): str,
                vol.Required(CONF_VALUE, default=DEFAULT_VALUE): str}
                )
            return self.async_show_form(
                step_id="user", data_schema=DATA_SCHEMA, errors=errors
            )
        else:     # 用户已经输入
            try:
                user_input["entity_id"] = async_generate_entity_id(DOMAIN+".{}", user_input[CONF_NAME], hass=self.hass)
                return self.async_create_entry(title=f"HAChina Example1:{user_input[CONF_NAME]}", data=user_input)
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

