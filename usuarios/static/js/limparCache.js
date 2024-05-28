window.addEventListener('beforeunload', function(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/deletar_vars/', true);
    xhr.send();
});