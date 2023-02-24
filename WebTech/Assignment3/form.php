<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link rel="stylesheet" href="style.css" />
        <title>MySite</title>
    </head>
    <body>
        <form method="post" enctype="multipart/form-data" action="action.php">
            <div class="row mb-3">
                <label for="fname" class="col-sm-2 col-form-label">First Name</label>
                <div class="col-sm-4">
                  <input required name="fname" type="text" class="form-control" id="fname" placeholder="First Name">
                </div>
                <label for="lname" class="col-sm-2 col-form-label">Last Name</label>
                <div class="col-sm-4">
                  <input required name="lname" type="text" class="form-control" id="lname" placeholder="Last Name">
                </div>
            </div>
            <div class="row mb-3">
                <label for="email" class="col-sm-2 col-form-label">Email</label>
                <div class="col-sm-10">
                  <input required name="email" type="email" class="form-control" id="email" placeholder="email@example.com">
                </div>
            </div>
            <div class="row mb-3">
                <label for="address" class="col-sm-2 col-form-label">Address</label>
                <div class="col-sm-10">
                    <textarea required name="address" class="form-control" id="address" rows="3" placeholder="Address"></textarea>
                </div>
            </div>
            <div class="row mb-3">
                <label for="photo" class="col-sm-2 col-form-label">Photo</label>
                <div class="col-sm-10">
                    <input required name="photo" accept="image/*" class="form-control" type="file" id="photo">
                </div>
            </div>
            <div class="row mb-3 btn-cls">
                <input type="reset" value="Cancel" class="btn btn-dark custom-btn">
                <input type="submit" value="Submit" class="btn btn-secondary custom-btn">
            </div>
        </form>
    </body>
</html>
