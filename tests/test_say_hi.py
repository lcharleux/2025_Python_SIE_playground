from dataproc.core import say_hi

def test_say_hi():
    out = say_hi()
    assert out == "Hi buddies"