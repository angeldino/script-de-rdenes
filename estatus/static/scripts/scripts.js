document.getElementById('distanceForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevenir el envío del formulario

    var origin = document.getElementById('origin').value;
    var destination = document.getElementById('destination').value;
    var orden = document.getElementById('orden').value;
    var carro = document.getElementById('carro').value;
    var remolque = document.getElementById('remolque').value;

    // Inicializar el servicio Distance Matrix
    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix(
        {
            origins: [origin],
            destinations: [destination],
            travelMode: 'DRIVING'
        },
        function(response, status) {
            if (status === 'OK') {
                var distance = response.rows[0].elements[0].distance.text;

                // Enviar datos al servidor usando AJAX
                fetch("calculate_distance/", {  // Asegúrate de que esta URL es correcta
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        origin: origin,
                        destination: destination,
                        orden: orden,
                        carro: carro,
                        remolque: remolque,
                        distance: distance
                    })
                })
                .then(response => response.json())
                .then(data => {
                    alert('Distance calculated and saved successfully!');
                })
                .catch(error => console.error('Error:', error));
            } else {
                alert('Error calculating distance: ' + status);
            }
        }
    );
});