<?php
try
{
    $db = new PDO('mysql:host=localhost;dbname=chat_test;charset = UTF8', 'root', '');
}
catch (Exception $e)
{
    die('Erreur: '.$e->getMessage());
}
$nouveau_message = htmlspecialchars($_POST['message']);
$pseudo = htmlspecialchars($_POST['pseudo']);


$request = $db->prepare("INSERT INTO messages(id, pseudo, message) VALUES('',:pseudo,:message)");
$request->bindvalue(':pseudo', $pseudo, PDO::PARAM_STR);
$request->bindvalue(':message', $nouveau_message, PDO::PARAM_STR);
$request->execute();

header('Location:index.php');
