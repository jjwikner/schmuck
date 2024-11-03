<html>
  <body>
    <?php
     ini_set('display_errors', 1);
     ?>

    <?php
     $mp3 = "None";
     if (isset($_POST['link'])) {   
     $mp3 = $_POST['link'] ; 
     }
     ?>


    <?php
     $conn = new mysqli('localhost', 'root', 'pass1234', 'skeletor');
     $table_name = "radiohead";
     if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }

    $sql = "INSERT INTO `$table_name` (`mp3`) VALUES ('$mp3')";
    
    if (isset($_POST['link'])) {
    
    echo "Starting to play $mp3";
    }    
    if (!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
    $conn->close();
    ?>
    
    <form action="/play.php" method="post">
      <label for="fname">MP3 link</label>
      <input type="text" id="link" name="link"><br><br>
      <input type="submit" value="Submit">
    </form>
    
  </body>
  
</html>
