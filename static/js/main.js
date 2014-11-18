var Cars = (function ($) {

    var btn = $('#rent_now')
    var form = $('#rent_form')
    var submit = $('#rent_submit')
    var rate_btn = $('#rate')
    var rate_form = $('#rate_form')
    var rate_list = $('#ratings')
    var rate_number = $('#rate_amount')

    var update_ratings = function (data) {
        var html = ''
        $(data.reviews).each(function (i) {
            html += '<div class="rating">' +
                    '<p class="text-right"><strong>' + data.reviews[i].name +
                    '</strong></p>' + 
                    '<div class="stars" style="width: ' + data.reviews[i].rating * 48 +
                    'px;"></div></div>'
        })
        rate_list.html(html)
        rate_number.text(data.reviews.length)
    }

    var testAlpha = function (data) {
        if (!data) return false
        if (/^[a-zA-ZæøåÆØÅ\w]+$/.test(data)) return true
        return false
    }
    var testAlphaNum = function (data) {
        if (!data) return false
        if (/^[a-zA-Z0-9æøåÆØÅ\w]+/.test(data)) return true
        return false
    }
    var testEmail = function (data) {
        if (/[a-zA-Z\w.]+@[a-zA-Z\w..]+/.test(data)) return true
        return false
    }
    var testPhone = function (data) {
        if (!data) return false
        if (/[0-9]+/.test(data)) return true
        return false
    }

    var validateRentForm = function () {
        var fname = $('#first_name')
        var lname = $('#last_name')
        var email = $('#email')
        var address = $('#address')
        var phone = $('#phone')
        var vendor = $('#vendor')
        fname.removeClass()
        lname.removeClass()
        email.removeClass()
        address.removeClass()
        phone.removeClass()
        vendor.removeClass()

        var errors = []
        
        if (!testAlpha(fname.val())) errors.push('#first_name')
        if (!testAlpha(lname.val())) errors.push('#last_name')
        if (!testEmail(email.val())) errors.push('#email')
        if (!testAlphaNum(address.val())) errors.push('#address')
        if (!testPhone(phone.val())) errors.push('#phone')

        if (errors.length) return errors
        else return true
    }

    return {
        init: function () {
            $(btn).on('click', function (e) {
                e.preventDefault()
                $(form).slideToggle(200)
            })
            $(submit).on('click', function (e) {
                e.preventDefault()
                var da_form = validateRentForm()
                if (da_form === true) {
                    $(form).slideToggle(200, function () {
                        alert('Congratulations! Your car has been reserved.')
                        $(btn).removeClass()
                        $(btn).addClass('button')
                        $(btn).addClass('button-red')
                        $(btn).text('Not available')
                        $(btn).unbind('click')
                    })
                }
                else {
                    $(da_form).each(function (i) {
                        $(da_form[i]).addClass('form-error')
                    })
                    alert('There are errors in the form!')
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
                    success: function (data) {
                        update_ratings(data)
                    },
                    error: function (xhr, thrownError, statusText) {
                        console.log(thrownError)
                    }
                })
            })
            $(contact_submit).on('click', function (e) {
                var contactForm = $('#contact_form')
                var fields = contactForm.serializeArray()
                for (var x = 0; x < fields.length; x++) {
                    if (!fields[x]['value']) {
                        alert('Missing input in fields')
                        return
                    }
                }
                alert('Thank you for your inquiry. We will get in touch shortly.')
            })
            if (location.hash === '#rent_now') {
                $(form).show()
            }
        },
    }
    
})(jQuery)

$(document).ready(function () {
    Cars.init()
})
