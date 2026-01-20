import os
import voluptuous as vol
from homeassistant import config_entries
from .const import *

USB_PORTS = [
    "/dev/ttyUSB0",
    "/dev/ttyUSB1",
    "/dev/ttyS0"
]

DEVICE_TYPES = {
    "dg_controller": "DG Controller",
    "energy_meter": "Energy Meter",
    "custom": "Custom Modbus Device"
}

BAUDRATES = [1200, 2400, 4800, 9600, 19200, 38400]

class ModbusTTLConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=f"Modbus {user_input[CONF_PORT]}",
                data=user_input
            )

        schema = vol.Schema({
            vol.Required(CONF_PORT): vol.In(USB_PORTS),
            vol.Required(CONF_DEVICE_TYPE, default="dg_controller"): vol.In(DEVICE_TYPES),
            vol.Required(CONF_BAUDRATE, default=9600): vol.In(BAUDRATES),
            vol.Required(CONF_TIMEOUT, default=2): vol.Coerce(int),
            vol.Required(CONF_SCAN_RATE, default=10): vol.Coerce(int),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors
        )
