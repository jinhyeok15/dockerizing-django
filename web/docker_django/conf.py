import configparser
import jwt

filename = "docker_django/conf.ini"

config = configparser.ConfigParser()
config.read(filename)

def get_conf(env):
    token = config.get(env, "TOKEN")
    secret = config.get(env, "SECRET")
    return jwt.decode(
        token, secret,
        algorithms=['HS256']
    )
