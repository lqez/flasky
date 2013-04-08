flasky
======
[![Build Status](https://travis-ci.org/lqez/flasky.png?branch=master)](https://travis-ci.org/lqez/flasky)

A Lazy man's Flask application.

Convert your python class into a web application via `Flask`.


USAGE
-----

    from flasky import Flasky

    class MyGorgeousWebSpace(Flasky):
        def index(self):
            return "Hello, lazy man :p"

        def status(self):
            return "I'm ok."

        def author(self, name):
            return "Yeah, I heard about %s, a little bit." % name

        def post(self, slug=None):
            if slug:
                return "I didn't write about %s." % slug
            else:
                return "What did you expect from me? Ummmm.. like a list of blog posts?"


CONVERTING RULES
----------------

 - Each `class method` will be routed with its own name; `def status(self)` > `/status`
 - `underscore` in method name will be replaced with `slash`; `def status_detail(self)` > `/status/detail`
 - Method `parameters` are also treated as `named parameter`; `def author(self, name)` > `/author/<name>`
 - And,
    - `rule.ignore` is a `list` contains ignorable method names. (e.g: `__init__`, `some_private`)
    - `rule.map` is a `dict` contains direct method-to-url maps. (e.g: `index` > `/`)

See [`flasky_test.py`](https://github.com/lqez/flasky/blob/master/flasky/tests/flasky_test.py) to reveal usages.


INSTALL
-------
    pip install flasky


LICENSE
-------
Distributed under MIT license.


AUTHOR
------
Park Hyunwoo / [@lqez](https://twitter.com/lqez)
