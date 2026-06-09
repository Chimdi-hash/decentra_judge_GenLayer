async function handleVerify(taskId) {
    console.log("DEBUG: Attempting to connect to GenLayer...");
    console.log("DEBUG: Target Contract Address:", CONTRACT_ADDRESS);

    try {
        const tx = await client.writeContract({
            address: CONTRACT_ADDRESS,
            functionName: 'verify_and_pay',
            args: [taskId]
        });

        console.log("DEBUG: Success! Transaction Hash:", tx.hash);
    } catch (error) {
        console.error("DEBUG: Interaction Failed:", error);
    }
}