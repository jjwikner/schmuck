<!DOCTYPE html>
<html>
<body>
<?php
$servername = "localhost";
$username = "root";
$password = "pass1234";
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
// Get the last element for photo

$conn = new mysqli('localhost', 'root', 'pass1234', 'skeletor');
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}

if (isset($_POST['move'])) {   
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (1, 0, 0, 0, 0,0,0,0)";
    if (!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}
if (isset($_POST['howl'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 1, 0, 0, 0,0,0,0)";
if (!mysqli_query($conn, $sql)) {
echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}
if (isset($_POST['blink'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 1, 0, 0,0,0,0)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}
if (isset($_POST['click'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 0, 1, 0,0,0,0)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}

if (isset($_POST['photo'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 0, 0, 1,0,0,0)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}


if (isset($_POST['detect'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 0, 0,0,0,0,1)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}

if (isset($_POST['start'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 0, 0,0,0,1,0)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}

if (isset($_POST['quit'])) {
    $sql = "INSERT INTO `Actions` (`Move`, `Howl`, `Blink`, `Click`, `Photo`, `Quit`, `Start`, `Detect`) VALUES (0, 0, 0, 0,0,1, 0,0)";
    if(!mysqli_query($conn, $sql)) {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}

$conn->close();
?>

<form method="post">
  <input   name="move" type="submit" value="Move" style="width: 50%; background-color: red;">
</form>
<form method="post">
    <input name="howl" type="submit" value="Howl" style="width: 50%; background-color: blue;">
</form>
<form method="post">
    <input name="click" type="submit" value="Click" style="width: 50%; height=20%;background-color: green;">
</form>
<form method="post">
    <input name="blink" type="submit" value="Blink" style="width: 50%; background-color: yellow;">
</form>
<form method="post">
    <input name="photo" type="submit" value="Photo" style="width: 50%; background-color: orange;">
</form>
<form method="post">
    <input name="detect" type="submit" value="Detect" style="width: 50%; background-color: orange;">
</form>
<form method="post">
    <input name="start" type="submit" value="Start" style="width: 50%; background-color: orange;">
</form>
<form method="post">
    <input name="quit" type="submit" value="Quit" style="width: 50%; background-color: orange;">
</form>

</body>
</html>
