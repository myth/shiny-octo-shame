var Cars = (function ($) {

    var btn = $('#rent_now')
    var form = $('#rent_form')
    var submit = $('#rent_submit')

    return {
        init: function () {
            $(btn).on('click', function (e) {
                console.log('Click')
                e.preventDefault()
                $(form).slideToggle(200)
            })
            $(submit).on('click', function (e) {
                e.preventDefault()
                if (Cars.validateForm()) {
                    alert('Congratulations! Your car has been reserved.')
                    $(form).slideToggle(200)
                }
                else {
                    // Do stuff
                    alert('There were errors in the form!')
                }
            })
        },
        validateForm: function () {
            return true;
        }
    }
    
})(jQuery)

$(document).ready(function () {
    Cars.init()
})
