import { createClient, createAccount } from "genlayer-js";
import { studionet } from "genlayer-js/chains";

// ── Signer account ────────────────────────────────────────────────────────────
// createAccount() with no args generates a deterministic test account.
// In production, replace with the private key from your GenLayer Studio wallet.
export const account = createAccount();

// ── Client connected to GenLayer Studio (studionet) ──────────────────────────
export const client = createClient({
    chain: studionet,
    account,
});

// ── Deployed contract address ─────────────────────────────────────────────────
export const CONTRACT_ADDRESS = "0xCE03D94827bD203F0E0a18831c00EEaB95803B5A";