mapboxgl.accessToken = 'pk.eyJ1IjoiYWxyaWZxaSIsImEiOiJjamExdmtkb3IyNXZiMnpsN2R1bjY5Y2xtIn0.GAtd2tMON8Iv4XfUSBOqmw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/alrifqi/cja1yc3z909te2sqc5f614sn4',
});
map.on('load', function () {
  map.addSource("states", {
        "type": "geojson",
        "data": "http://testshbdg.pythonanywhere.com/static/andir.json"
    });
    map.addLayer({
        'id': 'states-layer',
        'type': 'fill',
        'source': 'states',
        'paint': {
            'fill-color': 'rgba(200, 100, 240, 0.4)',
            'fill-outline-color': 'rgba(200, 100, 240, 1)'
        }
    });

    map.addLayer({
        "id": "states-layer-hover",
        "type": "fill",
        "source": "states",
        "layout": {},
        "paint": {
            "fill-color": "#627BC1",
            "fill-opacity": 1
        },
        "filter": ["==", "name", ""]
    });

    map.on('click', 'states-layer', function (e) {
        new mapboxgl.Popup()
            .setLngLat(e.lngLat)
            .setHTML(e.features[0].properties.nama_kelurahan)
            .addTo(map);
    });

    map.on("mousemove", "states-layer", function(e) {
        map.setFilter("states-layer-hover", ["==", "nama_kelurahan", e.features[0].properties.nama_kelurahan]);
        d3.select('#nama_kelurahan').text(e.features[0].properties.nama_kelurahan);
    });
    map.on("mouseleave", "states-layer", function() {
        map.setFilter("states-layer-hover", ["==", "nama_kelurahan", ""]);
    });
});