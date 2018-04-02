function init() {
  var data = [
    {
      values: [2558, 2356, 2199, 2099, 2061, 2024, 2020, 1999, 1954, 1942],
      labels: ['Russell Westbrook', 'James Harden','Isaiah Thomas','Anthony Davis', 'Karl-Anthony Towns', 'Damian Lillard', 'DeMar DeRozan','Stephen Curry', 'LeBron James', 'DeMarcus Cousins'],
      type: 'pie',
    },
  ];

  var layout = {
    height: 600,
    width: 800,
  };

  Plotly.plot('pie', data, layout);
}

function updatePlotly(newdata) {
  var PIE = document.getElementById('pie');
  Plotly.restyle(PIE, 'values', [newdata]);
}

function getData(dataset) {
  var data = [];
  switch (dataset) {
    case 'dataset1':
      data = [2558, 2356, 2199, 2099, 2061, 2024, 2020, 1999, 1954, 1942];
      break;
    case 'dataset2':
      data = [840, 907, 448, 157, 220, 440, 290, 524, 646, 332];
      break;
    case 'dataset3':
      data = [864, 659, 205, 884, 1007, 368, 386, 353, 639, 794];
      break;
    case 'dataset4':
      data = [31, 38, 13, 167, 103, 20, 13, 17, 44, 93];
      break;
    case 'dataset5':
      data = [132, 121, 70, 94, 56, 68, 78, 142, 92, 100];
      break;
    case 'dataset6':
      data = [438, 464, 210, 181, 212, 197, 180, 239, 303, 269];
      break;
    default:
      data = [30, 30, 30, 11];
  }
  updatePlotly(data);
}

init();

// Sort the data array using the greekSearchResults value
data.sort(function(a, b) {
  return b.wins - a.wins;
});

console.log(data);

// Slice the first 10 objects for plotting
data = data.slice(0, 10);

// Reverse the array due to Plotly's defaults
data = data.reverse();

// Trace1 for the Greek Data
var trace1 = {
  x: data.map(row => row.wins),
  y: data.map(row => row.team),
  text: data.map(row => row.team),
  name: 'NBA',
  type: 'bar',
  orientation: 'h',
};

// data
var data = [trace1];

// Apply the group bar mode to the layout
var layout = {
  title: 'Wins by Team',
  margin: {
    l: 100,
    r: 100,
    t: 100,
    b: 100,
  },
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot('plot', data, layout);