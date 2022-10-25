<?php
	$db = mysqli_connect('localhost', 'root','1234','mysitedb') or die('Fail'. mysqli_connect_error());
?>
<html>
	<head>
		<style>
			img{
				height: 344px;
				width: 260px;
				transition: height 0.8s linear 0.2s;
			}
			img:hover{
				height: 444pX;
			}
			table, td, th{
				border-collapse: collapse;
			}
			th{
				color: blue;
				transition: color 1s linear 0.3s;
			}
			th:hover{
				color:red;
			}
			td:hover{
				background-color: pink;
			}
			td{
				transition: background-color 0.3s linear 0.5s;
			}
		</style>
	</head>
	<body>
		<h1>Conexión establecida</h1>
		<table border="1">
			<tr>
				<th>ID</th>
				<th>Título</th>
				<th>Foto</th>
				<th>Valoración</th>
				<th>Género</th>
			</tr>
			<?php 
				//Lanzar una query
				$query = 'SELECT * FROM tPeliculas';
				
				$result = mysqli_query($db, $query) or die('Query error');
				//Recorrer el resultado
				while ($row = mysqli_fetch_array($result)){
					echo '<tr>';
					echo '<td>'.$row[0].'</td>';
					echo '<td>'.$row[1].'</td>';
					echo '<td><img src="'.$row[2];
					echo '"></td>';
					echo '<td>'.$row[3].'</td>';
					echo '<td>'.$row[4].'</td>';
					echo '</tr>';
				}
			?>
		</table>
        <a href="/logout.php">Logout</a>
		<a href="/pass.html">Cambiar contraseña</a>
	</body>
</html>