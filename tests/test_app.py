import unittest
import os
from flask import Response
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Cyber Sapiens Home</title>" in html
        # TODO Add more tests relating to the home page
        #DONE

        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1 class=\"about-header\">How I ended up an MLH fellow</h1>" in html

        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<source src=\"../static/vid/cyber.mp4\" type=\"video/mp4\" />" in html

        #EXTRA

        response = self.client.get("/maps")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Cyber Sapiens About Us</title>" in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        #TODO Add more tests relating to the /api/timeline_post GET and POST apis

        # . . . 

        #TODO Add more tests relating to the timeline page
        #DONE

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<textarea name=\"content\" type=\"text\" id=\"content\" required></textarea><br><br>" in html
    
    def test_malformed_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={"email":"john@example.com","content":"Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        response = self.client.post("/api/timeline_post", data={"name":"John Doe","email": "john@example.com", "content": ""})
        assert response .status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html