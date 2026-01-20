from homeassistant.helpers.entity import Entity
from pymodbus.client import ModbusSerialClient
from .const import *

class ModbusSensor(Entity):
    def __init__(self, config):
        self._port = config[CONF_PORT]
        self._baud = config[CONF_BAUDRATE]
        self._timeout = config[CONF_TIMEOUT]
        self._scan = config[CONF_SCAN_RATE]
        self._state = None

        self.client = ModbusSerialClient(
            method="rtu",
            port=self._port,
            baudrate=self._baud,
            timeout=self._timeout
        )

    @property
    def name(self):
        return "DG Voltage"

    def update(self):
        self.client.connect()
        rr = self.client.read_holding_registers(16384, 1, slave=1)
        if not rr.isError():
            self._state = rr.registers[0] * 0.01
        self.client.close()

    @property
    def state(self):
        return self._state
