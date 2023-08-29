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
            {"data": "position"},
            {"data": "empresa.empresa"},
            {"data": "propuesta"},
            {"data": "fecha"},
            {"data": "desvinculacion"},
            {"data": "opcion"},
            
        ],
        columnDefs: [
            {
                targets:[2],
                class:'text-center',
                orderable:false,
                render:function(data,type,row){
                  
                    if(row.propuesta==''){
                        return "<strong>NULL</strong>"
                    }
                    return'<a href="'+row.propuesta+'" target="_blank" ><i class="fas fa-file-pdf bg-red fa-lg"></i></a>';
                    
                }
            },
            {
                targets:[4],
                class:'text-center',
                orderable:false,
                render:function(data,type,row){
                    if(row.desvinculacion==''){
                        return "<strong>NULL</strong>"
                    }
                   return'<a href="'+row.desvinculacion+'" target="_blank" ><i class="fas fa-file-pdf bg-red fa-lg"></i></a>';
                  
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/evidenciaU/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    // buttons += '<a href="/erp/evidenciaU/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});