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
    
    // // Ваш код для открытия попапа
    // function openPopup() {
    //     var popup = document.querySelector('.popUpboxDark');
    //     popup.style.display = 'flex';
    
    //     // Добавьте класс active для попапа
    //     popup.classList.add('active');
    // }
    
    // // Ваш код для закрытия попапа
    // function closePopup() {
    //     var popup = document.querySelector('.popUpboxDark');
    
    //     // Удалите класс active для попапа
    //     popup.classList.remove('active');
    
    //     // Задержка перед скрытием попапа (время анимации)
    //     setTimeout(function () {
    //         popup.style.display = 'none';
    //     }, 500);
    // }
    

    







    jQuery(document).ready(function() {

    

        jQuery('.description-info__grid').slick({
          arrows: false,
          dots: false,
          infinite: true,
          slidesToShow: 6,
          slidesToScroll: 1,
          responsive: [
            {
              breakpoint: 1200,
              settings: {
                slidesToShow: 4,
                slidesToScroll: 2,
                arrows: true
              }
            },
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: true,
                arrows: false
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: true,
                arrows: false
              }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
          ]
        });
        
        
        
        /*
        $window = jQuery(window);
        $slick_slider = jQuery('.description-info__grid');
        settings = {
          mobileFirst: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          responsive: [
            {
              breakpoint: 1200,
              settings: "unslick"
            },
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 3
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2
              }
            },
            {
              breakpoint: 450,
              settings: {
                slidesToShow: 1
              }
            }
          ]
        };
        
        $slick_slider.slick(settings);
        
        $window.on('resize', function() {
          if ($window.width() > 1201) {
            //отключаем
            if ($slick_slider.hasClass('slick-initialized'))
              $slick_slider.slick('unslick');
            return
          }
          if ( ! $slick_slider.hasClass('slick-initialized')) {
            return $slick_slider.slick(settings);
          }
        });
        */
        
        });//ready
        
        
        jQuery(document).ready(function() {
        
        /* Слайдер категорий на главной */
        jQuery('.h-catalog .products').slick({
          arrows: true,
          dots: true,
          infinite: true,
          slidesToShow: 6,
          slidesToScroll: 2,
          responsive: [
            {
              breakpoint: 1300,
              settings: {
                slidesToShow: 4,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: true
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: true
              }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
          ]
        });
        
        });//ready
        
        jQuery(document).ready(function() {
        
        
        function checkWidth() {
          var windowSize = jQuery(window).width();
          if (windowSize <= 767) {
              /* Слайдер новостей на главной */
              jQuery('.h-news .vc_pageable-slide-wrapper').slick({
                arrows: false,
                dots: false,
                infinite: true,
                slidesToShow: 4,
                slidesToScroll: 2,
                responsive: [
                  {
                    breakpoint: 767,//>767
                    settings: {
                      infinite: true,
                      slidesToShow: 2,
                      slidesToScroll: 1,
                      arrows: false,
                      dots: true
                    }
                  },
                  {
                    breakpoint: 600,
                    settings: {
                      slidesToShow: 1,
                      slidesToScroll: 1,
                      dots: true,
                      arrows: false
                    }
                  }
                  // You can unslick at a given breakpoint now by adding:
                  // settings: "unslick"
                  // instead of a settings object
                ]
              });
          }
        }//checkWidth
        
        // Execute on load
        checkWidth();
        // Bind event listener
        jQuery(window).resize(checkWidth);
        
        });//ready
        
        
        jQuery(document).ready(function() {
        
        jQuery(".ip-responsive-table__wrap").each(function() {
          let titles = new Array();
          jQuery(this).find('thead th').each(function() {
            titles.push( jQuery( this ).text() );
          });
          jQuery(this).find('tbody tr').each(function() {
            let count = 0;
              // console.log( this );
            jQuery(this).find('td').each(function() {
              jQuery(this).attr("data-label", titles[count]);
              // console.log( this );
              // console.log( count );
              count++;
            });
          });
          // console.log(titles);
          // console.log(titles.length);
        });//table
        
        });//ready
        
        jQuery(document).ready(function() {
        
        /* Слайдер категорий на главной */
        jQuery('.m-why').slick({
          arrows: true,
          dots: true,
          infinite: true,
          slidesToShow: 5,
          slidesToScroll: 2,
          responsive: [
            {
              breakpoint: 1900,//>1900
              settings: {
                slidesToShow: 5,
                slidesToScroll: 2,
                arrows: true
              }
            },
            {
              breakpoint: 1300,//>1300
              settings: {
                slidesToShow: 5,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 2,
                dots: true
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: true
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: true
              }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
          ]
        });
        
        });//ready
        
        (function($){
        $('.good__accord__it.active .good__accord__it__cnt').fadeIn(0);
        
        $('.good__accord__it__title').on('click', function(event) {
            var th = $(this),
                par = th.closest('.good__accord__it'),
                cnt = par.find('.good__accord__it__cnt');
            if (par.hasClass('active')) {
                par.removeClass('active');
                cnt.slideUp(300);
            } else {
                par.addClass('active');
                cnt.slideDown(300);
            }
            event.preventDefault();
        });
        })(jQuery);
        
        /*
        jQuery(document).ready(function() {
          //Slider
          jQuery('.ip-slider').slick({
            // autoplay: true,
            // autoplaySpeed: 5000,
            arrows: true,
            dots: false,
            infinite: true,
            pauseOnHover: false,
            slidesToShow: 1,
            slidesToScroll: 1,
            // responsive: [
            //     {
            //       breakpoint: 1200,
            //       settings: {
            //         arrows: true,
            //         dots: false
            //       }
            //     },
            //     {
            //       breakpoint: 900,
            //       settings: {
            //         arrows: false,
            //         dots: true
            //       }
            //     },
            //     {
            //       breakpoint: 480,
            //       settings: {
            //         arrows: false,
            //         dots: true
            //       }
            //     }
            //   ]
          });
        });//ready
        */
        
        jQuery(document).ready(function() {
        
        function set_title_line_width() {
          jQuery(".title__text").each(function() {
            var widthTitleText = jQuery(this).width();
            jQuery(this).parent().find('.title__line').css('width', widthTitleText);
          });
        }
        set_title_line_width();
        jQuery( window ).resize(function(event) {
          set_title_line_width();
        });
        
        });//ready
        
          document.addEventListener("DOMContentLoaded", function () {
                    const sliderContainer = document.querySelector(".slider-containerNew");
                    const slideBoxes = document.querySelectorAll(".slidreNewBox");
                    let currentIndex = 0;
        
                    function showSlide(index) {
                        slideBoxes.forEach((box) => (box.style.display = "none"));
                        slideBoxes[index].style.display = "block";
                    }
        
                    function nextSlide() {
                        currentIndex = (currentIndex + 1) % slideBoxes.length;
                        showSlide(currentIndex);
                    }
        
                    // Показываем первый слайд при загрузке страницы
                    showSlide(currentIndex);
        
                    // Устанавливаем интервал для автоматического переключения слайдов каждые 3 секунды
                    setInterval(nextSlide, 3000);
                });
        
        
        
          document.addEventListener('DOMContentLoaded', function () {
            var currentSlide = 0;
            var slides = document.querySelectorAll('.itemSliderUp');
            var totalSlides = slides.length;
        
            function showSlide(index) {
              if (index >= totalSlides) {
                currentSlide = 0;
              } else if (index < 0) {
                currentSlide = totalSlides - 1;
              } else {
                currentSlide = index;
              }
        
              var translateValue = -currentSlide * (300 + 5); // Ширина слайда + отступ
              document.querySelector('.boxSliderUp').style.transform = 'translateX(' + translateValue + 'px)';
            }
        
            function nextSlide() {
              showSlide(currentSlide + 1);
            }
        
            // Автоматическое переключение слайдов каждые 3 секунды
            setInterval(function () {
              nextSlide();
            }, 3000);
          });
        
        
        
        document.addEventListener('DOMContentLoaded', () => {
            const imageList = document.getElementById('imageList');
            
            let intervalId;
        
            const startInterval = () => {
                intervalId = setInterval(() => {
                    const activeItem = imageList.querySelector('.active');
                    const nextItem = activeItem.nextElementSibling || imageList.firstElementChild;
        
                    nextItem.click();
                }, 2000);
            }
        
            startInterval();
        
            imageList.addEventListener('click', (event) => {
                clearInterval(intervalId);
        
                const clickedItem = event.target;
        
                if (clickedItem.tagName === 'LI') {
                    imageList.querySelectorAll('li').forEach(item => item.classList.remove('active'));
        
                    clickedItem.classList.add('active');
        
                    const index = Array.from(imageList.children).indexOf(clickedItem);
                    changeImage(index);
        
                    startInterval();
                }
            });
        
            startInterval();
        });
        
        let currentIndex = 0;
        const images = [
        
        ];
        
        let listItems;
        
        const changeImage = (index) => {
            currentIndex = index;
            updateImage();
        }
        
        const updateImage = () => {
            const displayedImages = document.querySelectorAll('.displayedImage');
            displayedImages.forEach((img, index) => {
                index === currentIndex ? img.classList.add('active') : img.classList.remove('active');
            });
        
            listItems = document.querySelectorAll('.imageList li');
        }
        
        

        




        