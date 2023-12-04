document.addEventListener('DOMContentLoaded', function () {
    // Получаем кнопки и контейнер слайдов
    var prevBtn = document.querySelector('.prev');
    var nextBtn = document.querySelector('.next');
    var scrollContainer = document.querySelector('.carouselContainer');
    
    // Получаем все слайды
    var slides = document.querySelectorAll('.scrollone');
    
    // Устанавливаем начальный индекс слайда
    var currentSlideIndex = 2; // Изменено начальное значение

    // Функция обновления стилей слайдов
    function updateSlides() {
        // Проходим по каждому слайду
        slides.forEach(function (slide, index) {
            // Добавляем класс 'active' текущему слайду, убираем у остальных
            if (index === currentSlideIndex) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });

        // Прокручиваем контейнер к текущему слайду с плавным эффектом
        slides[currentSlideIndex].scrollIntoView({
            behavior: 'smooth',
            block: 'center',
            inline: 'center'
        });
    }

    // Обработчик события для кнопки "Вперед"
    nextBtn.addEventListener('click', function () {
        // Увеличиваем индекс слайда с учетом цикличности
        currentSlideIndex = (currentSlideIndex + 1) % slides.length;
        // Обновляем стили слайдов
        updateSlides();
    });

    // Обработчик события для кнопки "Назад"
    prevBtn.addEventListener('click', function () {
        // Уменьшаем индекс слайда с учетом цикличности
        currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
        // Обновляем стили слайдов
        updateSlides();
    });

    // Вызываем функцию обновления стилей для установки начального состояния
    updateSlides();
});
