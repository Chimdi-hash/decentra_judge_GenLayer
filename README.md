
# DecentraJudge

> **A Decentralized AI Escrow Judge utilizing GenLayer's Equivalence Principle Consensus.**

DecentraJudge is an Intelligent Contract decentralized application (dApp) engineered for the GenLayer ecosystem. It automates freelance milestone escrows by eliminating the traditional "oracle problem" for subjective web data. By leveraging GenLayer’s unique capability to process unstructured text natively, the contract safely fetches web proof, executes decentralized LLM consensus to evaluate task completion, and updates the escrow state automatically.

---

## 🚀 Core Features

* **Subjective LLM Consensus:** Utilizes GenLayer's `gl.eq_principle.prompt_non_comparative` to judge natural language deliverables against task criteria.
* **Deterministic State & Non-Deterministic Execution:** Safely isolates web queries (`gl.nondet.web.get`) inside validator execution layers.
* **Lightweight Direct VM Testing:** Implements an in-memory testing framework bypassing heavy local dependencies—perfect for low-overhead environments.
* **Premium Web Interface:** A highly responsive dashboard styled with a tech-forward **Deep Crimson / Terracotta** visual brand identity.

---

## 📂 Project Directory Structure

```text
decentra_judge/
├── contracts/
│   └── decentrajudge_contract.py  # GenLayer Intelligent Contract backend logic
├── tests/
│   └── test_decentrajudge.py      # Direct Mode automated validation suite
├── frontend/
│   └── index.html                 # Deep Crimson client interactive dashboard
├── conftest.py                    # Test configuration framework settings
└── pytest.ini                     # Pytest suite discovery configuration
