// ! JS way

// const root = document.getElementById("root");
// const h1tag = document.createElement("h1");
// h1tag.textContent = "Hello by JS Way";
// root.append(h1tag);

// ! React way

import { createRoot } from "react-dom/client";
createRoot(document.getElementById("root")).render(
  <h1>Hello in react way!</h1>,
);
