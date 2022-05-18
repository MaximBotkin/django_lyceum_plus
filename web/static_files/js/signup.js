const username = '#id_username'
const email = '#id_email'

function add_error(selector, error_id, text){
    $(selector).removeClass('is-valid').addClass('is-invalid');
    $(selector).after(`<div class="invalid-feedback d-block" id="${error_id}">${text}</div>`);
}

function remove_error(selector, error_id){
    $(selector).removeClass('is-invalid').addClass('is-valid');
    $(`#${error_id}`).remove();
}

$(document).ready(function () {
    $(username).keyup(function (e) { 
        $.ajax({
            url: validate_username_url,
            data: $(this).serialize(),
            error: function (response) {
            },
            success: function (response) {
                if (response.is_username_taken){
                    add_error(username, 'usernameError', 'Это имя пользователя занято!')
                } else {
                    remove_error(username, 'usernameError')
                }
            }
        });
    });
    $(email).keyup(function (e) { 
        $.ajax({
            url: validate_email_url,
            data: $(this).serialize(),
            error: function (response) {
            },
            success: function (response) {
                if (response.is_email_taken){
                    add_error(email, 'emailError', 'Этот e-mail занят!')
                } else {
                    remove_error(email, 'emailError')
                }
            }
        });
    });
    return false
});