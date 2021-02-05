$( document ).ready(function)

$(".dropdown-trigger").dropdown();

document.addEventListener("click", function(){
  document.getElementById("demo").innerHTML = "Hello World";
});

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
  });

  $('.dropdown-trigger').dropdown();