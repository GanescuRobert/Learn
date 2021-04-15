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
    .gravity(0.005)
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

function search_link(item) {
    for (let i = 0; i < links.length; i++) {
        if ((links[i].source === item.source && links[i].target == item.target) ||
            (links[i].source === item.target && links[i].target == item.source)) {
            return i;
        }
    }
    return -1;
}

function search_node(item) {
    for (let i = 0; i < nodes.length; i++) {
        if (nodes[i].name === item.name) {
            return i;
        }
    }
    return -1;
}

function get_node(name) {
    for (let node_item of nodes)
        if (node_item.name === name) {
            return node_item;
        }
    return null;
}

function createLinkClick() {
    let source_name = document.getElementById("newSource").value,
        target_name = document.getElementById("newTarget").value;

    if (source_name === "" || target_name === "") {
        alert("Empty cell.");
    } else {
        let source_node = get_node(source_name),
            target_node = get_node(target_name);
        if (source_node === null || target_node === null) {
            alert("Node not found inside the array.");
        } else {
            let item = {
                source: source_node,
                target: target_node
            }
            let position = search_link(item);
            if (position !== -1) {
                alert("Link found inside the array.");
            } else {
                links.push(item);

                restart();
                redraw();
            }
        }
    }
    document.getElementById("newSource").value = "";
    document.getElementById("newTarget").value = "";
}

function removeLinkClick() {
    let source_name = document.getElementById("removeSource").value,
        target_name = document.getElementById("removeTarget").value;

    if (source_name === "" || target_name === "") {
        alert("Empty cell.");
    } else {
        let source_node = get_node(source_name),
            target_node = get_node(target_name);
        if (source_node === null || target_node === null) {
            alert("Node not found inside the array.");
        } else {
            let item = {
                source: source_node,
                target: target_node
            }
            let position = search_link(item);
            if (position !== -1) {
                links.splice(position, 1);
                document.getElementById("removeSource").value = "";
                document.getElementById("removeTarget").value = "";
                restart();
                redraw();
            } else {
                alert("The link does not exist.");
            }
        }
    }
    document.getElementById("removeSource").value = "";
    document.getElementById("removeTarget").value = "";
}

function editLinkClick() {
    let current_node_1 = document.getElementById("editLink1Current").value,
        current_node_2 = document.getElementById("editLink2Current").value,
        future_node_1 = document.getElementById("editLink1Future").value,
        future_node_2 = document.getElementById("editLink2Future").value;

    if (current_node_1 === "" || current_node_2 === "" ||
        future_node_1 === "" || future_node_2 === "") {
        alert("Empty cell.");
    } else {
        let cn1 = get_node(current_node_1),
            cn2 = get_node(current_node_2),
            fn1 = get_node(future_node_1),
            fn2 = get_node(future_node_2);

        if (cn1 === null || cn2 === null || fn1 === null || fn2 === null) {
            alert("Node not found inside the array.");
        } else {
            let itemC = {
                    source: cn1,
                    target: cn2
                },
                itemF = {
                    source: fn1,
                    target: fn2
                }
            let positionC = search_link(itemC),
                positionF = search_link(itemF);
            if (positionC !== -1 && positionF === -1) {
                links.splice(positionC, 1);
                links.push({
                    source: fn1,
                    target: fn2
                });
                restart();
                redraw();
            } else {
                alert("Current link not exist or future link exist.");
            }
        }
    }
    document.getElementById("editLink1Current").value = "";
    document.getElementById("editLink2Current").value = "";
    document.getElementById("editLink1Future").value = "";
    document.getElementById("editLink2Future").value = "";
}

function createNodeClick() {
    let node_name = document.getElementById("newNodeName").value;

    if (node_name === "") {
        alert("Empty cell.");
    } else {
        if (get_node(node_name) !== null) {
            alert("Node found inside the array.");
        } else {
            const x_center = 350,
                y_center = 350;

            let add_x = Math.random() * width - x_center,
                add_y = Math.random() * height - y_center;

            let item = {
                name: node_name,
                x: x_center + add_x,
                y: y_center + add_y
            };

            nodes.push(item);

            restart();
            redraw();

        }
    }
    document.getElementById("newNodeName").value = "";
}

function removeNodeClick() {
    let node_name = document.getElementById("removeNodeName").value;
    if (node_name === "") {
        alert("Empty cell.");
    } else {
        let node_item = get_node(node_name);
        if (node_item === null) {
            alert("Object not found.");
        } else {
            let position = search_node(node_item);
            nodes.splice(position, 1);
            links = links.filter(function(l) {
                return l.source !== node_item && l.target !== node_item;
            });
            restart();
            redraw();
        }
    }
    document.getElementById("removeNodeName").value = "";
}



function editNodeClick() {
    let node_name_current = document.getElementById("editCurrent").value;
    let node_name_future = document.getElementById("editFuture").value;
    if (node_name_current === "" || node_name_future === "") {
        alert("Empty cell.");
    } else
    if (nodes.some(temp => temp === get_node(node_name_future))) {
        alert("Future name used. Try another name.");
    } else {
        let node_item = get_node(node_name_current);
        if (nodes.some(temp => temp === node_item)) {
            nodes[nodes.indexOf(node_item)].name = node_name_future;
            restart();
            redraw();
        } else
            alert("Current name not found.");
    }
    document.getElementById("editCurrent").value = "";
    document.getElementById("editFuture").value = "";
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

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    text.attr("transform", function(d) {
        return "translate(" + (d.x - 7) + "," + (d.y + 7) + ")";
    });
}

function restart() {

    node = node.data(nodes);
    node.enter().insert("circle")
        .attr("class", "node")
        .attr("stroke", "black")
        .attr("fill", "white")
        .attr("r", 30)
        .call(force.drag);

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

function redrawTexts() {
    text.data(nodes)
        .text(function(d) { return d.name })
}

function redrawLinks() {
    link.data(links)
}

function redrawNodes() {
    node.data(nodes)
}

function redraw() {
    redrawTexts();
    redrawLinks();
    redrawNodes();
}