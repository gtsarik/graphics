var chart;
var chartData = [];

AmCharts.ready(function () {
    // generate some data first
    // generateChartData();

    // SERIAL CHART
    chart = new AmCharts.AmSerialChart();
    chart.dataProvider = chartData;
    chart.categoryField = "country";
    chart.startDuration = 1;

    chart.dataProvider = chartData;
    chart.categoryField = "date";
    chart.dataDateFormat = "YYYY-MM-DD";

    // AXES
    // category
    var categoryAxis = chart.categoryAxis;
    categoryAxis.labelRotation = 90;
    categoryAxis.gridPosition = "start";

    // value
    // in case you don't want to change default settings of value axis,
    // you don't need to create it, as one value axis is created automatically.

    // GRAPH
    var graph = new AmCharts.AmGraph();
    graph.valueField = "visits";
    graph.balloonText = "[[category]]: <b>[[value]]</b>";
    graph.type = "column";
    graph.lineAlpha = 0;
    graph.fillAlphas = 0.8;
    chart.addGraph(graph);

    // CURSOR
    var chartCursor = new AmCharts.ChartCursor();
    chartCursor.cursorAlpha = 0;
    chartCursor.zoomable = false;
    chartCursor.categoryBalloonEnabled = false;
    chart.addChartCursor(chartCursor);

    chart.creditsPosition = "top-right";

    chart.write("chartdiv");
    var file_name = $.cookie('current_param');

    if ( file_name !== undefined) {
        file_name += ".csv"
        alert(file_name);
        // loadCSV(file_name);
        loadCSV("static/json/11CuNPefD.csv");
    }

    // loadCSV("static/json/11CuNPefD.csv");

});

function loadCSV(file) {
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari
        var request = new XMLHttpRequest();
    } else {
        // code for IE6, IE5
        var request = new ActiveXObject('Microsoft.XMLHTTP');
    }
    // load
    request.open('GET', file, false);
    request.send();
    parseCSV(request.responseText);
}

function parseCSV(data) {
    //replace UNIX new lines
    data = data.replace(/\r\n/g, "\n");
    
    //replace MAC new lines
    data = data.replace(/\r/g, "\n");

    //split into rows
    var rows = data.split("\n");

    // loop through all rows
    for (var i = 0; i < rows.length; i++) {
        // this line helps to skip empty rows
        if (rows[i]) {
            // our columns are separated by comma
            var column = rows[i].split(",");
            // alert(column);
            // column is array now
            // first item is date
            var date = column[1];

            // second item is value of the second column
            var value = column[2];

            // alert('date === ', date);
            // alert('value === ', value);
            
            // create object which contains all these items:
            var dataObject = {
                date: date,
                visits: value
            };

        // add object to chartData array
        chartData.push(dataObject);
        }
    }
    chart.validateData();
}


function initGroupSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#group-selector select').change(function(event) {
        // get value of currently selected group option
        var group = $(this).val();
        // alert(group);
        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
            $.removeCookie('current_param', {'path': '/'});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', {'path': '/'});
        }
        
        // and reload a page
        location.reload(true);
        return true;
    });
}

function initParamSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#param-selector select').change(function(event) {
        // get value of currently selected param option
        var param = $(this).val();
        // alert(param);
        if (param) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_param', param, {'path': '/', 'expires': 365});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_param', {'path': '/'});
        }
        
        // and reload a page
        location.reload(true);
        return true;
    });
}

function initData() {
    alert("data");
    var article = document.querySelector('#chartdiv'),
              data = article.parameter;
        
        alert(data);
}

function showDetails() {
    alert("data");
    info = $('#chartdiv').data('parameter');
    // for (var i=0; i < info.length; i++ ) {
    //     alert(info[i]);
    // }
    alert(info);
    
}




$(document).ready(function(){
    initGroupSelector();
    initParamSelector();
    showDetails();
});
