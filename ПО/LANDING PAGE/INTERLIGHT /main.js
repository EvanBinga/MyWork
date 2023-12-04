document.addEventListener("DOMContentLoaded", function() {
    AOS.init({
        duration: 1000, // Длительность анимации в миллисекундах
        offset: 100, // Отступ, при котором начинается анимация
        easing: "ease-in-out", // Функция плавности анимации
        once: true // Анимация будет проигрываться только один раз
    });
});





const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;

function showSlide(index) {
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });

    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === index);
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
        showSlide(i);
        currentSlide = i;
    });
});

document.querySelector('.sliderPrev').addEventListener('click', prevSlide);
document.querySelector('.sliderNext').addEventListener('click', nextSlide);

showSlide(currentSlide);

setInterval(nextSlide, 5000);


// Добавляем классы для анимаций после загрузки страницы
// Добавляем классы для анимаций после загрузки страницы
// Добавляем классы для анимаций после загрузки страницы
// Уберите этот код
window.addEventListener('load', () => {
    const logo = document.querySelector('.logo');
    const h1 = document.querySelector('h1');
    const buttonLanding = document.querySelector('.buttonLanding');

    logo.classList.add('animate-logo');
    h1.classList.add('animate-h1');

    // Убираем анимацию из CSS
    buttonLanding.style.animation = 'none';

    // Добавляем анимацию через JavaScript
    buttonLanding.style.transform = 'translateY(100%)';
    buttonLanding.style.animation = 'slideInUp 1s ease-out forwards';
});


// JavaScript для отображения и скрытия попапа
const visitSitesButton = document.getElementById('visitSitesButton');
const popupContainer = document.createElement('div');
popupContainer.id = 'popupContainer';
const popupContent = document.createElement('div');
popupContent.id = 'popupContent';

// Замените ссылками на ваши сайты
const siteLinks = `
    <a href="https://altaircom.ru/" target="_blank">Altaircom</a><br>
    <a href="https://ortaclar.ru/" target="_blank">Ortac</a><br>
    <a href="https://klemmnik.com/" target="_blank">Klemmnik</a>
`;

popupContent.innerHTML = `
    <h2>Наши сайты:</h2>
    ${siteLinks}
    <button id="closePopupButton">Закрыть</button>
`;

popupContainer.appendChild(popupContent);
document.body.appendChild(popupContainer);

visitSitesButton.addEventListener('click', () => {
    popupContainer.style.display = 'block';
    setTimeout(() => {
        popupContainer.style.height = '100%';
        popupContent.style.transform = 'translateY(0)';
    }, 0);

    // Добавление обработчика события для закрытия по клику вне попапа
    document.addEventListener('click', closePopupOutside);
});

const closePopupButton = document.getElementById('closePopupButton');
closePopupButton.addEventListener('click', closePopup);

function closePopup() {
    popupContainer.style.height = '0';
    popupContent.style.transform = 'translateY(-100%)';
    setTimeout(() => {
        popupContainer.style.display = 'none';
    }, 300);

    // Удаление обработчика события после закрытия
    document.removeEventListener('click', closePopupOutside);
}

function closePopupOutside(event) {
    if (!popupContent.contains(event.target) && event.target !== visitSitesButton) {
        closePopup();
    }
}



// Ваш сценарий JavaScript
// Получение значения email из формы
var email = document.querySelector('input[name="email"]').value;

// Проверка корректности email
if (!isValidEmail(email)) {
    // Если email некорректный, отображаем сообщение об ошибке
    document.getElementById("email-error").style.display = "block";
} else {
    // В противном случае, скрываем сообщение об ошибке (если оно было видимым)
    document.getElementById("email-error").style.display = "none";
}

// Функция для проверки корректности email
function isValidEmail(email) {
    // Регулярное выражение для проверки email
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
