import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False,bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()
    
    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jame@example.com', content='Hello World, I\'m Jane!')
        assert second_post.id == 2

        time = TimelinePost.select()

        array = []
        for i in range(len(time)):
            array.append([time[i].name,time[i].email, time[i].content])

        assert(array[0][0] == first_post.name and array[0][1] == first_post.email and array[0][2] == first_post.content and array[1][0] == second_post.name and array[1][1] == second_post.email and array[1][2] == second_post.content)