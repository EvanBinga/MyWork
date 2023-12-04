<?php

require_once (__DIR__.'/src/crest.php');

$NAME = $_POST["name"];
$PHONE = $_POST["phone"];
$EMAIL = $_POST['email'];
$prod = $_POST['productName'];
$desc = $message; // В этой переменной должно быть значение для $desc, которое не определено в предоставленном коде
$TITLE =  $subject;
$url = $_POST["url"];

// Создание массива с полями лида
$arFields = array (
    'TITLE' => $TITLE,
    'NAME' =>$NAME,
    'PHONE' => (!empty($PHONE)) ? array(array('VALUE' => $PHONE, 'VALUE_TYPE' => 'WORK')) : array(),
    'EMAIL' => (!empty($EMAIL)) ? array(array('VALUE' => $EMAIL, 'VALUE_TYPE' => 'WORK')) : array(),
    'SOURCE_ID' => "WEB",
    'COMMENTS' =>$desc,
    'SOURCE_DESCRIPTION' =>  $url,
    'UF_CRM_1671448491' =>  $prod,
);

// Проверка на дублирование по телефону
if (!empty($PHONE)) {
    $arResultDuplicate = CRest::call('crm.duplicate.findbycomm', array(
        "entity_type" => "LEAD",
        "type" => "PHONE",
        "values" => array($PHONE)
    ));

    if (!empty($arResultDuplicate['result']['LEAD'])) {
        // Если найдены дубли, объединить лид с первым найденным дублем
        $firstDuplicateLeadId = reset($arResultDuplicate['result']['LEAD']);
        $arFields['ID'] = $firstDuplicateLeadId;
        $resultLead = CRest::call('crm.lead.update', array(
            'id' => $firstDuplicateLeadId,
            'fields' => $arFields
        ));
    } else {
        // Если дублей не найдено, создать новый лид
        $resultLead = CRest::call('crm.lead.add', array(
            'fields' => $arFields
        ));
    }
}

// Используйте error_log для отладочного вывода
error_log("Message: " . $desc);
error_log("Name: " . $NAME);
error_log("Phone: " . $PHONE);
error_log("Email: " . $EMAIL);
error_log("Product: " . $prod);
error_log("Title: " . $TITLE);
error_log("URL: " . $url);

?>
