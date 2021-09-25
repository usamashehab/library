
status_length = document.querySelectorAll(".status").length;

for (var i = 0; i < status_length; i++) {
  element = document.getElementsByClassName("status")[i];
  if (element.innerHTML === "Borrowed") {
    document.getElementsByClassName("status")[i].style.color = "tomato";
  } else {
    document.getElementsByClassName("status")[i].style.color = "green";
  }
}
