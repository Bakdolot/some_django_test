import pytest
from rest_framework.test import APIRequestFactory

from .models import Logging
from .views import MainView


@pytest.mark.django_db
class TestMainView:
    @pytest.fixture
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_empty(self, api_rf: APIRequestFactory):
        view = MainView()
        request = api_rf.get("/fake-url/")
        request.data = {"math_string": ""}
        view.request = request
        response = view.post(request)
        assert response.data == {"is_valid": True}

    def test_valid(self, api_rf: APIRequestFactory):
        view = MainView()
        request = api_rf.get("/fake-url/")
        request.data = {"math_string": "()[]{}"}
        view.request = request
        response = view.post(request)
        assert response.data == {"is_valid": True}

    def test_invalid(self, api_rf: APIRequestFactory):
        view = MainView()
        request = api_rf.get("/fake-url/")
        request.data = {"math_string": "123([)]"}
        view.request = request
        response = view.post(request)
        assert response.data == {"is_valid": False}

    def test_brackets_first_close(self, api_rf: APIRequestFactory):
        view = MainView()
        request = api_rf.get("/fake-url/")
        request.data = {"math_string": "423)654("}
        view.request = request
        response = view.post(request)
        assert response.data == {"is_valid": False}

    def test_logs(self, api_rf: APIRequestFactory):
        view = MainView()
        request = api_rf.get("/fake-url/")
        request.data = {"math_string": "423)654("}
        view.request = request
        response = view.post(request)
        log = Logging.objects.last()
        assert log.request_data == request.data
        assert log.response_data == response.data
