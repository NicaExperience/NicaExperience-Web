const map = L.map('map').setView([12.8, -85.0], 7);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:'OpenStreetMap'
}).addTo(map);

/* MANAGUA */

L.marker([12.1364, -86.2514])
.addTo(map)
.bindPopup("<b>Managua</b><br>Capital de Nicaragua");

/* GRANADA */

L.marker([11.9344, -85.9560])
.addTo(map)
.bindPopup("<b>Granada</b><br>Ciudad colonial y turística");

/* LEÓN */

L.marker([12.4350, -86.8780])
.addTo(map)
.bindPopup("<b>León</b><br>Cultura, historia y volcanes");

/* OMETEPE */

L.marker([11.5077, -85.6220])
.addTo(map)
.bindPopup("<b>Ometepe</b><br>Isla volcánica y turismo natural");

/* SAN JUAN DEL SUR */

L.marker([11.2529, -85.8705])
.addTo(map)
.bindPopup("<b>San Juan del Sur</b><br>Playas y turismo internacional");