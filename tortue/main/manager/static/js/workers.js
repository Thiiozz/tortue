$( document ).ready(function() {
    function refreshWorkers() {
        $.get( "/workers", function( data ) {
            objs = JSON.parse(data);
            $("#workers tbody tr").remove();

            for(var i = 0; i < objs.length; i++) {
                obj = objs[i];
                $("#workers tbody ").append("<tr><td>"+obj.id+"</td><td>"+obj.last_seen+"</td></tr>");
            }
        });
    }

    setInterval(refreshWorkers, 5000);
    refreshWorkers();
});