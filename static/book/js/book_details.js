status_check = document.querySelector(".status");

if (status_check.innerHTML === "Borrowed") {
  status_check.style.color = "tomato";
  document.getElementById("borrow_form").style.display = "none";
  document.getElementById("return_btn").style.display = "inline";


  

}
else{
  status_check.style.color = "green";

}



function myfun() {
  document.getElementById("borrow_btn").innerHTML = "Borrow";
  document.getElementById("borrow_btn").style.opacity = "100%";
  document.getElementById("borrow_btn").style.cursor = "pointer";
}

status_length = document.querySelectorAll(".status2").length;

for (var i = 0; i < status_length; i++) {
  element = document.getElementsByClassName("status2")[i];
  if (element.innerHTML === "Borrowed") {
    document.getElementsByClassName("status2")[i].style.color = "tomato";
  } else {
    document.getElementsByClassName("status2")[i].style.color = "green";
  }
}
