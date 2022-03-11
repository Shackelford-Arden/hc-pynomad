import unittest

from pynomad.models import agent_models
from tests.fixtures import agent


class TestAgentModels(unittest.TestCase):

    def test_valid_data_member(self):
        results = agent_models.Member.parse_obj(agent.MEMBERS_RESPONSE['Members'][0])

        self.assertEqual(results.port, 4648)

    def test_null_member_tags(self):

        results = agent_models.Member.parse_obj(
            agent.MEMBER_NULL_TAGS
        )

        self.assertTrue(isinstance(results.tags, dict))

    def test_null_member_addr(self):

        results = agent_models.Member.parse_obj(
            agent.MEMBER_NULL_TAGS
        )

        self.assertTrue(isinstance(results.addr, str))
