
status_check = document.querySelector(".status");

if (status_check.innerHTML == "Borrowed") {
  document.getElementById("borrow_btn").innerHTML = "Back to shelf";
  document.getElementById("borrow_btn").style.opacity = "100%";
  document.getElementById("borrow_btn").style.cursor = "pointer";
  document.getElementById("return_date").style.display = "none";
}

function myfun() {
  document.getElementById("borrow_btn").innerHTML = "Borrow";
  document.getElementById("borrow_btn").style.opacity = "100%";
  document.getElementById("borrow_btn").style.cursor = "pointer";
}