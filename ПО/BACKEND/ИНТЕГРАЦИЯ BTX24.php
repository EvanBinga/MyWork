<?php

// Подключаем библиотеку Crest для работы с API Битрикс24
require_once (__DIR__.'/src/crest.php');

// Получаем данные из POST-запроса
$NAME = $_POST["name"];
$PHONE = $_POST["phone"];
$EMAIL = $_POST['email'];
$prod = $_POST['productName'];
$desc = $message;
$TITLE =  $subject;
$url = $_POST["url"];

// Формируем массив полей для создания лида в Битрикс24
$arFields = array (
    'TITLE' => $TITLE,
    'NAME' => $NAME,
    'PHONE' => (!empty($PHONE)) ? array(array('VALUE' => $PHONE, 'VALUE_TYPE' => 'WORK')) : array(),
    'EMAIL' => (!empty($EMAIL)) ? array(array('VALUE' => $EMAIL, 'VALUE_TYPE' => 'WORK')) : array(),
    'SOURCE_ID' => "WEB",
    'COMMENTS' => $desc,
    'SOURCE_DESCRIPTION' =>  $url,
    'UF_CRM_1671448491' =>  $prod,
);

// Проверяем, есть ли номер телефона
if (!empty($PHONE)) {
    $_COOKIE = array(); // Очищаем массив cookie
}

$arLeadDuplicate = array();

// Проверяем дубликаты по номеру телефона
if (!empty($PHONE)) {
    $arResultDuplicate = CRest::call('crm.duplicate.findbycomm', array (
        "entity_type" => "LEAD",
        "type" => "PHONE",
        "values" => array($PHONE)
    ));
    if (!empty($arResultDuplicate['result']['LEAD'])) {
        $arLeadDuplicate = array_merge ($arLeadDuplicate, $arResultDuplicate['result']['LEAD']);
    }
}

// Проверяем дубликаты по электронной почте
if (!empty($EMAIL)) {
    $arResultDuplicate = CRest::call('crm.duplicate.findbycomm', array (
        "entity_type" => "LEAD",
        "type" => "EMAIL",
        "values" => array($EMAIL)
    ));
    if (!empty($arResultDuplicate[ 'result' ][ 'LEAD' ])) {
        $arLeadDuplicate = array_merge($arLeadDuplicate, $arResultDuplicate[ 'result' ][ 'LEAD' ]);
    }
}

// Если есть дубликаты, получаем информацию о них
if (!empty($arLeadDuplicate)) {
    $arDuplicateLead = CRest::call('crm.lead.list', array (
        "filter" => array(
            '=ID' => $arLeadDuplicate,
            'STATUS_ID' => 'CONVERTED',
        ),
        'select' => array(
            'ID', 'COMPANY_ID', 'CONTACT_ID'
        )
    ));

    // Если дубликаты преобразованы в компании или контакты, связываем с ними создаваемый лид
    if (!empty($arDuplicateLead['result'])) {
        $sCompany = reset(array_diff(array_column($arDuplicateLead['result'],'COMPANY_ID','ID'),array('')));
        $sContact = reset(array_diff(array_column($arDuplicateLead['result'],'CONTACT_ID','ID'),array('')));
        if ($sCompany > 0)
            $arFields['COMPANY_ID'] = $sCompany;
        if ($sContact > 0)
            $arFields['CONTACT_ID'] = $sContact;
    }
}

// Создаем новый лид
$resultLead = CRest::call('crm.lead.add', array (
    'fields' => $arFields
));

/*
// Раскомментируйте следующий блок, если хотите вернуть ответ клиенту
if (!empty($resultLead['result'])) {
    echo 'ok';
} elseif (!empty($resultLead['error_description'])) {
    echo json_encode(['message' => 'Lead not added: ' . $result['error_description']]);
} else {
    echo json_encode(['message' => 'Lead not added']);
}
*/

?>
