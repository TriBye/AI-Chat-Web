async function fetchData() {
    try {
      const response = await fetch("https://YOUR-FLASK-APP.onrender.com/api/hello");
      // ^ Use your actual Render URL and endpoint
      const data = await response.json();
      document.getElementById("output").innerText = data.message;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }
  
  // Attach event listener to the button
  document.getElementById("fetchBtn").addEventListener("click", fetchData);
  