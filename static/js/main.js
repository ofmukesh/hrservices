function openCloseNav() {
  var width = window.innerWidth > 0 ? window.innerWidth : screen.width;
  console.log(document.getElementById("mySidenav").style.width);
  if (document.getElementById("mySidenav").style.width == "0px") {
    document.getElementById("mySidenav").style.width = "250px";
    if (width > 600) {
      document.getElementById("main").style.marginLeft = "260px";
    }
  } else {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "4px";
  }
}