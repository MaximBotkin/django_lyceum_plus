function makeIconActive(icon){
    icon.addClass('estimation-icon-active').removeClass('estimation-icon-disabled');
}

function makeIconDisabled(icon){
    icon.removeClass('estimation-icon-active').addClass('estimation-icon-disabled');
}

function like() {
    var like = $(this);
    var type = like.data('type');
    var pk = like.data('pk');
    var action = like.data('action');
    var dislike = like.parent().parent().find('.dislikes').find('[data-action="dislike"]');

    $.ajax({
        url: like_url,
        type: 'POST',
        data: { 'pk': pk },

        success: function (json) {
            makeIconDisabled(dislike)
            console.log(json.result)
            if (json.result){
                makeIconActive(like)
            } else {
                makeIconDisabled(like)
            }
            like.parent().find("[data-count='like']").text(json.like_count);
            dislike.parent().find("[data-count='dislike']").text(json.dislike_count);
        }
    });

    return false;
}

function dislike() {
    var dislike = $(this);
    var type = dislike.data('type');
    var pk = dislike.data('pk');
    var action = dislike.data('action');
    var like = dislike.parent().parent().find('.likes').find('[data-action="like"]');

    $.ajax({
        url: dislike_url,
        type: 'POST',
        data: { 'pk': pk },

        success: function (json) {
            makeIconDisabled(like)
            console.log(json.result)
            if (json.result){
                makeIconActive(dislike)
            } else {
                makeIconDisabled(dislike)
            }
            like.parent().find("[data-count='like']").text(json.like_count);
            dislike.parent().find("[data-count='dislike']").text(json.dislike_count);
        }
    });

    return false;
}

function checkEstimated(){
    pks = []
    $('.estimation').each((i, block) => {
        block = $(block)
        pks[pks.length] = block.find('.likes').find('svg').data('pk')
    });
    $.ajax({
        url: check_estimated_url,
        type: 'GET',
        data: { 'pks': pks },

        success: function (json) {
            result = json.result
            for (const key in result) {
                const val = result[key]
                if (val === -1){
                    makeIconActive($(`.dislikes svg`).filter(`[data-pk="${key}"]`))
                } else if (val === 1){
                    makeIconActive($(`.likes svg`).filter(`[data-pk="${key}"]`))
                }
            }
        }
    })
}

// Получение переменной cookie по имени
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Подключение обработчиков
$(document).ready(function () {
    $(function () {
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        checkEstimated()
    });
    $('[data-action="like"]').click(like);
    $('[data-action="dislike"]').click(dislike);
});
