import os
from unittest import mock

import httpx
import pytest
import respx

from hc_pynomad.exceptions.base import Unauthenticated, UnknownResourceCalled
from hc_pynomad.lib.nomad import Nomad


@respx.mock
def test_get_403(respx_mock):
    nomad = Nomad()
    endpoint = '/testing403'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=403, json={})

    with pytest.raises(Unauthenticated):
        nomad.call(endpoint=endpoint, verb='GET')


@respx.mock
def test_get_404(respx_mock):
    nomad = Nomad()
    endpoint = '/testing404'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=404, json={})

    with pytest.raises(UnknownResourceCalled):
        nomad.call(endpoint=endpoint, verb='GET')


@respx.mock
def test_get_other_http_exception(respx_mock):
    nomad = Nomad()
    endpoint = '/other_error'
    mocked_route = respx_mock.get(url=f'{nomad.address}/v1{endpoint}')
    mocked_route.respond(status_code=500)

    with pytest.raises(httpx.HTTPStatusError):
        nomad.call(endpoint=endpoint, verb='GET')


def test_token_env_present():
    with mock.patch.dict(os.environ, {'NOMAD_TOKEN': 'FANCY_TOKEN'}):
        nomad = Nomad()

        assert nomad.token == 'FANCY_TOKEN'
