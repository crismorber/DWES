<html>
	<body>
		<h1>Página de bienvenida</h1>
		<?php
			function dar_bienvenida($nombre) {
				echo "¡Bienvenida, " .  $nombre . "!";
			}	
			dar_bienvenida("Robin Williams");
		?>
	</body>
</html>
