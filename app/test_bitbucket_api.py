import unittest

# To test the following, I would probably implement a spy with mock or magic mock with some handrolled test classes

class GetTests(unittest.TestCase):

    def test_fetch_parameters(self):
        """
        I would test that fetch.get is being parameterized with the correct url + header
        """
        pass

    def test_raise_for_status(self):
        """
        I would test/spy if this function is called on the response object.
        I wouldn't test it's behavior, I trust that raise_for_status will surface an exception as intended
        """
        pass

    def test_next_key_does_not_exist(self):
        """
        I would test that Link is not returned as a header.
        Assert that fetch is only called once
        """
        pass

    def test_next_key_exists(self):
        """
        I would test a good link returned on the header that can be parsed
        I would test that fetch is called twice, each with the correct parameters
        """
        pass

    def test_watcher_url_called_with_fetch(self):
        """
        I would test that fetch.get is being parameterized with the correct watcher url from passed key
        """
        pass

    def test_watcher_url_key_does_not_exist(self):
        """
        I would test that fetch.get is being parameterized with the correct watcher url from passed key
        """
        pass

    def test_watcher_url_request_does_not_have_size_key(self):
        """
        I would test that fetch.get is being parameterized with the correct watcher url from passed key
        """
        pass

    def test_watcher_url_request_has_size_key(self):
        """
        I would test that fetch.get is being parameterized with the correct watcher url from passed key
        """
        pass

    def test_return_value(self):
        """
        I would test that given a response, the correct array of Repo object is returned
        """
        pass

    def test_private_filter(self):
        """
        I would test that private repos are filtered out in the returned Repo object classes
        """
        pass

    def test_return_value_with_next(self):
        """
        I would test that given multiple requests with headers in link, the correct data is returned
        Expecting a single level array of Repo objects.
        """
        pass


if __name__ == '__main__':
    unittest.main()
