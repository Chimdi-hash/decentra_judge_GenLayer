/**
 * app.js — ES module companion
 * Reads the current contract state on page load and logs it to console.
 */
import { client, CONTRACT_ADDRESS } from "./genlayerclient.js";

try {
    const isCompleted = await client.readContract({
        address: CONTRACT_ADDRESS,
        functionName: "get_status",
        args: [],
        stateStatus: "accepted",
    });
    console.log(`[DecentraJudge] Contract ${CONTRACT_ADDRESS} → is_completed: ${isCompleted}`);
} catch (err) {
    console.warn("[DecentraJudge] Could not read contract status:", err.message ?? err);
}