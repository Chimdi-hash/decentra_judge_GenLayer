

﻿# decentra_judge_GenLayer

DecentraJudge — A Decentralized AI Escrow Judge utilizing GenLayer's Equivalence Principle Consensus.

live demo:https://decentra-judge-gen-layer.vercel.app/

Project Overview
DecentraJudge is an "Intelligent Contract" designed to bridge the gap between deterministic blockchain logic and the unstructured reality of the internet. Traditional smart contracts are inherently isolated; they cannot natively perceive natural language or verify external web events without relying on centralized, prone-to-manipulation oracles. DecentraJudge solves this by leveraging GenLayer’s Equivalence Principle to act as a subjective, decentralized escrow agent that understands the context of a freelance agreement.

The application allows clients and workers to lock funds into a contract that doesn't just wait for a manual "release" button. Instead, it utilizes GenLayer’s ability to execute Python code and perform non-deterministic web requests via gl.nondet.web.get. By feeding live web data—such as a developer's GitHub commit or a writer's published article—into a consensus-driven LLM layer, DecentraJudge programmatically verifies if the work meets the natural language criteria of the task description. If the network of validators reaches consensus that the work is complete, the contract autonomously updates its state to release payment, providing a trustless, automated "judge" for the global freelance economy.

Core Pillars & Architecture
Deterministic Backend State: Built using GenLayer’s Python-based contract framework, the core logic handles secure state persistence for client identities, worker handles, and task completion flags, ensuring high-integrity blockchain accounting.
Non-Deterministic Validation Layer: Unlike legacy chains, DecentraJudge executes non-deterministic operations directly within the consensus loop. It fetches live web text and uses LLM-powered "Optimistic Democracy" to evaluate subjective deliverables against natural language requirements.
Modern Frontend Dashboard: A sleek, responsive interface built with Tailwind CSS that provides a real-time view of the "judicial process," showing the contract's transition from task submission to autonomous verification and payout.
Project Directory Layout
text

decentra_judge/
├── contracts/
│   └── decentrajudge_contract.py    # GenLayer Intelligent Contract logic
├── tests/
│   └── test_decentrajudge.py       # Comprehensive pytest suite
├── frontend/
│   └── index.html                  # Deep Crimson/Terracotta dashboard
├── conftest.py                     # Pytest configuration & fixtures
├── pytest.ini                      # Test runner settings
└── .pytest_cache/                  # Local test execution cache

Local Test Execution
DecentraJudge is optimized for a lightweight developer experience, specifically designed to bypass the overhead of local Docker containers by utilizing GenLayer Direct Mode. Follow these steps to execute the test suite:

Initialize Environment: Ensure you have the genlayer SDK installed in your Python environment.
Run Tests: Execute the following command in the root directory:
bash
python -m pytest
Direct Mode Execution: The test suite leverages the conftest.py configuration to run tests in a simulated GenLayer environment. This validates the non-deterministic web-fetching logic and LLM prompt structures safely and instantly without needing to deploy to a live testnet or manage heavy infrastructure.
Visual Brand Identity Context
The project features a tech-forward, high-authority user interface designed to instill confidence in both clients and freelancers. The palette centers on Deep Crimson and Terracotta accents, moving away from generic "crypto-blue" toward a premium, sophisticated aesthetic that feels like a modern legal institution. This "vibe coding" approach ensures the interface is not only functional but provides a seamless, high-end experience for users navigating decentralized arbitration.



