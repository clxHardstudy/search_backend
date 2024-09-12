import configparser


config = configparser.ConfigParser()
config.read("../car-backend/development.ini")

print(config.get("db","port"))