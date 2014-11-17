var Cars = (function ($) {

    var btn = $('#rent_car')
    var form = $('#rent_form')

    return {
        init: function () {
            btn.on('click', function (e) {
                e.preventDefault()
                $(form).slideDown(200)
            })
        }
    }
    
})(jQuery)

$(document).ready(function (e) {
    Cars.init()
})
