<?php

$login = $_POST['username'];
$senha = $_POST['password'];

$checklogin = 'thunder';
$checkpass = 'cat';

if($login==$checklogin and $senha==$checkpass){
   
    echo 'Autenticado.';
}

?>
