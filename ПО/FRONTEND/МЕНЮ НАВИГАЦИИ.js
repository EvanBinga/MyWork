/**
 * File navigation.js.
 *
 * Handles toggling the navigation menu for small screens and enables TAB key
 * navigation support for dropdown menus.
 */
( function() {
	const siteNavigation = document.getElementById( 'site-navigation' );

	// Return early if the navigation don't exist.
	if ( ! siteNavigation ) {
		return;
	}

	const button = siteNavigation.getElementsByTagName( 'button' )[ 0 ];

	// Return early if the button don't exist.
	if ( 'undefined' === typeof button ) {
		return;
	}

	const menu = siteNavigation.getElementsByTagName( 'ul' )[ 0 ];

	// Hide menu toggle button if menu is empty and return early.
	if ( 'undefined' === typeof menu ) {
		button.style.display = 'none';
		return;
	}

	if ( ! menu.classList.contains( 'nav-menu' ) ) {
		menu.classList.add( 'nav-menu' );
	}

	// Toggle the .toggled class and the aria-expanded value each time the button is clicked.
	button.addEventListener( 'click', function() {
		siteNavigation.classList.toggle( 'toggled' );

		if ( button.getAttribute( 'aria-expanded' ) === 'true' ) {
			button.setAttribute( 'aria-expanded', 'false' );
		} else {
			button.setAttribute( 'aria-expanded', 'true' );
		}
	} );

	// Remove the .toggled class and set aria-expanded to false when the user clicks outside the navigation.
	document.addEventListener( 'click', function( event ) {
		const isClickInside = siteNavigation.contains( event.target );

		if ( ! isClickInside ) {
			siteNavigation.classList.remove( 'toggled' );
			button.setAttribute( 'aria-expanded', 'false' );
		}
	} );

	// Get all the link elements within the menu.
	const links = menu.getElementsByTagName( 'a' );

	// Get all the link elements with children within the menu.
	const linksWithChildren = menu.querySelectorAll( '.menu-item-has-children > a, .page_item_has_children > a' );

	// Toggle focus each time a menu link is focused or blurred.
	for ( const link of links ) {
		link.addEventListener( 'focus', toggleFocus, true );
		link.addEventListener( 'blur', toggleFocus, true );
	}

	// Toggle focus each time a menu link with children receive a touch event.
	for ( const link of linksWithChildren ) {
		link.addEventListener( 'touchstart', toggleFocus, false );
	}

	/**
	 * Sets or removes .focus class on an element.
	 */
	function toggleFocus() {
		if ( event.type === 'focus' || event.type === 'blur' ) {
			let self = this;
			// Move up through the ancestors of the current link until we hit .nav-menu.
			while ( ! self.classList.contains( 'nav-menu' ) ) {
				// On li elements toggle the class .focus.
				if ( 'li' === self.tagName.toLowerCase() ) {
					self.classList.toggle( 'focus' );
				}
				self = self.parentNode;
			}
		}

		if ( event.type === 'touchstart' ) {
			const menuItem = this.parentNode;
			event.preventDefault();
			for ( const link of menuItem.parentNode.children ) {
				if ( menuItem !== link ) {
					link.classList.remove( 'focus' );
				}
			}
			menuItem.classList.toggle( 'focus' );
		}
	}
}() );






// script.js







// // Функция для открытия попапа
// function openPopup() {
//     var popup = document.getElementById('popup');
//     popup.style.display = 'block';
// }

// // Функция для закрытия попапа
// function closePopup() {
//     var popup = document.getElementById('popup');
//     popup.style.display = 'none';
// }

// // Открываем попап через 5 секунд после загрузки страницы
// window.addEventListener('load', function() {
//     setTimeout(openPopup, 3000);
// });

// // Закрываем попап при клике вне его области
// document.addEventListener('click', function(event) {
//     var popup = document.getElementById('popup');
//     if (event.target === popup) {
//         closePopup();
//     }
// });
// 
// 
// 



document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    let currentIndex = 0;

    const showSlide = (index) => {
        slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    };

    // Функция для переключения на следующий слайд
    const nextSlide = () => {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    };

    const interval = setInterval(nextSlide, 4000);
});





