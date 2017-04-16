jQuery(document).ready(function ($) {
    console.log('ready');
    // var num = $('.team_retails').size();
    submit_event();

    // main.getHeight(".teamImage");
    $("[class^=h-table-]").click(function (e) {
        $('[class^=t-table-]').addClass('hidden-sm-down');

        $('.t-table-' + $(this).data('day')).removeClass('hidden-sm-down');
        e.preventDefault();
    });

    function submit_event() {
        $('button').click(function (e) {
            var my_radio = $(this).data('user');
            var username = my_radio.split(" ")[0];
            console.log(my_radio, username);
            post_data(my_radio).done(function (msg) {
                console.log(msg['msg'])
            });

            e.preventDefault();
        });
    }

    function post_data(data) {
        var contact_data = $.post("/password/",
            JSON.stringify({data: data}),
            function (data) {
                // console.log(data);
                return data;
            },
            "json");
        return contact_data;
    }


});