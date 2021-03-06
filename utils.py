import web
import simplejson

def json_processor():
    if web.ctx.path.endswith('.json'):
        web.ctx.path = web.ctx.path[:-len(".json")]
        web.ctx.is_json = True
    else:
        web.ctx.is_json = False
        
class Render(web.template.Render):
    """JSON API aware render."""
    def __init__(self, root, base=None):
        web.template.Render.__init__(self, root, base=base)
        
    def __getattr__(self, name):
        if web.ctx.is_json:
            return self.to_json
        else:
            return web.template.Render.__getattr__(self, name)
        
    def to_json(self, d):
        web.header('Content-Type', 'application/json')
        return simplejson.dumps(d)

