// Add this code to load JQuery first
// (function () {
//     // Load the script
//     var script = document.createElement("SCRIPT");
//     script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
//     script.type = 'text/javascript';
//     script.onload = function () {
//         var $ = window.jQuery;
//         // Use $ here...
//     };
//     document.getElementsByTagName("head")[0].appendChild(script);
// })();


var PAGE_START = 2;
var PAGE_END = 10;

var resultArray = [];

// Never name a important global variable as i. Because the page may use that and change the value unexpectedly.
// var i = PAGE_START;

var superIndex = PAGE_START;

var timeInterval;
timeInterval = setInterval(function () {

    console.log("Run into Interval");
    if (superIndex <= PAGE_END) {

        // Call to load page.
        loadPage(superIndex);

        // Next page
        superIndex = superIndex + 1;
    } else {
        clearInterval(timeInterval);
    }
}, 1000);

function loadPage(index) {

    var currentUrl = 'quan-hai-ba-trung?p=' + index;
    var currentId = index;

    $.ajax({
        url: currentUrl,
        success: onResult
    });

    function onResult(result) {

        console.log('The Result index: ' + currentId);

        var doc = $(result);

        var stockArrDom = doc.find('h4 a');

        console.log(stockArrDom.length);

        //Iterate all td's in second column
        stockArrDom.each(function () {
            //add item to array
            resultArray.push($(this).text());
        });
    }
}
JSON.stringify(resultArray)