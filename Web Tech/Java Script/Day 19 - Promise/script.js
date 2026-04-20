const url = "https://jsomplaceholder.typicode.com/users";

fetch(url)
  .then((response) => {
    console.log("Response from then - 1: ", response);
    if (!response.ok) {
      throw new Error("Something went wrong...");
    }
    return response.json();
  })
  .then((data) => {
    console.log("Data from then - 2: ", data);
  })
  .catch((error) => {
    console.log("Error in catch: ", error);
  })
  .finally(() => {
    console.log("Final Block");
  });

//   !------------------------------  or  -----------------------------------------

const getUsers = async () => {
  try {
    response = await fetch(url);
    if (!response.ok) {
      throw new Error("Something went Wrong.....");
    }
    console.log("Response after await: ", response);
    const data = await response.json();
  } catch (error) {
    console.log("Error in async catch: ", error)
  }
};
getUsers();
