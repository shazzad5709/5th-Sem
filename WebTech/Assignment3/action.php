<?php
$firstName = $lastName = $email = $address = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $address = $_POST['address'];
    $photo = $_FILES['photo']['name'];
  
    if (!empty($name) && !empty($email) && !empty($address) && !empty($photo)) {
      move_uploaded_file($_FILES['photo']['tmp_name'], "uploads/".$photo);
      header('Location: display.php?name='.$name.'&email='.$email.'&address='.$address.'&photo='.$photo);
    }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>