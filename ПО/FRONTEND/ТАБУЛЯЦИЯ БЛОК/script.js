document.addEventListener('DOMContentLoaded', () => {
    // Получаем элемент списка изображений
    const imageList = document.getElementById('imageList');
    
    // Идентификатор интервала
    let intervalId;

    // Функция запуска интервала
    const startInterval = () => {
        intervalId = setInterval(() => {
            // Получаем активный элемент
            const activeItem = imageList.querySelector('.active');
            
            // Получаем следующий элемент или первый, если активный последний
            const nextItem = activeItem.nextElementSibling || imageList.firstElementChild;

            // Имитируем клик на следующем элементе списка
            nextItem.click();
        }, 2000);
    }

    // Запускаем интервал при загрузке страницы
    startInterval();

    // Обработчик события клика по списку изображений
    imageList.addEventListener('click', (event) => {
        // Останавливаем интервал при клике на элемент списка
        clearInterval(intervalId);

        // Получаем кликнутый элемент
        const clickedItem = event.target;

        // Проверяем, что кликнутый элемент - LI
        if (clickedItem.tagName === 'LI') {
            // Убираем класс 'active' у всех элементов списка
            imageList.querySelectorAll('li').forEach(item => item.classList.remove('active'));

            // Добавляем класс 'active' только к кликнутому элементу списка
            clickedItem.classList.add('active');

            // Получаем индекс кликнутого элемента и обновляем изображение
            const index = Array.from(imageList.children).indexOf(clickedItem);
            changeImage(index);

            // Запускаем интервал заново после клика
            startInterval();
        }
    });

    // Вызываем startInterval сразу после загрузки страницы
    startInterval();
});

// Остальной код без изменений
// Индекс текущего изображения
let currentIndex = 0;

// Массив с путями к изображениям
const images = [

];

// Переменная для хранения элементов списка
let listItems;

// Функция изменения текущего изображения
const changeImage = (index) => {
    currentIndex = index;
    updateImage();
}

// Функция обновления изображения
const updateImage = () => {
    // Получаем все отображаемые изображения
    const displayedImages = document.querySelectorAll('.displayedImage');
    
    // Проходим по каждому изображению
    displayedImages.forEach((img, index) => {
        // Если текущий индекс совпадает с индексом изображения, добавляем класс 'active', иначе убираем
        index === currentIndex ? img.classList.add('active') : img.classList.remove('active');
    });

    // Обновляем переменную с элементами списка
    listItems = document.querySelectorAll('.imageList li');
}
