document.addEventListener("DOMContentLoaded", function () {
    const popupRegister = document.querySelector(".popupRegister");
    const closeButton = document.querySelector(".closeButton");
    const downloadButton = document.querySelector("#buttonLanding11"); // Выбираем кнопку "Скачать каталог Получить промокод"
    const catalogImages = document.querySelectorAll(".catalogDownload img"); // Выбираем все изображения
    const downloadLabels = document.querySelectorAll("#donwLoad"); // Выбираем все элементы с классом downloadLabel

    // Функция для открытия попапа
    function openPopup() {
        popupRegister.style.display = "block";
    }

    // Функция для закрытия попапа
    function closePopup() {
        popupRegister.style.display = "none";
    }

    // Назначаем обработчик события клика на кнопке "Закрыть"
    closeButton.addEventListener("click", closePopup);

    // Назначаем обработчик события клика на кнопку "Скачать каталог Получить промокод"
    downloadButton.addEventListener("click", openPopup);

    // Назначаем обработчик события клика на каждое изображение в catalogDownload
    catalogImages.forEach(function (image) {
        image.addEventListener("click", openPopup);
    });

    // Назначаем обработчик события клика на элементы с классом downloadLabel
    downloadLabels.forEach(function (label) {
        label.addEventListener("click", function (event) {
            openPopup(); // Открываем попап при клике на элементе с классом downloadLabel
            event.preventDefault(); // Предотвращаем стандартное действие ссылки
        });
    });

    // Добавляем обработчик события для закрытия попапа при клике за его пределами
    document.addEventListener("click", function (event) {
        if (event.target === popupRegister) {
            closePopup();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closePopup();
        }
    });
});


function closePopupWithAnimation() {
    var popup = document.querySelector('.popUpCataloge');
    var height = popup.clientHeight;
    var animationInterval = setInterval(function () {
        height -= 5; // Скорость анимации (можете изменить)
        popup.style.height = height + 'px';
        if (height <= 0) {
            clearInterval(animationInterval);
            popup.style.display = 'none';
            popup.style.height = ''; // Восстанавливаем исходную высоту
        }
    }, 10);
}

// Функция для закрытия попапа
function closePopupWithAnimation() {
    var popup = document.querySelector('.popUpCataloge');
    var height = popup.clientHeight;
    var animationInterval = setInterval(function () {
        height -= 17; // Скорость анимации (можете изменить)
        popup.style.height = height + 'px';
        if (height <= 0) {
            clearInterval(animationInterval);
            popup.style.display = 'none';
            popup.style.height = ''; // Восстанавливаем исходную высоту
        }
    }, 10);
}

// Обработчик события для закрытия попапа при клике на темную область
var darkOverlay = document.querySelector('.popUpCataloge');
darkOverlay.addEventListener('click', function (event) {
    if (event.target === darkOverlay) {
        closePopupWithAnimation();
    }
});

// Обработчик события для закрытия попапа при клике на кнопку
var closeButton = document.querySelector('.clousPopUpCatalog');
closeButton.addEventListener('click', function () {
    closePopupWithAnimation();
});
