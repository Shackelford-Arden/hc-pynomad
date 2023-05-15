from typing import Optional

from pydantic.dataclasses import dataclass

from hc_pynomad import Nomad
from hc_pynomad.models.jobs import Job


@dataclass
class Jobs(Nomad):
    """Client to interact with the Jobs endpoint."""

    def list_jobs(self,
                  prefix: Optional[str] = None, next_token: Optional[str] = None,
                  per_page: Optional[int] = 0, filter: Optional[str] = None,
                  namespace: Optional[str] = None, meta: bool = False
                  ) -> list[Job]:
        """
        This endpoint lists all known jobs in the system registered with Nomad.

        API Docs: https://developer.hashicorp.com/nomad/api-docs/jobs#list-jobs

        Parameters
        ----------
        prefix: Optional[str] = None
            Specifies a string to filter jobs on based on an index prefix.
            This is specified as a query string parameter.
        next_token: Optional[str] = None
            This endpoint supports paging. The next_token parameter accepts
            a string which identifies the next expected job.

            Added in Nomad 1.3.x.
        per_page: Optional[int] = 0
            Specifies a maximum number of jobs to return for this request.
            If omitted, the response is not paginated.

            Added in Nomad 1.3.x.
        filter: Optional[str] = None
            Specifies the expression used to filter the results. Consider using pagination
            or a query parameter to reduce resource used to serve the request.

            Added in Nomad 1.3.x.
        namespace: Optional[str] = None
            Specifies the target namespace. Specifying * would return all jobs
            across all the authorized namespaces.
        meta: bool = False
             If set, jobs returned will include a meta field containing key-value pairs
             provided in the job specification's meta block.

             Added in Nomad 1.4.x.

        Returns
        -------
        list[Job]
        """

        endpoint = '/jobs'
        params = {}

        if prefix:
            params['prefix'] = prefix

        if next_token:
            params['next_token'] = next_token

        if per_page:
            params['per_page'] = per_page

        if filter:
            params['filter'] = filter

        if namespace:
            params['namespace'] = namespace

        if meta:
            params['meta'] = meta

        jobs = []
        call_result = self.call(
            endpoint=endpoint, verb='GET', params=params
        )

        for job in call_result:
            jobs.append(Job.parse_obj(job))

        return jobs





