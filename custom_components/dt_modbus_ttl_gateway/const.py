DOMAIN = "dt_modbus_ttl_gateway"

# ---------- CONFIG KEYS ----------
CONF_PORT = "port"
CONF_DEVICE_TYPE = "device_type"
CONF_DEVICE_NAME = "device_name"
CONF_BAUDRATE = "baudrate"
CONF_TIMEOUT = "timeout"
CONF_SCAN_RATE = "scan_rate"

# ---------- DEVICE TYPES ----------
DEVICE_DG = "dg"
DEVICE_ENERGY = "energy"

DEVICE_TYPES = {
    DEVICE_DG: "DG Controller",
    DEVICE_ENERGY: "PEACEFAIR PZEM 016"
}

# ---------- DEFAULT VALUES ----------
DEFAULT_BAUDRATE = 9600
DEFAULT_TIMEOUT = 2
DEFAULT_SCAN_RATE = 10
DEFAULT_DEVICE_NAME = "Grid"

# ---------- SUPPORTED BAUDRATES ----------
BAUDRATES = [
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    115200
]

# ---------- PLATFORMS ----------
PLATFORMS = [
    "sensor",
    "switch"
]
