const inp1 = document.getElementById("inp1");
const inp2 = document.getElementById("inp2");
inp1.addEventListener("input", (e) => {
  console.log(e.target.value);
});

inp2.addEventListener("change", (e) => {
  console.log(e.target.value);
});

const signupForm = document.getElementById("signupForm");
signupForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const inp1 = document.getElementById("inp1");
  const inp2 = document.getElementById("inp2");
  const inp3 = document.getElementById("inp3");

  console.log(inp1.value);
  console.log(inp2.value);
  console.log(inp3.value);

  //   !----------------------or ---------------------------------

  const formData = new FormData(signupForm);

  console.log(formData.get("name"));
  console.log(formData.get("email"));
  console.log(formData.get("password"));
  console.log(formData.getAll("photo"));

  const pics = formData.getAll("photo");
  const is_valid = pics.every((p) => p.size <= 2097152);

  if (!is_valid) {
    console.log("Large image size");
  }

  signupForm.reset();
});
