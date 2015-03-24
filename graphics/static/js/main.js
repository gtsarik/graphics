var chart;
var chartData = [];


AmCharts.ready(function () {
    var box = $('#chartdiv');
    var indicator = $('#ajax-progress-indicator');

    $.ajax({
      'type': 'POST',
      'async': true,
      'dataType': 'json',
      'data': {
        'group_id': box.data('group-id'),
        'param_id': box.data('param-id'),
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      'beforeSend': function(xhr, settings){
        indicator.show();
      },
      'error': function(xhr, status, error){
        alert(error);
        indicator.hide();
      },
      'success': function(data, status, xhr){
        chartData = data['data'];
        indicator.hide();

        // SERIAL CHART
        chart = new AmCharts.AmSerialChart();
        chart.dataProvider = JSON.parse(chartData);
        chart.categoryField = "parameter";
        chart.startDuration = 1;

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
        graph.valueField = "value";
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
      }
    });
});


function initGroupSelector() {
    // look up select element with groups and attach our even handler
    // on field "change" event
    $('#group-selector select').change(function(event) {
        // get value of currently selected group option
        var group = $(this).val();

        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
            $.removeCookie('current_param', {'path': '/'});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', {'path': '/'});
            $.removeCookie('current_param', {'path': '/'});
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

$(document).ready(function(){
    initGroupSelector();
    initParamSelector();
});
