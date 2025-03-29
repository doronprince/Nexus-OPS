// Example: Fetch agents from the backend
async function fetchAgents() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/agents');
        const agents = await response.json();
        console.log('Agents:', agents);
    } catch (error) {
        console.error('Error fetching agents:', error);
    }
}

// Example: Chat with Agent1
async function chatWithAgent1(message) {
    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                agent_id: 1, // Agent1 ID
            }),
        });
        const data = await response.json();
        console.log('Response from Agent1:', data.response);
    } catch (error) {
        console.error('Error chatting with Agent1:', error);
    }
}

// Example usage
fetchAgents();
chatWithAgent1("Hello, how can you assist me?");