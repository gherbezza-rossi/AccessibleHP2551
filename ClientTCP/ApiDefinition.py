class ApiDefinition:
    def __init__(self, marker, name, size, op=1.0):
        self.marker = marker
        self.name = name
        self.size = size
        self.operation = op


# Define API definitions
api_defs = [
    ApiDefinition('0x01', "Internal Temperature", 2, 0.1),
    ApiDefinition('0x02', "External Temperature", 2, 0.1),
    ApiDefinition('0x03', "Dew Point", 2),
    ApiDefinition('0x04', "Wind Chill", 2),
    ApiDefinition('0x05', "Heat Index", 2),
    ApiDefinition('0x06', "Internal Humidity", 1),
    ApiDefinition('0x07', "External Humidity", 1),
    ApiDefinition('0x08', "Absolute Pressure", 2),
    ApiDefinition('0x09', "Relative Pressure", 2),
    ApiDefinition('0x0A', "Wind Direction", 2),
    ApiDefinition('0x0B', "Wind Speed", 2),
    ApiDefinition('0x0E', "Rain Rate", 2),
    ApiDefinition('0x0F', "Rain Hour", 2),
    ApiDefinition('0x10', "Rain Day", 2),
    ApiDefinition('0x11', "Rain Week", 2),
    ApiDefinition('0x12', "Rain Month", 4),
    ApiDefinition('0x13', "Rain Year", 4),
    ApiDefinition('0x14', "Rain Total", 4),
    ApiDefinition('0x15', "Light", 4),
    ApiDefinition('0x16', "UV", 2),
    ApiDefinition('0x17', "UV Index", 1),
    ApiDefinition('0x19', "Maximum Wind Daily", 2),
    ApiDefinition('0x1A', "TEMP1", 2, 0.1),
    ApiDefinition('0x22', "HUMI1", 1),
    ApiDefinition('0x2A', "PM25_CH1", 12),
    ApiDefinition('0x2B', "SOILTEMP1", 2),
    ApiDefinition('0x2C', "SOILMOISTURE1", 1),
    ApiDefinition('0x2D', "SOILTEMP2", 2),
    ApiDefinition('0x2E', "SOILMOISTURE2", 1),
    ApiDefinition('0x4D', "PM25_24HAVG1", 2),
    ApiDefinition('0x58', "LEAK_CH1", 1),
    ApiDefinition('0x60', "Lightning", 1)
]

# Create a dictionary from the list of ApiDefinition objects
API_DEFINITIONS = {api_def.marker: api_def for api_def in api_defs}