(function($){

//Функция для toggle text
$.fn.extend({
    toggleText: function(a, b){
        return this.text(this.text() == b ? a : b);
    }
});


if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
  $('.wpc-filters-scroll-container').slideUp(300);      
  $('.wpc-filter-set-widget-title').append('<div class="wpc-filter-toggle">Открыть</div>');
} else {
  $('.wpc-filter-set-widget-title').append('<div class="wpc-filter-toggle">Скрыть</div>');
}

$('.wpc-filter-toggle').click(function(){
  $('.wpc-filters-scroll-container').slideToggle(300);      
  $(".wpc-filter-toggle").toggleText('Открыть', 'Скрыть');
});

$('.up-sells h2').text('Сопутствующие товары');

//Устанавливаем в форму "Имя" и ID товара при клике по кнопке
$('.one-click__btn').on( 'click', function() {
  var productName = $(this).data('name');
  var productId = $(this).data('id');
  $('#f1 .form__subtitle').text(productName);
  $('#f1 input[name="productId"]').val(productId);
  $('#f1 input[name="productName"]').val(productName);
});

//Отключить ссылку на изображение - страница товара
$('.woocommerce-product-gallery__image a').on('click', function() {
  return false;
});

//WPBakery Page Builder - изображение со ссылкой на большое 
$('.section').magnificPopup({
  delegate: '.vc_single_image-wrapper',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
    enabled: true,
    navigateByImgClick: true,
    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
  },
  image: {
    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
    titleSrc: function(item) {
      return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
    }
  }
});


//Поиск
$('.h-search__wrap').on('click', '.fa-magnifying-glass', function() {
  $('.h-search__wrap form').submit();
});


//Маска для телеофона
$("input[type=tel]").inputmask("+7 (999) 999-99-99");


/**
* To top
*/
$('body').prepend('<a class="anchor" id="to_top"></a>');


// Появление и исчезновение to_top
$(function(f){
    var element = f('.to-top__link');
    f(window).scroll(function(){
        element['fade'+ (f(this).scrollTop() > 200 ? 'In': 'Out')](500);
    });
});


/*--------------------------------------------------------------
# Popup Form
--------------------------------------------------------------*/
jQuery('.callBack__link, a[href="#f1__wrap"], .callBack__wbp-button a, .one-click__btn, .woocommerce-loop-product__samples').magnificPopup({
  type:'inline',
  midClick: true,
  /* заданная цель
  items: {
    src: '#popup',
    type: 'inline'
  }
  */
});

jQuery('.woocommerce-loop-product__time').magnificPopup({
  type:'inline',
  midClick: true,
  //заданная цель
  items: {
    src: '#delivery-time-popup__mfp',
    type: 'inline'
  }
});

//Чтобы не создавать несколько одинаковых форм с разным заголовком
//меняем заголовок формы по умолчанию data-title='Рассчитать стоимость'
jQuery('.woocommerce-loop-product__samples, .callBack__link').on('click', function() {
  var title = $(this).data('title');
  $('#f1__wrap .form__title').text(title);
});


$('.wpb-gallery-row').magnificPopup({
  delegate: 'a',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
    enabled: true,
    navigateByImgClick: true,
    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
  },
  image: {
    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
    titleSrc: function(item) {
      return '<small>Альтаир</small>';
    }
  }
});

$('.wp-block-gallery').magnificPopup({
  delegate: 'a',
  type: 'image',
  tLoading: 'Loading image #%curr%...',
  mainClass: 'mfp-img-mobile',
  gallery: {
    enabled: true,
    navigateByImgClick: true,
    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
  },
  image: {
    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
    titleSrc: function(item) {
      return '<small>Компания</small>';
    }
  }
});


/*--------------------------------------------------------------
# Ajax Form
--------------------------------------------------------------*/
$(".ajax input[name='phone']").on('click', function(event) {
  $(this).removeClass('error').focus();
});

$(".ajax input[name='phone']").keypress(function() {
  $(this).removeClass('error').focus();
});


//Изменяем текст на имя файла
$('.input-file').each(function() {
  var $input = $(this),
      $label = $input.next('.userfile__label'),
      labelVal = $label.html();

  $input.on('change', function(element) {
    var fileName = '';
    if (element.target.value) fileName = element.target.value.split('\\').pop();
    fileName ? $label.addClass('has-file').find('.userfile__text').html(fileName) : $label.removeClass('has-file').html(labelVal);
 });
});


