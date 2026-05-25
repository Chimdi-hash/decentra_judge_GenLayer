from genlayer import *


class DecentraJudge(gl.Contract):
    """
    An Intelligent Contract that automates freelance task verification and payout
    using GenLayer's non-deterministic consensus and LLM capabilities.
    """

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
        task_info = self.task_description
        worker_id = self.worker_handle

        def leader_fn():
            import json
            url = f"https://api.verifytask.com/worker/{worker_id}/proof"
            proof_resp = gl.nondet.web.get(url)
            proof_content = getattr(proof_resp, "body", proof_resp)
            prompt = (
                "Task Description: " + str(task_info) + "\n"
                "Worker Proof: " + str(proof_content) + "\n\n"
                "Does the proof satisfy the task description? "
                "Reply with ONLY a JSON object: {\"payout\": true} or {\"payout\": false}."
            )
            llm_result = gl.nondet.exec_prompt(prompt)
            return llm_result

        def validator_fn(leader_res):
            import json
            if not isinstance(leader_res, gl.vm.Return):
                return False
            payload = leader_res.calldata
            if payload is None:
                return False
            if isinstance(payload, dict):
                data = payload
            else:
                raw_str = str(payload).strip()
                if raw_str.upper() in ("YES", "TRUE"):
                    return True
                try:
                    data = json.loads(raw_str)
                except (ValueError, TypeError):
                    return False
            if not isinstance(data, dict):
                return False
            verdict = data.get("payout")
            return verdict in (True, "true", "TRUE")

        raw_consensus_result = gl.vm.run_nondet_unsafe(leader_fn, validator_fn)

        if isinstance(raw_consensus_result, gl.vm.Return):
            consensus_result = raw_consensus_result.calldata
        else:
            consensus_result = raw_consensus_result

        import json
        payout_approved = False
        if isinstance(consensus_result, dict):
            payout_val = consensus_result.get("payout")
            payout_approved = payout_val in (True, "true", "TRUE")
        elif consensus_result is not None:
            raw_text = str(consensus_result).strip()
            if raw_text.upper() in ("YES", "TRUE"):
                payout_approved = True
            else:
                try:
                    parsed = json.loads(raw_text)
                    if isinstance(parsed, dict):
                        payout_approved = parsed.get("payout") in (True, "true", "TRUE")
                except (ValueError, TypeError):
                    pass
        if payout_approved:
            self.is_completed = True
