$(document).ready(function() {
    var cn_name;
    var compnode_class = "compnode";

    var disk_server_name;
    var disk_server_class = "disk-server";

    var dg_name;
    var dg_class = "data-gen";

    var switch_name;
    var sw_class = "switch";

    var robotic = "rl";
    var robotic_class = "robotic";

    $(".button-cn").click(function() {
        var model_name = $(".model-name").text();
        cn_name = $("#cn_name").val();
        var ncpu = $("#qp").val();
        var cpu_speed = $("#mp").val();
        var avr_data_value = $("#dv").val();

        $.ajax({
            type: "POST",
            url: "/create_comp_node/",
            data: {
                "cn_name": cn_name,
                "model_name":model_name,
                "ncpu": ncpu,
                "cpu_speed": cpu_speed,
                "avr_data_value": avr_data_value
            },
            success: function(data) {
                if (data) {
                    console.log(data);
                    $('.add-device__compnode__button').prop('disabled', false);
                    AddDeviceInSelect(cn_name);
                    $('.text-success').removeClass('hidden');
                    setTimeout(function(){
                      $('.text-success').addClass('hidden');
                    }, 5000);
                }
            }
        })
    })


    $(".button-ds").click(function() {
    var model_name = $(".model-name").text();
    disk_server_name = $("#disk_server_name").val();
    var disk_pool_size = $("#pool-size").val();

    $.ajax({
        type: "POST",
        url: "/create_disk_server/",
        data: {
            "model_name":model_name,
            "disk_server_name": disk_server_name,
            "disk_pool_size":disk_pool_size,
        },
        success: function(data) {
            if (data) {
                console.log(data);
                $('.add-device__diskserver__button').prop('disabled', false);
                AddDeviceInSelect(disk_server_name);
            }
        }
    })
    })


     $(".button-dg").click(function() {
        var model_name = $(".model-name").text();
        dg_name = $("#data_gen_name").val();
        var freq_data = $("#fd").val();
        var data_value = $("#vd").val();

        $.ajax({
            type: "POST",
            url: "/create_data_gen/",
            data: {
                "dg_name": dg_name,
                "model_name":model_name,
                "freq_data": freq_data,
                "data_value": data_value,
            },
            success: function(data) {
                if (data) {
                    console.log(data)
                    $('.add-device__datagen__button').prop('disabled', false);
                    AddDeviceInSelect(dg_name);
                    $('.text-success').removeClass('hidden');
                    setTimeout(function(){
                      $('.text-success').addClass('hidden');
                    }, 5000);

                }
            }
        })
    })

    $(".button-sw").click(function() {
    var model_name = $(".model-name").text();
    switch_name = $("#sw_name").val();
    var sw_capacity = $("#capacity").val();

    $.ajax({
        type: "POST",
        url: "/create_switch/",
        data: {
            "model_name":model_name,
            "switch_name": switch_name,
            "sw_capacity":sw_capacity,
        },
        success: function(data) {
            if (data) {
                console.log(data);
                $('.add-device__switch__button').prop('disabled', false);
                AddDeviceInSelect(switch_name);
            }
        }
    })
    })


    container= document.getElementById('cy');
    var cy = cytoscape({
    container: document.getElementById('cy'),
    elements: [ /*
      // flat array of nodes and edges
        { // node dg
          group: 'nodes',
          data: {  id: 'dg' },
          position: { x: 50, y: 0 },
          selected: false, // whether the element is selected (default false)
          selectable: true, // whether the selection state is mutable (default true)
          locked: false, // when locked a node's position is immutable (default false)
          grabbable: true, // whether the node can be grabbed and moved by the user
        },

        { // node sw0
          data: { id: 'sw0' },
          position: { x: -200, y: 200 } // can alternatively specify position in rendered on-screen pixels
        },

        { // node sw1
          data: { id: 'sw1' },
          position: { x: 300, y: 200 }
        },

         { // node sw2
          data: { id: 'sw2' },
          position: { x: -450, y: 400 }
        },

        { // node sw3
          data: { id: 'sw3' },
          position: { x: -200, y: 450 } // can alternatively specify position in rendered on-screen pixels
        },

         { // node sw4
          data: { id: 'sw4' },
          position: { x: 150, y: 400 } // can alternatively specify position in rendered on-screen pixels
        },

        { // node cn1
          data: { id: 'cn1' },
          position: { x: 250, y: 600 } // can alternatively specify position in rendered on-screen pixels
        },

        { // node cn2
          data: { id: 'cn2' },
          position: { x: 550, y: 500 } // can alternatively specify position in rendered on-screen pixels
        },

        { // node ds1
          data: { id: 'ds1' },
          position: { x: -550, y: 500 } // can alternatively specify position in rendered on-screen pixels
        },

        { // node ds2
          data: { id: 'ds2' },
          position: { x: -350, y: 600 } // can alternatively specify position in rendered on-screen pixels
        },


        { // edge e1
          group: 'edges',
          data: {
            id: 'e1',
            // inferred as an edge because `source` and `target` are specified:
            source: 'dg', // the source node id (edge comes from this node)
            target: 'sw0'  // the target node id (edge goes to this node)
            // (`source` and `target` can be effectively changed by `eles.move()`)
          }
        }
      */],

      layout: {
        name: 'preset',
      },
      wheelSensitivity: 0.2,

      // so we can see the ids
      style: cytoscape.stylesheet()
        .selector('node')
          .style({
            'content': 'data(id)',
            'shape': 'circle',
            'width': '80px',
            'height': '80px',
            'background-opacity': '0',
          })
        .selector('edges')
          .style({
            'label': 'data(label)',
            'text-margin-y': '15px'
          })
        .selector('.data-gen')
          .style({
            'content': 'data(id)',
            'shape': 'rectangle',
            'width': '100px',
            'height': '130px',
            'background-image': '/static/symsim/img/device/generator-1.png',
          })
          .selector('.switch')
          .style({
            'content': 'data(id)',
            'shape': 'rectangle',
            'width': '140px',
            'height': '80px',
            'background-image': '/static/symsim/img/device/NetworkSwitch.png',
          })
          .selector('.disk-server')
          .style({
            'content': 'data(id)',
            'shape': 'rectangle',
            'width': '80px',
            'height': '130px',
            'background-image': '/static/symsim/img/device/disk-server1.png',
          })
           .selector('.compnode')
          .style({
            'content': 'data(id)',
            'shape': 'rectangle',
            'width': '80px',
            'height': '130px',
            'background-image': '/static/symsim/img/device/compnode.png',
          })
        .selector('.robotic')
          .style({
            'content': 'data(id)',
            'shape': 'rectangle',
            'width': '100px',
            'height': '130px',
            'background-image': '/static/symsim/img/device/robothand1.png',
          })
    });


    cy.zoom({
      level: 0.6, // the zoom level
      renderedPosition: { x:500, y: 0 }
    });


    //var canvas1 = document.querySelector('canvas[data-id="layer2-node"]');
    //var canvas2 = document.querySelector('canvas[data-id="layer2-node"]');
    //var canvas3 = document.querySelector('canvas[data-id="layer2-node"]');


    function NewNode(name, class_name) {
      var elem= cy.add([
        { group: 'nodes', data: { id: name }, classes: [ class_name ], position: { x: 100, y: 100 } },
      ]);
    }

    $(".add-device__compnode__button").click(function() {
        NewNode(cn_name, compnode_class );
    })

    $(".add-device__diskserver__button").click(function() {
        NewNode(disk_server_name, disk_server_class );
    })

    $(".add-device__datagen__button").click(function() {
        NewNode(dg_name, dg_class );
    })

    $(".add-device__switch__button").click(function() {
        NewNode(switch_name, sw_class );
    })

    $(".open-form-robotic").click(function() {
        NewNode(robotic, robotic_class );
    })





    function AddDeviceInSelect(device) {
        $('.device-list').append($('<option>', {
            value: device,
            text: device
        }));
    }

    function AddEdge(from, to, capacity) {
            var eles = cy.add([
            { group: 'edges', data: { id: from+"_"+to, source: from, target: to, label: capacity+"Мб/с" } }
            ]);
       }

    $(".add-edge__button").click(function() {
        var elem_from = $(".device-list.source").val();
        var elem_to = $(".device-list.target").val();
        var capacity_edge = $(".capacity-edge").val();
        console.log(elem_from, elem_to);
        AddEdge(elem_from, elem_to, capacity_edge);
    })
});