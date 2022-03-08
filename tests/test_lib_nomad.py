import httpx
import pytest
import respx

from pynomad.exceptions.base import Unauthenticated, UnknownResourceCalled
from pynomad.lib.nomad import Nomad


@respx.mock
def test_get_403(respx_mock):
    nomad = Nomad(address='http://localhost:4646')
    endpoint = '/testing403'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=403, json={})

    with pytest.raises(Unauthenticated):
        nomad._get(endpoint=endpoint)


@respx.mock
def test_get_404(respx_mock):
    nomad = Nomad(address='http://localhost:4646')
    endpoint = '/testing404'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=404, json={})

    with pytest.raises(UnknownResourceCalled):
        nomad._get(endpoint=endpoint)


@respx.mock
def test_get_other_http_exception(respx_mock):
    nomad = Nomad(address='http://localhost:4646')
    endpoint = '/other_error'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=500)

    with pytest.raises(httpx.HTTPStatusError):
        nomad._get(endpoint=endpoint)
