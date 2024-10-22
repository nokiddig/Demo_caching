from flask import Flask,send_from_directory, make_response, render_template
from flask_caching import Cache
from time import sleep
import os

app = Flask(__name__)

# config cache
cache = Cache(app, config={'CACHE_TYPE': 'FileSystemCache', 'CACHE_DIR': './path/to/cache/directory'})

# link cache into app
cache.init_app(app)

@app.route('/')
@cache.cached(timeout=100)  # Cache trang này trong 60 giây
def hello():
    home_page = 'home.html'
    if os.path.exists(rf"./templates/{home_page}"):
        # Load data
        sleep(5)
        return render_template(home_page)
    else:
        return "File not found!", 403

if __name__ == '__main__':
    app.run(debug=True)
