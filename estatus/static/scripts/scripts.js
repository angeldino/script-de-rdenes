function initMap() {
    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix(
        {
            origins: ['26.4618	-100.1633'], // Coordenadas de origen
            destinations: ['COAH 105 2731, 25300 Saltillo, Coah.'], // Destino
            travelMode: 'DRIVING', // Modo de viaje
            unitSystem: google.maps.UnitSystem.METRIC, // Sistema métrico
            avoidTolls: false
        }, callback);
}

function callback(response, status) {
    if (status == 'OK') {
        var origins = response.originAddresses;
        var destinations = response.destinationAddresses;

        // Obtenemos la referencia de la tabla en el DOM
        var table = document.getElementById('resultsTable');

        for (var i = 0; i < origins.length; i++) {
            var results = response.rows[i].elements;
            for (var j = 0; j < results.length; j++) {
                var element = results[j];
                var order = "2032425"
                var truck = "T-1783"
                var trailer = "55432"
                var distance = element.distance.text;
                var eta = element.duration.text;
                var from = origins[i];
                var to = destinations[j];

                // Crear una nueva fila
                var row = table.insertRow(-1);

                // Insertar las celdas en la fila
                var cellOrder = row.insertCell(0);
                var cellTruck = row.insertCell(1);
                var cellTrailer = row.insertCell(2);
                var cellFrom = row.insertCell(3);
                var cellTo = row.insertCell(4);
                var cellDistance = row.insertCell(5);
                var cellEta = row.insertCell(6);

                // Agregar el texto a cada celda
                cellOrder.innerHTML = order;
                cellTruck.innerHTML = truck;
                cellTrailer.innerHTML = trailer;
                cellFrom.innerHTML = from;
                cellTo.innerHTML = to;
                cellDistance.innerHTML = distance;
                cellEta.innerHTML = eta;
            }
        }
    } else {
        console.error('Error:', status);
    }
}

window.onload = initMap;

document.getElementById('downloadBtn').addEventListener('click', function() {
    html2canvas(document.getElementById('contenedor')).then(function(canvas) {
        // Crear un enlace temporal para descargar la imagen
        let link = document.createElement('a');
        link.download = 'tabla_resultados.png';
        link.href = canvas.toDataURL();
        link.click();
    });
});