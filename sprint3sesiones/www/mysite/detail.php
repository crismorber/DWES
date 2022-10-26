<?php
	$db = mysqli_connect('localhost','root','1234','mysitedb')or die('Fail');
?>
<html>
	<head>
		<style>
			img{
				width:260px;
				height: 344px;
			}
		</style>
	</head>
	<body>
		<?php
			if (!isset($_GET['pelicula_id'])){
				die('No se ha especificado una pelicula');
			}
			$pelicula_id = $_GET['pelicula_id'];
			$query = 'SELECT * FROM tPeliculas WHERE id='.$pelicula_id;
			$result = mysqli_query($db, $query) or die ('Query error');
			$only_row = mysqli_fetch_array($result);
			echo '<h1>'.$only_row['1'].'</h1>';
			echo '<img src="'.$only_row['2'];
			echo '">';
			echo '<h2>'.$only_row['3'].'</h2>';
			echo '<h2>'.$only_row['4'].'</h2>';
		?>
		<h3>Comentarios</h3>
		<ul>
			<?php
				$query2 = 'SELECT * FROM tComentarios WHERE pelicula_id='.$pelicula_id;
				$query3 = 'SELECT tUsuarios.nombre FROM tUsuarios, tComentarios WHERE tUsuarios.id=usuario_id and pelicula_id='.$pelicula_id;
				$result2 = mysqli_query($db, $query2) or die('Query error2');
				$result3 = mysqli_query($db, $query3) or die('Query error3');
				while ($row = mysqli_fetch_array($result2) and $row2=mysqli_fetch_array($result3)) {
					$fecha = $row['fecha'];
					if (is_null($fecha)) {
						echo '<li>'.$row['comentarios']." ".$row2['nombre']." (Sin fecha registrada) </li>";
					}else {
						echo '<li>'.$row['comentarios'].'  '.$row2['nombre']." ".$row['fecha']."</li>";
					}
				}
				mysqli_close($db);
			?>
		</ul>
		<p>Deja un nuevo comentario:</p>
		<form action="/comment.php" method="post">
			<textarea rows="4" cols="50" name="new_comment"></textarea><br>
			<input type="hidden" name="pelicula_id" value="<?php echo $pelicula_id; ?>">
			<input type="submit" value="Comentar">
		</form>
        <a href="/logout.php">Logout</a>
	</body>
</html>
