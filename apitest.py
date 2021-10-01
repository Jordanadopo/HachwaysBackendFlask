import unittest
from src.api import create_app, route1, route2


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(test_config=True)
        self.client = self.app.test_client

    def tearDown(self):
        pass

    # Route 1
    def test_200_with_ping(self):
        resp = self.client().get(route1)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json["success"])

    # Route 2
    def test_200_with_one_tag(self):
        resp = self.client().get(route2 + "?tags=culture")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json["posts"])
        for post in resp.json["posts"]:
            self.assertTrue("culture" in post["tags"])

    def test_200_with_two_tags(self):
        resp = self.client().get(route2 + "?tags=culture,tech")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json["posts"])
        for post in resp.json["posts"]:
            self.assertTrue("culture" in post["tags"] or "tech" in post["tags"])

    def test_400_with_no_tag_parameter_in_url(self):
        resp = self.client().get(route2 + "")
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json["error"], "Tags parameter is required")

    def test_200_with_sort(self):
        resp = self.client().get(route2 + "?tags=culture" + "&sortBy=likes")
        self.assertEqual(resp.status_code, 200)
        prev, curr = 0, 0
        for post in resp.json["posts"]:
            self.assertTrue("culture" in post["tags"])
            curr = post["likes"]
            self.assertTrue(curr >= prev)
            prev = curr

    def test_400_with_sort_bad_sort_key(self):
        resp = self.client().get(route2 + "?tags=culture" + "&sortBy=xyz")
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.json["error"], "sortBy parameter is invalid")


if __name__ == "__main__":
    unittest.main()
