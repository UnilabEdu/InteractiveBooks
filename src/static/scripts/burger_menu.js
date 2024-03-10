// BurgerMenu //

const burgerMenu = document.querySelector(".burgerMenu");
const closeBtn = document.querySelector(".closeBtn");
const overlay = document.querySelector(".overlay");
const mobileMenu = document.querySelector(".mobileMenu");

burgerMenu.addEventListener("click", () => {
  overlay.classList.add("active");
  mobileMenu.style.transform = "translateY(0)";
  document.body.style.overflow = "hidden";
});

closeBtn.addEventListener("click", () => {
  overlay.classList.remove("active");
  mobileMenu.style.transform = "translateY(-300px)";
  document.body.style.overflow = "visible";
});
