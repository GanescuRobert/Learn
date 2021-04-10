'use strict';

var canvas = d3.select("#graphBoard"),
    width = canvas.attr("width"),
    height = canvas.attr("height");

var fill = d3.scale.category20();

var force = d3.layout.force()
    .size([width, height])
    .nodes([]) // initialize with a single node
    .linkDistance(200)
    .charge(-300)
    .on("tick", tick);

var svg = d3.select("#graphBoard").append("svg")
    .attr("width", width)
    .attr("height", height);


var nodes = force.nodes(),
    links = force.links(),
    node = svg.selectAll(".node"),
    link = svg.selectAll(".link"),
    text = svg.selectAll(".text");


restart();

function get_node(name) {
    for (let node_item of nodes)
        if (node_item.name === name) {
            return node_item;
        }
    return false;
}

function createLinkClick() {
    let source_name = document.getElementById("newSource").value,
        target_name = document.getElementById("newTarget").value;

    let source_node = get_node(source_name),
        target_node = get_node(target_name);

    if (source_node && target_node) {
        let item = {
            source: source_node,
            target: target_node
        }
        if (links.some(temp => (temp.source === source_node && temp.target === target_node)) ||
            links.some(temp => (temp.source === target_node && temp.target === source_node))) {
            alert("Object found inside the array.");
        } else {
            links.push(item);
            document.getElementById("newSource").value = "";
            document.getElementById("newTarget").value = "";
        }
        restart();
    } else {
        alert("The node does not exist");
    }
}

function removeLinkClick() {
    let source_name = document.getElementById("removeSource").value,
        target_name = document.getElementById("removeTarget").value;
    let source_node = get_node(source_name),
        target_node = get_node(target_name);

    if (source_node && target_node) {
        let item = {
            source: source_node,
            target: target_node
        }
        if (links.some(temp => (temp.source === source_node && temp.target === target_node))) {
            links.splice(links.indexOf(item), 1);
            document.getElementById("removeSource").value = "";
            document.getElementById("removeTarget").value = "";
        } else {
            alert("Object not found inside the array.");
        }
        restart();
    } else {
        alert("The node does not exist");
    }
}

function createNodeClick() {
    let node_name = document.getElementById("newNodeName").value;
    if (nodes.some(temp => temp.name === node_name)) {
        alert("Object found inside the array.");
    } else {
        const x_center = 350,
            y_center = 350;

        let add_x = Math.random() * width - x_center,
            add_y = Math.random() * height - y_center;

        let node_item = {
            name: node_name,
            x: x_center + add_x,
            y: y_center + add_y
        };

        nodes.push(node_item);
        document.getElementById("newNodeName").value = "";

    }
    restart();
}

function removeNodeClick() {
    let node_name = document.getElementById("removeNodeName").value;
    let node_item = get_node(node_name);
    if (nodes.some(temp => temp === node_item)) {
        nodes.splice(nodes.indexOf(node), 1);
        links = links.filter(function(l) {
            return l.source !== node_item && l.target !== node_item;
        });
        document.getElementById("removeNodeName").value = "";
    } else {
        alert("Object not found.");
    }
    restart();
}

function tick() {
    link.attr("x1", function(d) {
            return d.source.x;
        })
        .attr("y1", function(d) {
            return d.source.y;
        })
        .attr("x2", function(d) {
            return d.target.x;
        })
        .attr("y2", function(d) {
            return d.target.y;
        });

    node.attr("cx", function(d) {
            return d.x;
        })
        .attr("cy", function(d) {
            return d.y;
        });
    text.attr("x", function(d) {
            return d.x - 8;
        })
        .attr("y", function(d) {
            return d.y + 10;
        });
}

function restart() {

    node = node.data(nodes);
    node.enter().insert("circle")
        .attr("class", "node")
        .attr("stroke", "black")
        .attr("fill", "white")
        .attr("r", 25)
    node.exit().remove();

    text = text.data(nodes);
    text.enter().insert("text")
        .attr("class", "text")
        .attr("fill", "black")
        .attr("font-size", "30px")
        .text(function(d) { return d.name; })
    text.exit().remove();

    link = link.data(links);
    link.enter().insert("line", ".node")
        .attr("class", "link")
        .attr("stroke", "#000");
    link.exit().remove();

    force.start();
}