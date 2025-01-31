async function fetchData() {
    try {
        const response = await fetch("https://ai-chat-web-2oth.onrender.com"); // Replace with your actual backend URL
        const data = await response.json();
        document.getElementById("output").innerText = data.message;
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}