var Cars = (function ($) {

    var btn = $('#rent_now')
    var form = $('#rent_form')
    var submit = $('#rent_submit')
    var rate_btn = $('#rate')
    var rate_form = $('#rate_form')

    var update_ratings = function (data) {
        console.log(data)
    }

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
            $(rate_btn).on('click', function (e) {
                e.preventDefault()
                var d = $(rate_form).serializeArray()
                var json_d = {}
                for (var x = 0; x < d.length; x++) {
                    json_d[d[x]['name']] = d[x]['value']
                }
                $.ajax({
                    url: '/rate',
                    type: 'POST',
                    dataType: 'json',
                    contentType: 'application/json',
                    data: JSON.stringify(json_d),
                    done: function (data) {
                        update_ratings(data)
                    },
                    failure: function (xhr, thrownError, statusText) {
                        console.log(thrownError)
                    }
                })
            })
            if (location.hash === '#rent_now') {
                $(form).show()
            }
        },
        validateForm: function () {
            return true;
        },
        rate: function () {
            
        }
    }
    
})(jQuery)

$(document).ready(function () {
    Cars.init()
})
