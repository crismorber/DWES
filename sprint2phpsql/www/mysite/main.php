<?php
	$db = mysqli_connect('localhost', 'root','1234','mysitedb') or die('Fail'. mysqli_connect_error());
?>
<html>
	<head>
		<style>
			img{
				height: 344px;
				width: 260px;
			}
		</style>
	</head>
	<body>
		<h1>Conexión establecida</h1>
		<?php 
			//Lanzar una query
			$query = 'SELECT * FROM tPeliculas';
			
			$result = mysqli_query($db, $query) or die('Query error');
			//Recorrer el resultado
			while ($row = mysqli_fetch_array($result)){
			echo $row[0];
			echo '<br>';
			echo  $row['1'];
			echo '<br>';
			echo '<img src="'.$row['2'];
			echo '">';
			echo '<br>';
			echo $row['3'];
			echo '<br>';
			echo $row['4'];
			echo '<br>';
			}
		?>
	</body>
</html>
