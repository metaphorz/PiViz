// Generate Pi digits
function generatePiDigits(numDigits) {
    let q = 1n, r = 0n, t = 1n, k = 1n, n = 3n, l = 3n;
    let digits = [];
    while (digits.length < numDigits) {
        if (4n * q + r - t < n * t) {
            digits.push(Number(n));
            q = 10n * q;
            r = 10n * (r - n * t);
            n = (10n * (3n * q + r)) / t - 10n * n;
        } else {
            q = q * k;
            r = (2n * q + r) * l;
            t = t * l;
            k = k + 1n;
            n = (q * (7n * k + 2n) + r * l) / (t * l);
            l = l + 2n;
        }
    }
    return digits;
}

// Set up the SVG
const width = 800;
const height = 800;
const svg = d3.select("#piSpiral")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

// Generate 1000 digits of Pi
const piDigits = generatePiDigits(1000);

// Set up the spiral
const centerX = width / 2;
const centerY = height / 2;
const maxRadius = Math.min(width, height) / 2 - 10;
const spiralConstant = 0.1;

// Colors for digits 0-9
const colors = [
    "#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF",
    "#4B0082", "#8F00FF", "#FFC0CB", "#FFFFFF", "#808080"
];

// Highlight color for the start of Pi
const highlightColor = "#FF00FF";

// Create tooltip
const tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

// Draw the spiral
svg.selectAll("circle")
    .data(piDigits)
    .enter()
    .append("circle")
    .attr("cx", (d, i) => {
        const angle = i * spiralConstant;
        const radius = maxRadius * (1 - i / 1000);
        return centerX + radius * Math.cos(angle);
    })
    .attr("cy", (d, i) => {
        const angle = i * spiralConstant;
        const radius = maxRadius * (1 - i / 1000);
        return centerY + radius * Math.sin(angle);
    })
    .attr("r", (d, i) => 5 * (1 - i / 1000) + 1)
    .attr("fill", (d, i) => i === 1 ? highlightColor : colors[d])
    .on("mouseover", function(event, d) {
        d3.select(this).attr("stroke", "white").attr("stroke-width", 2);
        tooltip.transition()
            .duration(200)
            .style("opacity", .9);
        tooltip.html(d)
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 28) + "px");
    })
    .on("mouseout", function() {
        d3.select(this).attr("stroke", null);
        tooltip.transition()
            .duration(500)
            .style("opacity", 0);
    });
