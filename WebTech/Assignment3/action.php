<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css" />
  <title>MySite</title>
</head>

<body>
  <div class="container">
    <div class="box"></div>
    <div class="box"></div>
    <div class="box picture">
      <?php echo ('<img src= "' . $_GET["photo"] . '" id="upload-img">'); ?>
    </div>
    <div class="box">
      <?php echo ("<p>Name<p>"); ?>
    </div>
    <div class="box">
      <?php echo ("<p>".$_GET["first-name"]." ".$_GET["last-name"]."<p>"); ?>
    </div>
    
    <div class="box">
      <?php echo ("<p>Email<p>"); ?>
    </div>
    <div class="box">
      <?php echo ("<p>" . $_GET["email"] . "<p>"); ?>
    </div>
    <div class="box">
      <?php echo ("<p>Address<p>"); ?>
    </div>
    <div class="box">
      <?php echo ("<p>" . $_GET["address"] . "<p>"); ?>
    </div>
    <div class="box"></div>
  </div>
</body>

</html>