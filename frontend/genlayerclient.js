import { createClient } from "genlayer-js";
import { studionet } from "genlayer-js/chains";

export const client = createClient({
    chain: studionet
});

// Using your contract address from GenLayer Studio
export const CONTRACT_ADDRESS = "0xCE03D94827bD203F0E0a18831c00EEaB95803B5A";