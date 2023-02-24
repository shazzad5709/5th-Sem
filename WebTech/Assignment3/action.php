<?php
$fname = $lname = $email = $address = "";
$photo = array();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fname = $_POST["fname"];
    $lname = $_POST["lname"];
    $email = $_POST["email"];
    $address = $_POST["address"];
    $photo = $_FILES["photo"]["name"];

    if (!empty($fname) && !empty($lname) && !empty($email) && !empty($address) && !empty($photo)) {
        $target_dir = "uploads/";
        $target_file = $target_dir . basename($photo);
        move_uploaded_file($_FILES["photo"]["tmp_name"], $target_file);
        
    }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css" />
  <title>MySite</title>
</head>
<body>
<div class="container">
  <div class="box">
    <?php echo("<p>Name<p>");?>
  </div>
  <div class="box">
    <?php echo("<p>$fname $lname<p>");?>
  </div>
  <div class="box picture">
    <?php echo('<img src= "'.$target_file.'" id="upload-img">');?>
  </div>
  <div class="box">
  <?php echo("<p>Email<p>");?>
  </div>
  <div class="box">
    <?php echo("<p>".$email."<p>");?>
  </div>
  <div class="box">
    <?php echo("<p>Address<p>");?>
  </div>
  <div class="box">
    <?php echo("<p>".$address."<p>");?>
  </div>
</div>
</body>
</html>