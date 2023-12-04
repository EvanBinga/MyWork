document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.slide');
    const tabs = document.querySelectorAll('.tab');

    let currentIndex = 0; // Инициализация индекса текущего слайда

    tabs.forEach((tab, index) => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Скрываем текущий активный слайд
            slides[currentIndex].classList.remove('active');

            currentIndex = index; // Обновление текущего индекса при переключении вкладки

            // Показываем выбранный слайд
            slides[currentIndex].classList.add('active');
        });
    });
});