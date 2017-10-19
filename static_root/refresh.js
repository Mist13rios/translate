$(document).ready( function () {

    $('#parsing_request').on('click', function (e) {
        e.preventDefault();

        $.ajax({
            url: '/',
            method: 'POST',
            data: '',
            contentType: false,
            processData: false
        }).done(function(info){
             if (info.success){
                 $('#current').text(info.success)
             } else {
                 alert('Error with ' + info.error)
             }
        });

        return false;

        });

});