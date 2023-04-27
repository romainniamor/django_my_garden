// scripts relatif à la presentation

// modal under navbar 5 sec duration

// selection de la class modal
const modal = document.querySelector(".modal");

//si modal (relatif) {% if messages %}
if (modal) {
// on ajoute à la class modal active qui déclenche transform css
  modal.classList.toggle("active");
// timer de 5sec
  setTimeout(() => {
    modal.classList.remove('active');
  }, 5000);
}


//  vertNav

const burgerToggler = document.querySelector(".burger");
const navLinksContainer = document.querySelector(".nav-links-container");
const body = document.querySelector('body');
const toggleNav = e => {
    if(navLinksContainer.classList.contains("open")){
        body.style.overflow = "auto";
    }else{
        body.style.overflow = "hidden";
    }
    navLinksContainer.classList.toggle("open")
    }
    burgerToggler.addEventListener("click", toggleNav)

    new ResizeObserver(entries => {
    if(entries[0].contentRect.width <= 750){
    navLinksContainer.style.transition = "transform 0.3s ease-out"
    }
    else {
    navLinksContainer.style.transition = "none"
    }
    }).observe(document.body)


// scrollDisplay, intersection obeserver api

const sections = document.querySelectorAll('section');

const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.3
};

console.log(sections)

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('appear');
      observer.unobserve(entry.target); // one time transform
    }
  });
}, options);

sections.forEach(section => {
  observer.observe(section);
});





/*

// extend bar

const extendBtn = document.querySelector(".collection .extend");
console.log(extendBtn)
const displayCards = document.querySelector(".collection .display-cards");

extendBtn.addEventListener('click', () => {
  if (extendBtn.classList.contains('reduce')) {
    extendBtn.classList.remove('reduce');
    extendBtn.innerHTML = "Étendre";
    displayCards.style.height = "540px";
  } else {
    extendBtn.classList.add('reduce');
    extendBtn.innerHTML = "Réduire";
    displayCards.style.height = "auto";
  }
});


*/










