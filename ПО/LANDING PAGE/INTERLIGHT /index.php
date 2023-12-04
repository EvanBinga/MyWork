<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    require_once('phpmailer/PHPMailerAutoload.php');
    header('Content-Type: text/html; charset=UTF-8');

    // Получение данных из формы
    $to = $_POST["email"]; // Адрес, указанный пользователем в форме
    $subject = "Получение бесплатного билета на Interlight 2023";
    $companyName = $_POST["company_name"];
    $userName = $_POST["user_name"];
    $userNumber = $_POST["user_number"];
    $email = $_POST["email"];
    $agreeCheckbox = isset($_POST["agreeCheckbox"]) ? $_POST["agreeCheckbox"] : 'Нет'; // Проверка чекбокса на согласие


   if (empty($companyName) || empty($userName) || empty($userNumber) || empty($email)) {
        echo '<script>alert("Error: Заполните обязательные поля.");</script>';
        echo '<script>window.history.back();</script>';
        exit;
    }


// Ваши настройки токена и идентификатора чата для Telegram
$botToken = 'bot6525782237:AAGGGDiNaHe0exbOaqoCvzFhCLUs7gqJCrw';
$chatId = '-4033020470';

// Сообщение для отправки в телеграм
$messageToTelegram = "Новая заявка с формы:\n\n";
$messageToTelegram .= "Название компании: $companyName\n";
$messageToTelegram .= "Имя: $userName\n";
$messageToTelegram .= "Номер: $userNumber\n";
$messageToTelegram .= "Email: $email\n";
$messageToTelegram .= "Согласие на получение информации: $agreeCheckbox\n";

// Отправка сообщения в телеграм
$telegramUrl = "https://api.telegram.org/$botToken/sendMessage?chat_id=$chatId&text=" . urlencode($messageToTelegram);
$ch = curl_init($telegramUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

if ($response !== false) {
    // Данные успешно отправлены в телеграм

    // Создание объекта PHPMailer
    $mail = new PHPMailer;
    $mail->CharSet = 'utf-8';

    // Настройка SMTP сервера для отправки почты
    $mail->isSMTP();
    $mail->Host = 'smtp.mail.ru'; // Укажите ваш SMTP сервер
    $mail->SMTPAuth = true;
    $mail->Username = 'khaysarov.ivan@mail.ru'; // Укажите вашу почту
    $mail->Password = 'hzpwihwCJuJAvLmbKXxi'; // Укажите пароль от почты
    $mail->Port = 465;
    $mail->SMTPSecure = 'ssl';

    // Отправитель и получатель для письма
    $mail->setFrom('khaysarov.ivan@mail.ru', 'Interlight Altair'); // Укажите вашу почту и имя отправителя
    $mail->addAddress($to); // Адрес, указанный пользователем в форме

 // Тема и содержание письма
$mail->isHTML(true);
$mail->Subject = $subject;

// Создаем письмо с HTML-разметкой
$messageToUser = "<html>
    <body>
        <p>Дорогой(ая) $userName,</p>
        <p>Спасибо за ваш запрос на получение бесплатного билета на Interlight 2023.</p>
        <p>Ваш промокод: <a href='https://interlightaltaircom.ru'>IL23-ZKXXH</a></p>
        <p>Вы также можете посетить наш сайт: <a href='https://interlightaltaircom.ru'>https://interlightaltaircom.ru</a></p>
        <p>С уважением, Иван</p>
    </body>
</html>";

$mail->Body = $messageToUser; // Используем сообщение для пользователя
$mail->AltBody = '';


    // Отправка письма
    if ($mail->send()) {
        // Письмо успешно отправлено
        // Здесь можно добавить дополнительные действия или перенаправление пользователя на другую страницу
        echo '<script>alert("Письмо успешно отправлено. Проверьте свою почту для получения билета и промокода.");</script>';
    } else {
        // Ошибка при отправке письма
        // Здесь можно добавить дополнительные действия или перенаправление пользователя на другую страницу
        echo '<script>alert("Ошибка при отправке письма.");</script>';
    }
   } else {
        // Ошибка отправки данных в телеграм
         echo '<script>alert("Ошибка при отправке письма.");</script>';
    }
}


