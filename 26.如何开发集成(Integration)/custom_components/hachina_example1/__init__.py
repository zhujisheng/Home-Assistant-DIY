"""HAChina Example for Integration Basic"""
import asyncio

import logging
import voluptuous as vol

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import async_generate_entity_id

from .const import DOMAIN, CONF_VALUE, DEFAULT_VALUE

_LOGGER = logging.getLogger(__name__)


# 对configuration.yaml文件中该集成的配置格式要求
CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                # “name”在配置文件中是必须存在的（Required），否则报错，它的类型是字符串
                vol.Required(CONF_NAME): cv.string,
                # “value”在配置文件中可以没有（Optional），如果没有缺省值为“积木构建智慧空间！”，它的类型是字符串
                vol.Optional(CONF_VALUE, default=DEFAULT_VALUE): cv.string,
            }),
    },
    extra=vol.ALLOW_EXTRA)


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the hachina_example1 component."""

    # config[DOMAIN]: configuration.yaml中这个域的配置信息
    conf = config.get(DOMAIN)

    if conf:
        # 获得具体配置项信息
        name = conf.get(CONF_NAME)
        value = conf.get(CONF_VALUE)

        _LOGGER.info(f"Get the configuration from configuration.yaml: {CONF_NAME}={name}; {CONF_VALUE}={value}")

        # 根据配置内容设置属性值
        entity_id = async_generate_entity_id(DOMAIN+".{}", name, hass=hass)
        attr = {"icon": "mdi:home-assistant",
                "friendly_name": name
                }
        hass.states.async_set(entity_id, value, attributes=attr)

    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up hachina_example1 from a config entry."""
    name = entry.data[CONF_NAME]
    value = entry.data[CONF_VALUE]
    entity_id = entry.data["entity_id"]

    _LOGGER.info(f"Get the configuration from config entry: {CONF_NAME}={name};entity_id={entity_id};{CONF_VALUE}={value}")

    # 根据配置内容设置属性值
    attr = {"icon": "mdi:home-assistant",
            "friendly_name": name
            }
    hass.states.async_set(entity_id, value, attributes=attr)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""

    entity_id = entry.data["entity_id"]
    hass.states.async_remove(entity_id)

    return True
