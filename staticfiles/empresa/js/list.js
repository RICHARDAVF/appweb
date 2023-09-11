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
            {"data": "id"},
            {"data": "empresa"},
            {"data": "ruc"},
            {"data": "supervisor"},
            {"data": "encargado"},
            {"data": "planillero"},
            {"data": "id"},
           
            
        ],
        columnDefs: [
            {
                targets:[-3],
                class:'text-center',
                orderable:false,
                render:function(data,type,row){
                    var enc =row.encargado;
                    if(row.encargado=='nan'){
                        enc = ''
                    }
                    return "<strong>"+enc+"</strong>"
                }
            },
            {
                targets:[-2],
                class:'text-center',
                orderable:false,
                render:function(data,type,row){
                    var plan =row.planillero;
                    if(row.planillero=='nan'){
                        plan = ''
                    }
                    return "<strong>"+plan+"</strong>"
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    
                    var buttons = '<a href="/erp/empresa/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/empresa/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            new $.fn.dataTable.Buttons(table, {
                buttons: [
                    'copy', 'excel', 'csv', 'pdf', 'print',"colvis"
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