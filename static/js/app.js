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

// Grupo de lugares turísticos de Masaya
const lugaresMasaya = L.layerGroup();

// 🌋 Volcán Masaya
L.marker([11.9845, -86.1610])
    .bindPopup('<b>🌋 Volcán Masaya</b><br><a href="/volcan-masaya/">Ver más</a>')
    .addTo(lugaresMasaya);

// 🌊 Laguna de Apoyo
L.marker([11.9235, -86.0420])
    .bindPopup('<b>🌊 Laguna de Apoyo</b>')
    .addTo(lugaresMasaya);

// 🛍️ Mercado de Artesanías
L.marker([11.9748, -86.0950])
    .bindPopup('<b>🛍️ Mercado de Artesanías</b>')
    .addTo(lugaresMasaya);

// 🎭 Centro Cultural de Masaya
L.marker([11.9742, -86.0945])
    .bindPopup('<b>🎭 Centro Cultural de Masaya</b>')
    .addTo(lugaresMasaya);

// 🌳 Parque Central de Masaya
L.marker([11.9739, -86.0948])
    .bindPopup('<b>🌳 Parque Central de Masaya</b>')
    .addTo(lugaresMasaya);

// ⛪ Basílica Menor de Nuestra Señora de la Asunción
L.marker([11.9740, -86.0942])
    .bindPopup('<b>⛪ Basílica Menor de Nuestra Señora de la Asunción</b>')
    .addTo(lugaresMasaya);

// 🏺 Barrio Indígena Monimbó
L.marker([11.9698, -86.0978])
    .bindPopup('<b>🏺 Barrio Indígena Monimbó</b>')
    .addTo(lugaresMasaya);

// 🎨 Talleres de Artesanía
L.marker([11.9730, -86.0965])
    .bindPopup('<b>🎨 Talleres de Artesanía</b>')
    .addTo(lugaresMasaya);

// Marcador del departamento
L.marker([11.9744, -86.0942])
    .addTo(map)
    .bindPopup("<b>📍 Masaya</b><br>Haz clic para explorar sus lugares turísticos.")
    .on("click", function () {
        map.setView([11.9744, -86.0942], 11);
        lugaresMasaya.addTo(map);
    });
    
/* RIVAS */
L.marker([11.4372, -85.8263])
.addTo(map)
.bindPopup("<b>Rivas</b><br>Puerta de la Isla de Ometepe");

/* MATAGALPA */
L.marker([12.9256, -85.9175])
.addTo(map)
.bindPopup("<b>Matagalpa</b><br>La Perla del Septentrión");

/* JINOTEGA */
L.marker([13.0910, -86.0014])
.addTo(map)
.bindPopup("<b>Jinotega</b><br>Ciudad de las Brumas");

/* CHINANDEGA */
L.marker([12.6294, -87.1311])
.addTo(map)
.bindPopup("<b>Chinandega</b><br>Tierra del Volcán San Cristóbal");

/* RÍO SAN JUAN */
L.marker([11.2586, -84.7770])
.addTo(map)
.bindPopup("<b>Río San Juan</b><br>Naturaleza y aventura");

/* COSTA CARIBE */
L.marker([12.1500, -83.7500])
.addTo(map)
.bindPopup("<b>Costa Caribe</b><br>Cultura y playas del Caribe");