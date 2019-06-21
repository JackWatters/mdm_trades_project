var slideIndex = 1;

var myTimer;

window.addEventListener("load",function() {
    displaySlides(slideIndex);
    myTimer = setInterval(function(){plusSlides(1)}, 4000);
})


function plusSlides(n){
  clearInterval(myTimer);
  if (n > 0){
    displaySlides(slideIndex += 1);
  } else {
   displaySlides(slideIndex -= 1);
  }
  if (n === -1){
    myTimer = setInterval(function(){plusSlides(n + 2)}, 4000);
  } else {
    myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
  }
}


function thisSlide(n){
  clearInterval(myTimer);
  myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
  displaySlides(slideIndex = n);
}


function displaySlides(n){
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
       slideIndex = 1
   }
  if (n < 1) {
       slideIndex = slides.length
   }
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