//Отправка формы
$(".ajax").submit(function() {
  var form = $(this);
  var phone = $(this).find('input[name="phone"]');
  var message = $(this).find('.message');
  var btn = $(this).find('.btn');

  if ( phone.val() == "") {
    message.fadeIn(300).addClass('alert-danger').text('Введите Ваш телефон');
    phone.addClass('error').focus();
  } else {
    //отключаем кнопку
    btn.attr("disabled", true);
    phone.removeClass('error').focus();
    message.fadeIn(300).removeClass('alert-danger').addClass('alert-info').text( 'Отправляем...' );
    $.ajax({
      type: "POST",
      url: "/wp-content/themes/ip/mail.php",
      data: new FormData(this),
      contentType: false,
      cache: false,
      processData:false,
      success: function ( response ) {
        var jsonData = JSON.parse(response);
        if (jsonData.success == "1") {
          message.fadeIn(300).removeClass('alert-danger alert-info').addClass('alert-success').text( jsonData.text );
          //включаем кнопку
          btn.removeAttr("disabled");
          //Очищаем форму и прячем сообщение, через 2 секунды
          setTimeout(function(){
            form[0].reset();
            message.hide();
          }, 2000);
        }
        else {
          message.fadeIn(300).removeClass('alert-danger alert-info').addClass('alert-danger').text( jsonData.text );
          //включаем кнопку
          btn.removeAttr("disabled");
        }
      }
    });//ajax
  }//if
return false;
});//submit

})(jQuery);

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    let currentIndex = 0;

    const showSlide = (index) => {
        slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
    };

    // Функция для переключения на следующий слайд
    const nextSlide = () => {
        slides[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    };

    const interval = setInterval(nextSlide, 4000);
});




// Добавьте этот скрипт в ваш файл скриптов (например, script.js)
function showSuccessPopup() {
    document.querySelector('.popUpContainerForm').style.display = 'flex';
}

function closePopup() {
    document.getElementById('successPopup').style.display = 'none';
}

function showSuccessPopup() {
    document.querySelector('.popUpContainerForm').style.display = 'flex';
}

function closePopup() {
    document.querySelector('.popUpContainerForm').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    const submitButton = document.getElementById('submitButton');

    submitButton.addEventListener('click', (event) => {
        event.preventDefault(); // Предотвращаем стандартное поведение формы

        // Ваш существующий код отправки формы...

        // После успешной отправки формы вызываем функцию показа попапа
        showSuccessPopup();
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('myFormm');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем стандартное поведение формы

        var formData = new FormData(this);

        // AJAX-запрос
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    console.log(xhr.responseText); // Логируем ответ от сервера

                    // Проверка, чтобы попап не отображался, если он уже видим
                    var popup = document.querySelector('.popUpboxDark');
                    if (!popup.classList.contains('active')) {
                        openPopup();
                    }

                    // Раскомментируйте следующую строку, чтобы увидеть ответ сервера в консоли браузера
                    console.log(xhr.responseText);

                    // Раскомментируйте следующую строку, чтобы увидеть, что происходит с формой после успешной отправки
                    this.reset();
                } else {
                    console.error('Ошибка при отправке запроса. Код ошибки: ' + xhr.status);
                }
            }
        };

        xhr.open('POST', '/wp-content/themes/ip/newform.php', true); // Исправляем путь к обработчику
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.send(formData);
    });
});

// Ваш код для открытия попапа
function openPopup() {
    var popup = document.querySelector('.popUpboxDark');
    popup.style.display = 'flex';

    // Добавьте класс active для попапа
    popup.classList.add('active');
}

// Ваш код для закрытия попапа
function closePopup() {
    var popup = document.querySelector('.popUpboxDark');

    // Удалите класс active для попапа
    popup.classList.remove('active');

    // Задержка перед скрытием попапа (время анимации)
    setTimeout(function () {
        popup.style.display = 'none';
    }, 500);
}

 




document.addEventListener("DOMContentLoaded", function () {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.boximgSlide img');
    const bigImage = document.querySelector('.boxvideo .vide');

    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${100 * (i - index)}%)`;
      });
    }

    function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
      updateBigImage();
    }

    function prevSlide() {
      currentIndex = (currentIndex - 1 + slides.length) % slides.length;
      showSlide(currentIndex);
      updateBigImage();
    }

    function updateBigImage() {
      const currentSlide = slides[currentIndex];
      const newSrc = currentSlide.getAttribute('src');
      bigImage.setAttribute('src', newSrc);
    }

    // Привязка к кнопкам
    document.querySelector('.arrow.left').addEventListener('click', prevSlide);
    document.querySelector('.arrow.right').addEventListener('click', nextSlide);
  });



  document.addEventListener("DOMContentLoaded", function () {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.ozonBoximgSlide img');
    const bigImage = document.querySelector('.boxOzonImg img');
  
    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${100 * (i - index)}%)`;
      });
    }
  
    function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
      updateBigImage();
    }
  
    function prevSlide() {
      currentIndex = (currentIndex - 1 + slides.length) % slides.length;
      showSlide(currentIndex);
      updateBigImage();
    }
  
    function updateBigImage() {
      const currentSlide = slides[currentIndex];
      const newSrc = currentSlide.getAttribute('src');
      bigImage.setAttribute('src', newSrc);
    }
  
    // Привязка к кнопкам
    document.querySelector('.ozonArrow.left').addEventListener('click', prevSlide);
    document.querySelector('.ozonArrow.right').addEventListener('click', nextSlide);
  });
  




alert('awdwad');

