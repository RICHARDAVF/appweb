function renderEvidencia(data, type, row, columnIndex) {
    var fields = ["evidencia_comunicacion", "evidencia_presentacion", "evidencia_startup", "evidencia_eeff", "evidencia_dja"];
    var field = fields[columnIndex - 2]; // Restamos 2 porque los campos comienzan desde la tercera columna (índice 2)
    
    if (row[field] === '') {
        return '<strong > Pendiente </strong>';
    }

    return '<a href="' + row[field] + '" target="_blank" >Documento</a>';
}

$(function () {
    var table = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        dom:'Qlfrtip',
        conditions:{
            num:{
                'MultipleOf':{
                    conditionName:'MultipleOf',
                    init : function(that,fn,preDefined=null){
                    },
                    inputValue:function(el){
                        return $(el[0].val());
                    },
                    isInputValid:function(el,that){
                        return $(el[0].val().length!==0);
                    },
                    search:function(value,comparison){
                        return value%comparison===0;
                    }
                }
            }
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "empresa.empresa" },
            { "data": "evidencia_comunicacion" },
            { "data": "evidencia_presentacion" },
            { "data": "evidencia_startup" },
            { "data": "evidencia_eeff" },
            { "data": "evidencia_dja" },
            { "data": "cumplimiento" },
            { "data": "id" },
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
            new $.fn.dataTable.Buttons(table, {
                buttons: [
                    'copy', 'excel', 'csv', 'pdf', 'print',"colvis",
                ],
                // Personalizar la apariencia de los botones (opcional)
                dom: {
                    button: {
                        className: 'btn btn-primary'
                    }
                }
            });

            // Crear un contenedor para los botones de exportación
            var $exportButtonsContainer = $('<div class="export-buttons-container"></div>');
            table.buttons().container().appendTo($exportButtonsContainer);

            // Agregar el contenedor de botones antes del input de búsqueda
            $exportButtonsContainer.insertBefore($('#data_wrapper .dataTables_filter'));
        
        }
    });
});
