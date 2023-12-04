<!-- ФОРМА 1 -->

<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    require_once(dirname(__FILE__) . '/phpmailer/PHPMailerAutoload.php');
    header('Content-Type: application/json; charset=UTF-8');

    // Тема письма
    $subject = "Быстрый запрос c Altaircom.ru";

    // Получение данных из формы
    $message = isset($_POST["message"]) ? $_POST["message"] : ''; // Получение сообщения
    $name = isset($_POST["name"]) ? $_POST["name"] : ''; // Получение имени
    $email = isset($_POST["email"]) ? $_POST["email"] : ''; // Получение email
    $phone = isset($_POST["phone"]) ? $_POST["phone"] : ''; // Получение номера телефона

    // Проверка на заполненность обязательных полей
    if (empty($name) || empty($email)) {
        $response = array('status' => 'error', 'message' => 'Заполните обязательные поля.');
        echo json_encode($response);
        exit;
    }

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

    // Отправитель и получатель для письма (жестко заданный адрес)
    $mail->setFrom('khaysarov.ivan@mail.ru', 'ALTAIRCOM');
    $mail->addAddress('altair.b24@mail.ru'); // Замените на желаемый адрес

    // Тема и содержание письма
    $mail->isHTML(true);
    $mail->Subject = $subject;

    // Создаем письмо с HTML-разметкой
    $messageToUser = "<html>
        <body>
            <p>$name оставил заявку:</p>
            <p>Сообщение: $message</p>
            <p>Email: $email</p>
            <p>Номер телефона: $phone</p>
        </body>
    </html>";

    $mail->Body = $messageToUser;

    // Отправка письма
    if ($mail->send()) {
        // Письмо успешно отправлено
        $response = array('status' => 'success', 'message' => 'Письмо успешно отправлено.');
    } else {
        // Ошибка при отправке письма
        $response = array('status' => 'error', 'message' => 'Ошибка при отправке письма.');
    }

    // Возвращаем JSON-ответ
    echo json_encode($response);
}
?>
<!-- Конец формы 1  -->




<!--  -->