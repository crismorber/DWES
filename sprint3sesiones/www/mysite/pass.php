<?php 
    $db = mysqli_connect('localhost', 'root','1234','mysitedb') or die('Fail');


    session_start();
    $user = 'NULL';
    if (!empty($_SESSION['user_id'])) {
        $user = $_SESSION['user_id'];
    }
    $passwordA_posted = $_POST['f_passwordA'];
    $passwordN_posted = $_POST['f_passwordN'];

    $query = 'SELECT id, contraseña FROM tUsuarios where id = "'.$id.'"';
    $result = mysqli_query($db, $query) or die('Query error');
    if (mysqli_num_rows($result)>0){
        $only_row = mysqli_fetch_array($result);
        if ($only_row[4] == $passwordA_posted){
            $query = "UPDATE  tUsuarios SET contraseña = '".$passwordN_posted."' WHERE id =".$id.'; ';
            $result = mysqli_query($db, $query2) or die('Query error');
            header('Location: main.php');
        } else{
            echo '<p>Contraseña incorrecta</p>';
        }
    }
    ?>
