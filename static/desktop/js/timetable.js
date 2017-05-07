jQuery(document).ready(function ($) {
    console.log('ready');
    // run test on initial page load
    testSize(this);

    // run test on resize of the window
    $(window).resize(testSize(this));
    // enableEvent();
    lessonEvent();
    function testSize(elm) {
        if (main.checkSize(elm) == true) {
            setHeight();
        }
        else {
            enableEvent();
        }
    }

    function setHeight() {
        for (var i = 1; i <= 4; i++) {
            main.getHeight(".lesson-" + i)
        }
    }

    function enableEvent() {
        $("[class^=h-table-]").click(function (e) {
            $('[class^=t-table-]').addClass('hidden-sm-down');
            $('.t-table-' + $(this).data('day')).removeClass('hidden-sm-down');
            e.preventDefault();
        });
    }

    function lessonEvent() {
        $('.t_break').click(function (e) {
            var myFile= $(this).data('break');
            myFile['page'] = "day";
            // console.log(htmlPage);
            $.post("/partials/",
                JSON.stringify({data: myFile}),
                function (data) {
                    $("#content").html(data['page']);
                },
                "json");
            e.preventDefault();
        });
    }
});