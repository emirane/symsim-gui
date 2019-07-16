$(document).ready(function() {
$("#myChart")
var sw0 = 110;
var sw1 = 102;
var sw2 = 108;
var sw3 = 112;
var dc_core = 109;
var operation = 33;
var simid = 2;

    $(".btn-graph").click(function(){
    canvas = document.getElementById("myChart");
    var ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var sys_time= new Array();
    var jsDoub = new Array();
    var jsDoub2 = new Array();
    var jsDoub3 = new Array();
    var jsDoub4 = new Array();
    var jsDoub5 = new Array();
        $.ajax({
            type: "POST",
            url: "/graphics-data/",
            data: {
                'sw0': sw0,
                'sw1': sw1,
                'sw2': sw2,
                'sw3': sw3,
                'dc_core': dc_core,
                'operation': operation,
                'simid': simid,
            },
            success: function(data) {
                if (data) {
                //console.log(data)
                for (i = 0;i< data.sim_rep1.length;i++){
                    sys_time.push((data.sim_rep1[i][0]/3600).toFixed(2));
                    jsDoub.push(data.sim_rep1[i][1])
                }
                for (i = 0;i< data.sim_rep2.length;i++){
                    jsDoub2.push(data.sim_rep2[i][0])
                }
                for (i = 0;i< data.sim_rep3.length;i++){
                    jsDoub3.push(data.sim_rep3[i][0])
                }
                for (i = 0;i< data.sim_rep4.length;i++){
                    jsDoub4.push(data.sim_rep4[i][0])
                }
                for (i = 0;i< data.sim_rep5.length;i++){
                    jsDoub5.push(data.sim_rep5[i][0])
                }
                new Chart(document.getElementById("myChart"), {
                    type: 'line',
                    data: {
                    labels: sys_time,
                    datasets: [{
                    data: jsDoub,
                    label: "Sw_0",
                    borderColor: "#3e95cd",
                    fill: false,

                    }, {
                    data: jsDoub2,
                    label: "Sw_1",
                    borderColor: "#8e5ea2",
                    fill: false
                    }, {
                    data: jsDoub3,
                    label: "Sw_2",
                    borderColor: "#3cba9f",
                    fill: false
                    } , {
                    data: jsDoub4,
                    label: "Sw_2",
                    borderColor: "yellow",
                    fill: false
                    } , {
                    data: jsDoub5,
                    label: "DC Core",
                    borderColor: "blue",
                    fill: false
                    }
                    ]
                    },
                    options: {
                    maintainAspectRatio: true,
                    responsive: false,
                    title: {
                    maintainAspectRatio: true,
                    responsive: false,
                    display: true,
                    text: 'Switch load'
                    },
                    scales: {
                        yAxes: [{
                          scaleLabel: {
                            display: true,
                            labelString: 'Нагрузка (Мб/c)',
                            fontSize: 18,
                          },

                        }],
                      xAxes: [{
                       ticks: {
                          beginAtZero: true,
                          maxTicksLimit: 24,
                          callback: function(value) {if (value % 1 === 0) {return value;}}
                        },
                      scaleLabel: {
                        display: true,
                        labelString: 'Время (ч)',
                        fontSize: 18,
                       }
                    }]
                    }
                }
            });
            }
                else
                    console.log("error")
                }
        })
    })

    $(".btn-graph2").click(function(){
    var sys_time= new Array()
    var jsDoub = new Array()
    var jsDoub2 = new Array()
        $.ajax({
            type: "POST",
            url: "/graphics-data2/",
            data: {},
            success: function(data) {
                if (data) {
                for (i = 0;i< data.sim_rep.length;i++){
                    sys_time.push((data.sim_rep[i][0]/3600).toFixed(2));
                    jsDoub.push(data.sim_rep[i][1])
                }
                for (i = 0;i< data.sim_rep2.length;i++){
                    jsDoub2.push(data.sim_rep2[i][0])
                }

                new Chart(document.getElementById("myChart"), {
                    type: 'line',
                    data: {
                    labels: sys_time,
                    datasets: [{
                    data: jsDoub,
                    label: "bb1",
                    borderColor: "#3e95cd",
                    fill: false,
                    pointRadius: 2,
                    borderWidtrh: 2
                    }, {
                    data: jsDoub2,
                    label: "bb2",
                    borderColor: "#8e5ea2",
                    fill: false,
                    pointRadius: 2,
                    borderWidtrh: 2
                    },/* {
                    data: jsDoub3,
                    label: "Sw_2",
                    borderColor: "#3cba9f",
                    fill: false
                    }
                    */
                    ]
                    },
                    options: {
                    maintainAspectRatio: true,
                    responsive: false,
                    title: {
                        maintainAspectRatio: true,
                        responsive: false,
                        display: true,
                        text: 'Свободные процессорные элементы',
                    },
                    scales: {
                        yAxes: [{
                          scaleLabel: {
                            display: true,
                            labelString: 'Количество свободных процессоров',
                            fontSize: 18,
                          }
                        }],
                      xAxes: [{
                      ticks: {
                          beginAtZero: true,
                          maxTicksLimit: 24,
                         // precision: 0.01,
                          callback: function(value) {if (value % 1 <= 0.3) {return value;}}
                        },
                      scaleLabel: {
                        display: true,
                        labelString: 'Время (ч)',
                        fontSize: 18,
                      }
                    }]
                    }
                }
            });
            }
                else
                    console.log("error")
                }
        })
    })


})

$(document).ready(function() {
    $(".text-info").click(function() {
            $(".list_user_model").toggleClass("hidden");
        });

     $(".open-list-device").click(function() {
            $(".side-bar").toggleClass("hidden");
     });

     $(".task-flow").click(function() {
            $(".parameters__forms.task").toggleClass("hidden");
     });
     $(".params-files").click(function() {
            $(".parameters__forms.files").toggleClass("hidden");
     });

    $(".start-params").click(function() {
            $(".parameters__forms.simulation").toggleClass("hidden");
     });






/*
    $(".create-model-name-button").on("click", function(){
        var name = $("#model_name").val();
        $.ajax({
            type: "POST",
            url: "/create_model_name/",
            data: { "name":name}

        })
    })
    */
})

function TabForm(elem_id) {
        switch (elem_id) {
            case 'gt-1':
                $(".gt-1").addClass("active").siblings().removeClass("active");
                $('.add-device.datagen').addClass("active").siblings().removeClass("active");
              break;
            case 'bb-1':
                $(".bb-1").addClass("active").siblings().removeClass("active");
                $('.add-device.compnode').addClass("active").siblings().removeClass("active");
              break;
            case 'rd':
                $(".rd").addClass("active").siblings().removeClass("active");
                $('.add-device.diskserver').addClass("active").siblings().removeClass("active");
              break;
            case 'sw':
                $(".sw").addClass("active").siblings().removeClass("active");
                $('.add-device.switch').addClass("active").siblings().removeClass("active");
              break;
    }
}
