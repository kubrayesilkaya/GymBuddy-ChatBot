<?php
  // Connect to the database
  $host = "localhost";
  $user = "root";
  $password = "";
  $dbname = "gymbuddy";
  $conn = mysqli_connect($host, $user, $password, $dbname);

  // Check connection
  if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
  }

  // Get the data from the form
  $name = $_POST['Name'];
  $surname = $_POST['Surname'];
  $email = $_POST['Email'];
  $password = $_POST['Password'];
  $weight = $_POST['Weight'];
  $height = $_POST['Height'];
  $age = $_POST['Age'];
  $gender = $_POST['Gender'];

  // Insert the data into the database
  $sql = "INSERT INTO users (name,surname,email,password,height,weight,age,gender ) VALUES ('$name', '$surname', '$email','$password', '$height','$weight','$age','$gender')";
  if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
  } else {
      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }

  // Close the connection
  mysqli_close($conn);
  header("Location: homepage.html");
exit;

?>