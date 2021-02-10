$(document).ready( function () {
    $('#dashboard-table').DataTable({
        "paging": false,
        "order": [[1, "asc"]]
    });
} );