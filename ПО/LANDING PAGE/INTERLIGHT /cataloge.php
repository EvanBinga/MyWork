<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    require_once('phpmailer/PHPMailerAutoload.php');
    header('Content-Type: text/html; charset=UTF-8');

    // Получение данных из формы
    $to = $_POST["email"]; // Адрес, указанный пользователем в форме
    $subject = "Приветсвую";
    $INN = $_POST["INN"]; // Получение ИНН из формы

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
    $botToken = 'bot6681067142:AAHLJsnTF3STKeZ9j2Y2In1h3C8v8stDyd0';
    $chatId = '-4029055585';
        $promoCode = strtoupper(substr(uniqid(), 6, 6)); // Пример: ABCDEF

    // Сообщение для отправки в телеграм
    $messageToTelegram = "Новая заявка с формы:\n\n";
    $messageToTelegram .= "Название компании: $companyName\n";
    $messageToTelegram .= "Имя: $userName\n";
    $messageToTelegram .= "Номер: $userNumber\n";
    $messageToTelegram .= "ИНН: $INN\n"; // Добавляем ИНН в сообщение
    $messageToTelegram .= "Email: $email\n";
    $messageToTelegram .= "Согласие на получение информации: $agreeCheckbox\n";
    $messageToTelegram .= "Промокод: $promoCode\n"; // Добавляем промокод в сообщение


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
        // Генерация случайного промокода

        // Добавляем промокод в сообщение для пользователя
        $messageToUser = "<html>
  <body>
        <p>Дорогой(ая) $userName,</p>
        <p>Поздравляем вас с успешной регистрацией на Interlight 2023!</p>
        <p>Ваш промокод: <strong>$promoCode</strong></p>
        <p>Вы можете скачать каталоги по следующим ссылкам:</p>
        <ul>
            <li><a href='https://interlight-altaircom.ru/public_html/img/cataloge/KATALOG_EXCEEDCONN_2023_SITE.pdf' download>Скачать каталог EXCEEDCONN</a></li>
            <li><a href='https://interlight-altaircom.ru/public_html/img/cataloge/Fersan-catalogue_2023_SITE.pdf' download>Скачать каталог FERSAN</a></li>
            <li><a href='https://interlight-altaircom.ru/public_html/img/cataloge/ORTAC_CATALOG_2023_SITE.pdf' download>Скачать каталог ORTAC</a></li>
        </ul>
        <p>Вы также можете посетить наш сайт: <a href='https://altaircom.ru/'>altaircom.ru/</a></p>
    </body>
        </html>";

        // Добавьте промокод к данным для отправки
     $mail->Body = $messageToUser; // Используем сообщение для пользователя
$mail->AltBody = '';

        // Отправка письма
        if ($mail->send()) {
            // Письмо успешно отправлено
            // Здесь можно добавить дополнительные действия или перенаправление пользователя на другую страницу

            // Добавьте JavaScript код для открытия попапа
        echo '<script>';
            echo 'document.addEventListener("DOMContentLoaded", function () {';
            echo '    const popUpCataloge = document.querySelector(".popUpCataloge");';
            echo '    popUpCataloge.style.display = "block";'; // Открываем попап
            echo '});';
            echo '</script>';

            echo '<script>alert("Каталоги доступны для скачивания");</script>';
        } else {
            // Ошибка при отправке письма
            // Здесь можно добавить дополнительные действия или перенаправление пользователя на другую страницу
         
        }
    } else {
        // Ошибка отправки данных в телеграм
        echo '<script>alert("Ошибка при отправке данных в телеграм.");</script>';
    }
}
?>



<!DOCTYPE html>
<html lang="ru">
<head>
    <noscript><div><img src="https://mc.yandex.ru/watch/94916666" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InterLightAltair</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="catalog.css">
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css">

<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" />

</head>
<body>


<div class="popUpCataloge">
    <div class="popUpBoxPopUp">
        <div class="catalogDownloadPopUp">
             <button class="clousPopUpCatalog">Х</button>
            <div class="catalogItemPopUp">
                <a href="/img/cataloge/KATALOG_EXCEEDCONN_2023_SITE.pdf" download>
                    <img src="/img/cataloge/EXCEEDCONN_500x500px.jpg" alt="" class="catImgPopUp">
                    <p>EXCEEDCONN<br>СКАЧАТЬ</p>
                </a>
                
            </div>
            <div class="catalogItemPopUp">
                <a href="/img/cataloge/Fersan-catalogue_2023_SITE.pdf" download>
                    <img src="/img/cataloge/FERSAN_500x500px.jpg" alt="" class="catImgPopUp">
                    <p>FERSAN<br>СКАЧАТЬ</p>
                </a>
                
            </div>
            <div class="catalogItemPopUp">
                <a href="/img/cataloge/ORTAC_CATALOG_2023_SITE.pdf" download>
                    <img src="/img/cataloge/ORTAC_500x500px.jpg" alt="" class="catImgPopUp">
                    <p>ORTAC<br>СКАЧАТЬ</p>
                </a>

            </div>
        </div>
        
    </div>
     
