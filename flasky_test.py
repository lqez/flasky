from flasky import Flasky
import unittest


class MyGorgeousWebSpace(Flasky):
    def __init__(self):
        rule = {
            "ignore": ["__init__", "private"],
            "map": {"index": "/"},
        }
        super(MyGorgeousWebSpace, self).__init__(rule)

    def index(self):
        return "Hello, lazy man :p"

    def private(self):
        return "Hey!"

    def status(self):
        return "I'm ok."

    def status_detail(self):
        return "I'm ok, seriously. (sigh)"

    def author(self, name):
        return "Yeah, I heard about %s, a little bit." % name

    def post(self, slug=None):
        if slug:
            return "I didn't have chance to write about %s." % slug
        else:
            return "What did you expect from me? Ummmm... like a list of blog posts?"


class FlaskyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = MyGorgeousWebSpace().app.test_client()

    def test_mapped(self):
        rv = self.app.get('/')
        assert rv.data == "Hello, lazy man :p"

    def test_ignore(self):
        rv = self.app.get('/private')
        assert rv.status_code == 404

    def test_simple(self):
        rv = self.app.get('/status')
        assert rv.data == "I'm ok."

    def test_autoslash(self):
        rv = self.app.get('/status/detail')
        assert rv.data == "I'm ok, seriously. (sigh)"

    def test_parameter_101(self):
        rv = self.app.get('/author/lqez')
        assert rv.data == "Yeah, I heard about lqez, a little bit."

    def test_parameter_102(self):
        rv = self.app.get('/author')
        assert rv.status_code == 404

    def test_parameter_103(self):
        rv = self.app.get('/author/lqez/idiot')
        assert rv.status_code == 404

    def test_parameter_201(self):
        rv = self.app.get('/post')
        assert rv.data == "What did you expect from me? Ummmm... like a list of blog posts?"

    def test_parameter_202(self):
        rv = self.app.get('/post/django')
        assert rv.data == "I didn't have chance to write about django."


if __name__ == "__main__":
    unittest.main()