?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <!-- Yandex.Metrika counter -->
<script type="text/javascript" >
    (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
    m[i].l=1*new Date();
    for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
    k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
    (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
 
    ym(94916666, "init", {
         clickmap:true,
         trackLinks:true,
         accurateTrackBounce:true
    });
 </script>
 <noscript><div><img src="https://mc.yandex.ru/watch/94916666" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
 <!-- /Yandex.Metrika counter -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InterLightAltair</title>
    <link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css">

<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" />

</head>
<body>

<div class="mobile"data-aos="fade-up" data-aos-duration="1000">
    <img src="/img/landing-1 1.png" alt="" class="mobImg">    
    <div class="contentmob"data-aos="fade-up" data-aos-duration="1000">
        <img src="/img/logo.png" alt="logo" class="logom">
        <h1 class="titilemob">Interlight 2023</h1>
        <p class="landingTextmob">Мы рады пригласить вас на наш стенд на выставки interlight<br>
            Вас ждут уникальные возможности!<br>
            18.09.23 </p>
            <a href="#myform" class="buttonLandingmob" onclick="scrollToForm()">Получить бесплатный билет</a>
    </div>
        <div class="boxOnem"data-aos="fade-up" data-aos-duration="1000">
            <h2 class="titleExpom">
                О выставке
            </h2>
            <p class="textExpom">
                Интересная возможность для освещения будущего!
                Добро пожаловать на выставку Interlight 2023, одно из ярчайших событий в мире освещения и инноваций. Наша компания гордится быть участником этой выставки и представить перед вами самые передовые технологии и решения в области освещения.
            </p>

            <div class="logoboxm">
                <div class="textlogom">
                    <p class="ulitem">U-LITE</p>
                </div>
                <div class="ortacm">
                    <img src="/img/ort.png" alt="" class="imgLm" id="ortm">
                </div>
                <div class="exedconm">
                    <img src="/img/exceedconn_logo_WH_300px.png" alt="" class="imgLem" id="ortm">
                </div>
                <div class="fersanm">
                    <img src="/img/fersan_logo_WH_300px.png" alt="" class="imgLm" id="ortm">
    
                </div>
    
            </div>


            <h3 class="witExpom">Что вас ожидает на выставке:</h3>
                <img src="/img/mobile.png" alt="" class="mobm">
        </div>


    </div>

    <div class="none">
    <div class="container">
        <header>
            <img src="/img/logo.png" alt="logo" class="logo">
            <!-- <p class="headerText">
                Осветим<br>будущее<br>с Altair
            </p> -->
           
        </header>
        <div class="content">
            <h1>Interlight 2023</h1>
            <p class="landingText animate-text">Мы рады пригласить вас на наш стенд на выставки interlight<br>
                Вас ждут уникальные возможности!<br>
                18.09.23 </p>
                <a href="#myform" class="buttonLanding"  onclick="scrollToForm()">Получить бесплатный билет</a>
        </div>
    </div>
    <div class="boxAnimate" data-aos="fade-up" data-aos-duration="1000">
       
   
    <div class="boxOne" data-aos="fade-up" data-aos-duration="1000">
        <h2 class="titleExpo">
            О выставке
        </h2>
        <p class="textExpo">
            Интересная возможность для освещения будущего!<br>
            Добро пожаловать на выставку Interlight 2023, одно из ярчайших событий в мире освещения и инноваций. Наша компания гордится<br>быть участником этой выставки и представить перед вами самые передовые технологии и решения в области освещения.
        </p>

        <p class="nashiPost">Наши поставщики</p>
        <div class="logobox">
            <div class="textlogo">
                <p class="ulite">U-LITE</p>
            </div>
            <div class="ortac">
                <img src="/img/ort.png" alt="" class="imgL" id="ort">
            </div>
            <div class="exedcon">
                <img src="/img/exceedconn_logo_WH_300px.png" alt="" class="imgLe">
            </div>
            <div class="fersan">
                <img src="/img/fersan_logo_WH_300px.png" alt="" class="imgL">

            </div>

        </div>



        <h3 class="witExpo">Что вас ожидает на выставке:</h3>
            <img src="/img/tab.svg" alt="" class="boxRed">
            <img src="/img/mobile.png" alt="" class="mob">
    </div>
</div>
</div>
<div class="abotUs">
    <button id="visitSitesButton">Посетите наши сайты</button>

</div>
    <div class="slider" data-aos="fade-up" data-aos-duration="1000">
        <h4 class="sliderTitle">Найдите нас по номеру стенда:<br>21C25</h4>
        <div class="sliderControls">
            <div class="sliderPrev">◀</div>
            <div class="sliderNext">▶</div>
          
        </div>
        <div class="sliderContent">
            <div class="slide">
                <img src="/img/1.jpg" alt="Фото 1">
            </div>
            <div class="slide">
                <img src="/img/2.jpg" alt="Фото 2">
            </div>
            <div class="slide">
                <img src="/img/3.jpg" alt="Фото 3">
            </div>
        </div>
        <div class="sliderDots">
            <span class="dot active"></span>
            <span class="dot"></span>
            <span class="dot"></span>
        </div>
    </div>
    <div class="map">

    </div>

    <div class="calbackform" data-aos="fade-up" data-aos-duration="1000">
        <h4 class="formtitile">Получите бесплатный билет!</h4>
        <p class="textForm">Заполните форму ниже, чтобы получить свой бесплатный билет на<br>выставку Interlight 2023</p>
        <div class="formRedBox">
            <form id="myform" class="boxform" action="" method="POST" onsubmit="return validateForm();">
 
                <p class="textInput">Название компании:</p>
                <input type="text" class="inputForm" name="company_name" placeholder="ОАО...."required>
                <p class="textInput">Имя</p>
                <input type="text"  class="inputForm" name="user_name" placeholder="Ваше имя..."required>
                <p class="textInput">Номер</p>
                <input type="number"  class="inputForm" name="user_number" placeholder="+7 (___)-__-__"required>
                <p class="textInput">Email</p>
                <p id="email-error" class="error-message"></p>
                <input type="text" class="inputForm" name="email" placeholder="Email"required>
                <img src="/images/iner.jpg" alt="">

                <div class="chekbox">
                    <input type="checkbox" id="agreeCheckbox" name="agreeCheckbox"required>
                    <label for="agreeCheckbox">Я соглашаюсь получать информацию о наших продуктах и специальных предложениях</label>
                </div>
                <button type="submit" class="buttonForm" name="submit">Получить бесплатный билет</button>
            </form>







             <img src="/img/form.png" alt="" class="formImg">
        </div>
        <div id="success-popup" class="popup">
            <p>Форма успешно отправлена!</p>
            <p>Мы отправили вам билет и промокод на указанный email.</p>
        </div>
    
        <!-- Добавлен стилизованный попап -->
        <div id="error-popup" class="popup">
            <p>Произошла ошибка при заполнении формы:</p>
            <p id="error-message"></p>
            <button id="close-error-popup">Закрыть</button>
        </div>
    
    </div>
    <div class="endLandos"data-aos="fade-up" data-aos-duration="1000">
        <p class="textOne">После заполнения формы мы отправим вам на email ваш бесплатный билет на выставку и<br>
            уникальный промокод, который вы сможете использовать на нашем стенде. Не упустите эту<br>
            уникальную возможность насладиться выставкой в полной мере! 
        </p>
        <p class="textTwo">
            Мы с нетерпением ждем вашего визита!
        </p>
    </div>

    <script src="main.js"></script>

</body>
</html>





