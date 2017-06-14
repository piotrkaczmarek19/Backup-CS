<?php

    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);
    $secret_number = 12345;

if (isset($username) AND isset($password)){
    if($password=="Piotr1212" AND $username=="Mercutio19"){
        print "<h2>Welcome, $username!</h2>
               <p>This is the secret number: $secret_number</p>";
    }else {
        print "Wrong credentials fucker";
    }
}