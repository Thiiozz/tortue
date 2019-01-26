$( document ).ready(function() {
    function refreshLastSubjects() {
        $.get( "/subjects/pending/5", function( data ) {
            objs = JSON.parse(data);
            $("#subjects tbody tr").remove();

            for(var i = 0; i < objs.length; i++) {
                obj = JSON.parse(objs[i]);
                $("#subjects tbody ").append("<tr><td>"+obj.title+"</td><td>"+obj.content+"</td></tr>");
            }
        });
    }

    setInterval(refreshLastSubjects, 10000);
    refreshLastSubjects();
});