</div>

 


   <div class="popupRegister">
    <div class="popupBox">
        <div class="redboxx">
        <!-- Добавляем кнопку "Закрыть" -->
        <button class="closeButton">Х</button>
        <h2 class="titlePopup">Зарегистрируйтесь и <br>получите промокод.<br>А также возможность скачать каталоги</h2>
<form id="registrationForm" method="POST">
    <!-- Форма для регистрации -->
                <input type="text" name="user_name" placeholder="Ваше имя">
                <input type="email" name="email" placeholder="Ваш Email">
                <input type="text" name="company_name" placeholder="Название компании">
                                <input type="number" name="INN" placeholder="ИНН">       

                <input type="number" name="user_number" placeholder="Номер">

                <div class="chekbox1">
                    <input type="checkbox" id="agreeCheckbox1" name="agreeCheckbox"required style="width: 15px; position: relative; top: 10px;;">
                    <label for="agreeCheckbox">Я соглашаюсь получать информацию о наших продуктах и специальных предложениях</label>
                </div>
                <button type="submit">Зарегистрироваться</button>
                
        </form>

        
    </div>
    </div>
</div>





<!-- 












 -->



<div class="mobile"data-aos="fade-up" data-aos-duration="1000">
    <img src="/img/landing-1 1.png" alt="" class="mobImg">    
    <div class="contentmob"data-aos="fade-up" data-aos-duration="1000">
        <img src="/img/logo.png" alt="logo" class="logom">
        <h1 class="titilemob">Interlight 2023</h1>
        <p class="landingTextmob">Добро пожаловать! Зарегистрируйтесь сейчас и получите возможность скачать наши каталоги и промокод на скидку до 10%<br><br>





        </p>
            <a href="#op" class="buttonLanding" id="buttonLanding1">Скачать каталог Получить  промокод</a>
        </div>
                <p id="sp">Акция не является публичной офертой. Вся информация предоставлена исключительно в информационных целях.*</p>

  
    
       <div class="textBox">
    <h1 class="h111">Скачать каталог</h1>

    </div>
    <div class="catalogDownload">
        <div class="catalogItem" id="op">
            <img src="/img/cataloge/EXCEEDCONN_500x500px.jpg" alt="" class="catImg1">
            <p class="downloadLabel1" id="donwLoad">EXCEEDCONN<br>Скачать</p>
        </div>
        <div class="catalogItem">
            <img src="/img/cataloge/FERSAN_500x500px.jpg" alt="" class="catImg">
            <p class="downloadLabel" id="donwLoad">FERSAN<br>Скачать</p>
        </div>
        <div class="catalogItem">
            <img src="/img/cataloge/ORTAC_500x500px.jpg" alt="" class="catImg">
            <p class="downloadLabel" id="donwLoad">ORTAC<br>Скачать</p>
        </div>
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

    <!-- 










     -->

    <div class="none">
    <div class="container">
        <header>
            <img src="/img/logo.png" alt="logo" class="logo">
            <!-- <p class="headerText">
                Осветим<br>будущее<br>с Altair
            </p> -->
           
        </header>










        <div class="content">
            <h1>Interlight 2023</h1><p id="ps">Добро пожаловать! Зарегистрируйтесь сейчас и получите возможность<br>скачать наши каталоги и промокод на скидку до 10%</p>
                <a href="#" class="buttonLanding" id="buttonLanding11">Скачать каталог Получить  промокод</a>
                              <p id="spp">Акция не является публичной офертой. Вся информация предоставлена исключительно в информационных целях.*</p>

        </div>
    </div>
    <div class="boxAnimate" data-aos="fade-up" data-aos-duration="1000">
          <div class="textBox">
    <h1 class="h111">Скачать каталог</h1>

    </div>
    <div class="catalogDownload">
        <div class="catalogItem">
            <img src="/img/cataloge/EXCEEDCONN_500x500px.jpg" alt="" class="catImg1">
            <p class="downloadLabel1" id="donwLoad">EXCEEDCONN<br>Скачать</p>
        </div>
        <div class="catalogItem">
            <img src="/img/cataloge/FERSAN_500x500px.jpg" alt="" class="catImg">
            <p class="downloadLabel" id="donwLoad">FERSAN<br>Скачать</p>
        </div>
        <div class="catalogItem">
            <img src="/img/cataloge/ORTAC_500x500px.jpg" alt="" class="catImg">
            <p class="downloadLabel" id="donwLoad">ORTAC<br>Скачать</p>
        </div>
    </div> 


    </div>
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
        <h4 class="sliderTitle">Найдите нас по номеру стенда:<br></h4>
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
    <script src="popup.js"></script>
    <script src="main.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    // Определяем инпут с именем "promo_code"
    const promoCodeInput = document.querySelector('input[name="promo_code"]');

    // Вызываем функцию генерации промокода при загрузке страницы
    promoCodeInput.value = "<?php echo $promoCode; ?>";
  });
</script>
</body>
</html>