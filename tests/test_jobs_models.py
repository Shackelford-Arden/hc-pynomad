import unittest
import json

from hc_pynomad.models.jobs import Job


class TestJobModel(unittest.TestCase):

    def test_valid_job(self):
        with open('tests/fixtures/nomad_job.json', encoding='utf8') as job_json:
            jobspec = job_json.read()

        jobspec = json.loads(jobspec)
        Job.model_validate(jobspec.get('Job'))
