# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

class DecentraJudge(gl.Contract):
    # 1. State variables declared in the class body for secure blockchain persistence
    client: str
    worker_handle: str
    task_description: str
    is_completed: bool

    def __init__(self, client: str, worker_handle: str, task_description: str):
        self.client = client
        self.worker_handle = worker_handle
        self.task_description = task_description
        self.is_completed = False

    @gl.public.view
    def get_status(self) -> bool:
        return self.is_completed

    @gl.public.write
    def verify_and_pay(self):
        # Local variables to capture state data for the non-deterministic block
        task_info = self.task_description
        url = "https://example.org/freelancer-submission-placeholder"

        # 2. Non-deterministic web fetching operation
        def fetch_worker_delivery() -> str:
            # Safely fetches text content from the target URL
            web_data = gl.nondet.web.get(url, mode="text")
            return web_data

        # 3. Using GenLayer's non-comparative equivalence principle for LLM consensus
        llm_decision = gl.eq_principle.prompt_non_comparative(
            prompt_fn=fetch_worker_delivery,
            task_description=f"Analyze the text data and determine if it satisfies this goal: {task_info}",
            criteria="Return exactly 'YES' if the criteria is fully met, or 'NO' if it is missing or invalid."
        )

        # 4. State updates based on network-verified agreement
        if "YES" in llm_decision:
            self.is_completed = True
