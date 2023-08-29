function renderEvidencia(data, type, row, columnIndex) {
    var fields = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"];
    var field = fields[columnIndex - 2]; // Restamos 2 porque los campos comienzan desde la tercera columna (índice 2)
    
    if (row[field] === '') {
        return '<strong class="text-red"> PENDIENTE </strong>';
    }

    return '<a href="' + row[field] + '" target="_blank" ><i class="fas fa-file-pdf bg-red fa-lg"></i></a>';
}

$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "position" },
            { "data": "empresa.empresa" },
            { "data": "enero" },
            { "data": "febrero" },
            { "data": "marzo" },
            { "data": "abril" },
            { "data": "mayo" },
            { "data": "junio" },
            { "data": "julio" },
            { "data": "agosto" },
            { "data": "septiembre" },
            { "data": "octubre" },
            { "data": "noviembre" },
            { "data": "diciembre" },
            { "data": "opcion" },
        ],
        columnDefs: [
            {
                targets: [2, 3, 4, 5, 6,7,8,9,10,11,12,13],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row,meta) {
                    return renderEvidencia(data, type, row, meta.col);
                }
            },
            {
                targets:[-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/evidenciaMRC/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    // buttons += '<a href="/erp/evidenciaM/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
