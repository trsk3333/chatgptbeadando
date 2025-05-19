async function ask() {
  const question = document.getElementById("question").value;
  const responseDiv = document.getElementById("response");

  responseDiv.innerHTML = "Válasz folyamatban...";

  const res = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();
  responseDiv.innerHTML = `<strong>Válasz:</strong><br>${data.answer}`;
}