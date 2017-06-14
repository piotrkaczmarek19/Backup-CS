<?php

$commentaires = (int)$_POST['billet_id'];

try
{
    $db = new PDO("mysql:host=localhost;dbname=blog_test;charset = utf8", "root", "");
}
catch (Exception $e)
{
    die('Erreur: '.$e->getMessage());
}
$requete = $db->prepare('SELECT auteur, commentaire FROM commentaires WHERE c_id = 1');
$requete->bindValue(":id", $commentaires,PDO::PARAM_INT);
$requete->execute();
$billets = $requete->fetch();
var_dump($billets);
foreach($billets as $billet){
    print"<h1>$billet[auteur]</h1>
          <p>$billet[commentaire]</p>";
}