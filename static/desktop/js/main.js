/**
 * Created by perry on 12/03/17.
 */
var csrf_token = "{{ csrf_token() }}";

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader('X-CSRFToken', csrf_token)
        }
    }
});


var main = (function () {

    // Function to the css rule
    var checkSize = function (elem) {
        if ($(elem).width() >= 980) {
            console.log($(elem).width());
            return true
        }
    };

    var getHeight = function (item) {
        var maxHeight = $(item).map(function () {
            console.log($(this).height());
            return $(this).height()
        }).get();
        $(item).height(Math.max.apply(null, maxHeight))
    };

    var first_upper = function (str) {
        return (str + '').toLowerCase().replace(/\b[a-z]/g, function ($1) {
            return $1.toUpperCase()
        })
    };

    var get_data = function (myFile) {
        return $.get('/' + myFile)
    };

    var post_data = function (myFile, data, csrf_token) {
        console.log(myFile, data);
        return $.ajax({
            type: "POST",
            url:'/' + myFile,
            data: data,
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                    xhr.setRequestHeader('X-CSRFToken', csrf_token)
                }
            }
        })

    };
    var post_json_data = function (myFile, data, csrf_token) {
        console.log(myFile, data);
        return $.ajax({
            type: "POST",
            url:'/' + myFile,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: data,
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                    xhr.setRequestHeader('X-CSRFToken', csrf_token)
                }
            }
        })

    };


    var dynamicSort = function (property) {
        var sortOrder = 1;
        if (property[0] === "-") {
            sortOrder = -1;
            property = property.substr(1);
        }
        return function (a, b) {
            var result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
            return result * sortOrder;
        }
    };


    var shuffle = function (array) {
        var currentIndex = array.length, temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
        }

        return array;
    };


    return {
        getHeight: getHeight,
        checkSize: checkSize,
        first_upper: first_upper,
        get_data: get_data,
        post_data: post_data,
        dynamicSort: dynamicSort,
        shuffle: shuffle,
        post_json_data: post_json_data
    }

})();





