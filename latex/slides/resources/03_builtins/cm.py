class MyManager:
    def __enter__(self):
        # tue dinge
        pass

    def __exit__(self):
        # schließe handler etc ...
        pass

    def do_things(self):
        # ...
        pass

with MyManager() as m:
    m.do_things()
