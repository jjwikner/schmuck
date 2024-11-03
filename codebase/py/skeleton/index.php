<!DOCTYPE html>
<html>
<body>
<?php
$servername = "localhost";
$username = "root";
$password = "s0mmar!#$23";
$dbname = "skeletor";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
//$sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`) VALUES (12, 12, 12, 12)";
//if(mysqli_query($conn, $sql)) {
//    echo "New record created successfully";
//} else {
//    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
//}
mysqli_close($conn);
?>


<?php

if (isset($_POST['move'])) {
    $conn = new mysqli('localhost', 'root', 's0mmar!#$23', 'skeletor');    
    if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error);
    }
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`) VALUES (1, 0, 0, 0)";
    if(mysqli_query($conn, $sql)) {
    echo "";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
    echo "Gesture New records created successfully";
    $conn->close();
}

if (isset($_POST['howl'])) {
    $conn = new mysqli('localhost', 'root', 's0mmar!#$23', 'skeletor');    
    if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error);
    }
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`) VALUES (0, 1, 0, 0)";
    if(mysqli_query($conn, $sql)) {
    echo "";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
    echo "";
    $conn->close();
}

if (isset($_POST['blink'])) {
    echo "BLINK!";
    //make a database connection
    $conn = new mysqli('localhost', 'root', 's0mmar!#$23', 'skeletor');    
    if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error);
    }
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`) VALUES (0, 0, 1, 0)";
    if(mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
    echo "";
    $conn->close();
}

if (isset($_POST['click'])) {
    $conn = new mysqli('localhost', 'root', 's0mmar!#$23', 'skeletor');    
    if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error);
    }
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`) VALUES (0, 0, 0, 1)";
    if(mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
    echo "";
    $conn->close();
}
?>

<form method="post">
    <input name="move" type="submit" value="Move" style="background-color: red;">
</form>
<form method="post">
    <input name="howl" type="submit" value="Howl" style="background-color: blue;">
</form>
<form method="post">
    <input name="click" type="submit" value="Click" style="background-color: green;">
</form>
<form method="post">
    <input name="blink" type="submit" value="Blink" style="background-color: yellow;">
</form>

</body>
</html>
