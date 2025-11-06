from starlette.staticfiles import StaticFiles
from markupsafe import Markup
from pyview import PyView
from pyview.template import defaultRootTemplate
from .views import CountLiveView

app = PyView()
app.mount("/static", StaticFiles(packages=[("pyview", "static")]), name="static")

# Configure Web Awesome
web_awesome_includes = Markup("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@awesome.me/webawesome@3.0.0/dist/styles/webawesome.css" />
    <script type="module" src="https://esm.sh/@awesome.me/webawesome@3.0.0/dist/webawesome.loader.js"></script>
""")

app.rootTemplate = defaultRootTemplate(css=web_awesome_includes)

routes = [("/", CountLiveView)]

for path, view in routes:
    app.add_live_view(path, view)
