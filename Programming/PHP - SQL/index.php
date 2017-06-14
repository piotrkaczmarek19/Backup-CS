<?php
try
{
    $db = new PDO("mysql:host=localhost;dbname=chat_test;charset = utf8", "root", "");
}
catch (Exception $e)
{
    die('Erreur: '.$e->getMessage());
}
$reponse = $db->query('SELECT pseudo, message FROM messages ORDER BY ID DESC LIMIT 0, 10');

$messages = $reponse->fetchAll();

try
{
    $db = new PDO("mysql:host=localhost;dbname=blog_test;charset = utf8", "root", "");
}
catch (Exception $e)
{
    die('Erreur: '.$e->getMessage());
}

$requete_insert = $db->query('UPDATE billets SET date_creation = NOW() WHERE 1');
$requete_insert->execute();

$requete = $db->query('SELECT * FROM billets WHERE 1');
$billets = $requete->fetchAll();



include('index.phtml');