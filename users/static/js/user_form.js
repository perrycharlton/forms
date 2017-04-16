jQuery(document).ready(function ($) {
    console.log('ready');

    function submit_event() {
        $('.contact_btn').click(function (e) {
            var contact_data = {};
            $('input').each(function(){
                contact_data[$(this).attr('name')] = $(this).val();
            });

            $.post("/partials/",
                JSON.stringify({page: 'contact_form', data: contact_data}),
                function (data) {
                    $("#content").html(data['page']);
                },
                "json");


            e.preventDefault();
            // console.log(contact_data);
            return contact_data;
        });

    }


    submit_event();

    $("[class^=h-table-]").click(function (e) {
        $('[class^=t-table-]').addClass('hidden-sm-down');

        $('.t-table-' + $(this).data('day')).removeClass('hidden-sm-down');
        e.preventDefault();
    });
});