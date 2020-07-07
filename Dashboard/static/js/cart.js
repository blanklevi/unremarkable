var updateBtns = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    let productId = this.dataset.product;
    let action = this.dataset.action;
    console.log("productId: ", productId, "Action: ", action);

    console.log("User: ", user);
    if (user === []) {
      console.log("Not logged in");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is logged in, sending data...");
  let url = "update_item";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
}
