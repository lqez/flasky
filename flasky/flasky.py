from flask import Flask
import inspect


class Flasky(object):
    """
    Flasky - Lazy man's Flask Application

    Convert your class into a flask app.

    """
    def __init__(self, rule=None):
        self.app = Flask(__name__)

        if rule:
            self.rule = rule
        else:
            self.rule = {
                'ignore': ['__init__'],
                'map': {'index': '/'},
            }

        for name, func in inspect.getmembers(self, inspect.ismethod):

            if name in self.rule['ignore']:
                continue
            elif name in self.rule['map']:
                self.app.add_url_rule(self.rule['map'][name], view_func=func)
                continue

            url_prefix = [''] + name.split('_')
            args = inspect.getargspec(func).args

            for x in xrange(len(args), 0, -1):
                url = '/'.join(url_prefix + ['<%s>' % _ for _ in args[1:x]])
                self.app.add_url_rule(url, view_func=func)

                if not func.func_defaults:
                    break
                elif x <= len(args) - len(func.func_defaults):
                    break
