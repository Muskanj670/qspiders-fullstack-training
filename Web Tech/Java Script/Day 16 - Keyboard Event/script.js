window.addEventListener("keydown", (e) => {
  e.preventDefault();
  const body = document.body;
  if (e.ctrlKey && (e.key == "d" || e.key == "D")) {
    body.style.backgroundColor = "black";
    body.style.color = "White";
  }

  if (e.ctrlKey && (e.key == "l" || e.key == "L")) {
    body.style.backgroundColor = "white";
    body.style.color = "black";
  }
});

window.addEventListener("keyup", () => {
  const body = document.body;
  body.style.backgroundColor = "white";
  body.style.color = "Red";
});


// ! online offline events

const internetStatus = document.getElementById("status");

window.addEventListener("offline", () => {
  internetStatus.innerHTML = "<p>❌ You are Offline </p>";
});

window.addEventListener("online", () => {
  internetStatus.innerHTML = "<p>✅ You are online </p>";
});

