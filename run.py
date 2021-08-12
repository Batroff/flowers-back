from flaskr import create_app
from config import config_dict
from decouple import config


DEBUG = config('DEBUG', default=True)
app_config = config_dict['debug'] if DEBUG else config_dict['production']

app = create_app(app_config)

if __name__ == '__main__':
    app.run()
