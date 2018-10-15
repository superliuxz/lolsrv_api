import json
from unittest.mock import patch, MagicMock

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import encode_multipart


class TestLolsView(TestCase):
    @patch("lolsrv_api.views.lols.sink")
    def test_get_success(self, mock_sink):
        mock_sink.retrieve_all.return_value = ["123", "abc"]

        response = self.client.get(reverse("lols"))
        self.assertEqual(response.status_code, 200)

        mock_sink.retrieve_all.assert_called_once()

        body = json.loads(response.content.decode("utf-8"))
        self.assertEqual(body, [{"sha": "123"}, {"sha": "abc"}])

    @patch("lolsrv_api.views.lols.sink")
    def test_get_success_empty(self, mock_sink):
        mock_sink.retrieve_all.return_value = []

        response = self.client.get(reverse("lols"))
        self.assertEqual(response.status_code, 200)

        mock_sink.retrieve_all.assert_called_once()

        body = json.loads(response.content.decode("utf-8"))
        self.assertEqual(body, [])

    def test_non_get_fail(self):
        response = self.client.post(reverse("lols"))
        self.assertEqual(response.status_code, 405)

    @patch("lolsrv_api.views.lols.sink")
    def test_post_success(self, mock_sink):
        mock_sink.save.return_value = None

        mock_file = MagicMock()
        mock_file.read.return_value = "this is a mock file"
        mock_file.name = "mock_file.txt"

        data = {
            "lol": mock_file,
            "url": "abc",
            "repo": "test-repo",
            "date": "1234",
            "sha": "zxc321",
        }
        boundary_value = "some_boundary_value"
        content = encode_multipart(boundary_value, data)

        response = self.client.post(
            reverse("uplol"),
            data=content,
            content_type=f"multipart/form-data; " f"boundary={boundary_value}",
        )
        self.assertEqual(response.status_code, 201)

        (repo, date, sha, file_ref), kwargs = mock_sink.save.call_args
        self.assertEqual(repo, "test-repo")
        self.assertEqual(date, "1234")
        self.assertEqual(sha, "zxc321")
        self.assertEqual(file_ref.name, "mock_file.txt")
        self.assertEqual(file_ref.closed, True)

    @patch("lolsrv_api.views.lols.sink")
    def test_post_bad_multipart_request(self, mock_sink):
        mock_sink.save.return_value = None

        mock_file = MagicMock()
        mock_file.read.return_value = "this is a mock file"
        mock_file.name = "mock_file.txt"

        data = {
            "lol": mock_file,
            "url": "abc",
            "repo": "test-repo",
            "date": "1234",
            "sha": "zxc321",
        }
        boundary_value = "some_boundary_value"
        content = encode_multipart(boundary_value, data)

        # missing `boundary=<..>` in the content_type
        response = self.client.post(
            reverse("uplol"), data=content, content_type="multipart/form-data"
        )
        self.assertEqual(response.status_code, 400)
        mock_sink.save.assert_not_called()

    @patch("lolsrv_api.views.lols.sink")
    def test_post_non_multipart_request(self, mock_sink):
        mock_sink.save.return_value = None
        response = self.client.post(
            reverse("uplol"), data={1: 2}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        mock_sink.save.assert_not_called()
