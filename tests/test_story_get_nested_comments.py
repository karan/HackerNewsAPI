from hn import Story
import unittest

class TestStoryGetComments(unittest.TestCase):

    def setUp(self):
        self.story = Story.fromid(7404389)
        self.comments = self.story.get_comments()

    def test_get_nested_comments(self):
    	comment = self.comments[0].body
    	print len(comment)
    	self.assertTrue(len(comment) >= 5508)

if __name__ == '__main__':
     unittest.main()
