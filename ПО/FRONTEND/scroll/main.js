document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".caruselSlide"); // Corrected class name
    const slides = document.querySelectorAll(".caruselOne");
    const prevButton = document.querySelector(".prev");
    const nextButton = document.querySelector(".next");

    let currentIndex = 0;

    // Добавляем обработчики событий для стрелок
    prevButton.addEventListener("click", () => {
        if (currentIndex > 0) {
            currentIndex--;
        } else {
            currentIndex = slides.length - 1;
        }
        setActiveSlide();
    });

    nextButton.addEventListener("click", () => {
        if (currentIndex < slides.length - 1) {
            currentIndex++;
        } else {
            currentIndex = 0;
        }
        setActiveSlide();
    });

    function setActiveSlide() {
        slides.forEach((slide, index) => {
            slide.classList.remove("active");
            if (index === currentIndex) {
                slide.classList.add("active");
            }
        });
    }
});
