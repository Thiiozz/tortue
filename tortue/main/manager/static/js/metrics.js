$( document ).ready(function() {
    function refreshMetrics() {
        $.get( "/metrics", function( data ) {
            obj = JSON.parse(data);
            $('#total_number_subjects').text(obj.total_subjects);
            $('#total_pending_subjects').text(obj.pending_subjects);
            $('#total_ready_subjects').text(obj.ready_subjects);
            $('#total_learned_subjects').text(obj.learned_subjects);
        });
    }

    setInterval(refreshMetrics, 5000);
    refreshMetrics();
});