function renderEvidencia(data, type, row, columnIndex) {
    var fields = ["evidencia_comunicacion", "evidencia_presentacion", "evidencia_startup", "evidencia_eeff", "evidencia_dja"];
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
            { "data": "evidencia_comunicacion" },
            { "data": "evidencia_presentacion" },
            { "data": "evidencia_startup" },
            { "data": "evidencia_eeff" },
            { "data": "evidencia_dja" },
            { "data": "cumplimiento" },
            { "data": "opcion" },
        ],
        columnDefs: [
            {
                targets: [2, 3, 4, 5, 6],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row, meta) {
                    return renderEvidencia(data, type, row, meta.col);
                }
            },
            {
                targets: 7,
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (row.cumplimiento) {
                        return '<i class="fas fa-check">';
                    }
                    return '<strong class="text-red"> PENDIENTE </strong>';
                }
            },
            {
                targets: 8,
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/evidenciaA/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    // buttons += '<a href="/erp/evidenciaA/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
