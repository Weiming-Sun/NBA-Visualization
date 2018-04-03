//function optionChanged() 
//creating drop down
var $dataList = document.getElementById('selDataset');
url = "/yearandtype";
d3.json(url, function(error, response) {
    if (error) return console.log(error);

    //console.log(response)
    var items = response;
    for(var i = 0; i < items.length; i++){
      var $option =  document.createElement("option");
      $option.setAttribute("value", items[i]);
      $option.innerHTML = items[i];
      $dataList.appendChild($option);
    }
})


//Average salary for every age--  as the page loads
var $AvgSalaryAndAge = document.getElementById('AvgSalaryAndAge');
url = "/avgageandsalary";
d3.json(url, function(error, response) {
    if (error) return console.log(error);

    // Grab values from the response json object to build the plots
    //console.log(response);
    var age = [];
    var avgSalary = [];
    for (var key in response){
      age.push(key)
      avgSalary.push(response[key])
    }
    // console.log(age)
    // console.log(avgSalary)

      var trace1 = {
        type: 'scatter',
        mode: 'lines',
        //name: name,
        x: age,
        y: avgSalary,
        line: {
          color: '#17BECF',
        },
      };
      var data = [trace1];
      var layout = {
        title: "Average Salary earned over the years",
        xaxis: {title: 'AGE',
          autorange: true,
          showgrid: true,
          autotick: true,
          //type: Number
          //range: [age[0], age[-1]],
          //type: 'date',
          rangeslider: {},
        },
        yaxis: {title: 'AVG SALARY'
          //autorange: true,
          //type: 'linear',
        },
      };
      Plotly.newPlot('AvgSalaryAndAge', data, layout);
    })
  
    //Loading age distribution as page loads
var agedistribution = document.getElementById('agedistribution');
sampleUrl = "/ageDistribution";
d3.json(sampleUrl, function(error, response) {
    if (error) return console.log(error);

    // Grab values from the response json object to build the plots
    //console.log(response);
    var age = [];
    var numPlayers = [];
    for (var key in response){
      age.push(key)
      //console.log(key)
      //console.log(response[key].length)
      numPlayers.push(response[key].length)
    }
      var trace1 = {
        type: 'scatter',
        //mode: 'lines',
        //name: name,
        x: age,
        y: numPlayers,
        line: {
          color: '#17BECF',
        },
      };
      var data = [trace1];
      var layout = {
        title: "Age distribution: how many players at each age in a given year and game type",
        xaxis: {title: 'AGE',
          autorange: true,
          showgrid: true,
          autotick: true,
          //type: Number
          //range: [age[0], age[-1]],
          //type: 'date',
          //rangeslider: {},
        },
        yaxis: {title: 'Number of players at each age'
          //autorange: true,
          //type: 'linear',
        },
      };
      Plotly.newPlot('agedistribution', data, layout);
    })

    //Loading age and 3pointers
    var ageAndTop3Pts = document.getElementById('ageAndTop3Pts');
    sampleUrl = "/ageAndTop3Pts";
    d3.json(sampleUrl, function(error, response) {
        if (error) return console.log(error);
    
        // Grab values from the response json object to build the plots
        //console.log(response);
        var age = [];
        var topThreePM = [];
        for (var key in response){
          age.push(key)
          //console.log(key)
          //console.log(response[key])
          topThreePM.push(response[key])
        }
    
          var trace1 = {
            type: 'scatter',
            //mode: 'lines',
            //name: name,
            x: age,
            y: topThreePM,
            line: {
              color: '#17BECF',
            },
          };
          var data = [trace1];
          var layout = {
            title: "Highest 3PMs at any age in a given year and game type",
            xaxis: {title: 'AGE',
              autorange: true,
              showgrid: true,
              autotick: true,
              //type: Number
              //range: [age[0], age[-1]],
              //type: 'date',
              //rangeslider: {},
            },
            yaxis: {title: 'Highest 3PM at each of the age'
              //autorange: true,
              //type: 'linear',
            },
          };
          Plotly.newPlot('ageAndTop3Pts', data, layout);
        })

    //Loading age and top FGM
    var ageAndTopFGM = document.getElementById('ageAndTopFGM');
    sampleUrl = "/ageAndTopFGM";
    d3.json(sampleUrl, function(error, response) {
        if (error) return console.log(error);
    
        // Grab values from the response json object to build the plots
        //console.log(response);
        var age = [];
        var topFGM = [];
        for (var key in response){
          age.push(key)
          //console.log(key)
          //console.log(response[key])
          topFGM.push(response[key])
        }
    
          var trace1 = {
            type: 'scatter',
            //mode: 'lines',
            //name: name,
            x: age,
            y: topFGM,
            line: {
              color: '#17BECF',
            },
          };
          var data = [trace1];
          var layout = {
            title: "Highest FGMs at each of the age in a given year and game type",
            xaxis: {title: 'AGE',
              autorange: true,
              showgrid: true,
              autotick: true,
              //type: Number
              //range: [age[0], age[-1]],
              //type: 'date',
              //rangeslider: {},
            },
            yaxis: {title: 'Highest FGM at each age'
              //autorange: true,
              //type: 'linear',
            },
          };
          Plotly.newPlot('ageAndTopFGM', data, layout);
        })

//Loading age and top Percent winning
var ageandTopPWin = document.getElementById('ageandTopPWin');
sampleUrl = "/ageAndTopPWin";
d3.json(sampleUrl, function(error, response) {
    if (error) return console.log(error);

    // Grab values from the response json object to build the plots
    //console.log(response);
    var age = [];
    var topPWin = [];
    for (var key in response){
      age.push(key)
      //console.log(key)
      //console.log(response[key])
      topPWin.push(response[key])
    }

      var trace1 = {
        type: 'scatter',
        //mode: 'lines',
        //name: name,
        x: age,
        y: topPWin,
        line: {
          color: '#17BECF',
        },
      };
      var data = [trace1];
      var layout = {
        title: "Highest % winnning at each of the age in a given year and game type",
        xaxis: {title: 'AGE',
          autorange: true,
          showgrid: true,
          autotick: true,
          //type: Number
          //range: [age[0], age[-1]],
          //type: 'date',
          //rangeslider: {},
        },
        yaxis: {title: 'Highest % Wins at each age'
          //autorange: true,
          //type: 'linear',
        },
      };
      Plotly.newPlot('ageandTopPWin', data, layout);
    })

//getting new data based on the selection in drop down and update pie chart, bubble plot and metadata
function optionChanged(optionValue) {
    optionValue = optionValue.replace(/:/g, '/');
    newageDistributionUrl = "/ageDistribution/"+optionValue;
  
    d3.json(newageDistributionUrl, function(error, response) {
    if (error) return console.log(error);
    updateageDistribution(response);

    })

    newageAndTop3PtsUrl = "/ageAndTop3Pts/"+optionValue;
    //console.log(newageAndTop3PtsUrl);
    d3.json(newageAndTop3PtsUrl, function(error, response) {
      if (error) return console.log(error);
      updateageAndTop3Pts(response)
      })
  
    newageAndTopFGMUrl = "/ageAndTopFGM/"+optionValue;
    //console.log(newageAndTopFGMUrl);
    d3.json(newageAndTopFGMUrl, function(error, response) {
      if (error) return console.log(error);
      updateageAndTopFGM(response)
      })

      newageAndTopPWinUrl = "/ageAndTopPWin/"+optionValue;
    //console.log(newageAndTopFGMUrl);
    d3.json(newageAndTopPWinUrl, function(error, response) {
      if (error) return console.log(error);
      updateageAndTopPWin(response)
      })

    }

  //updating  plot with new values 
function updateageDistribution(response) {
  var age = [];
  var numPlayers = [];
    for (var key in response){
      age.push(key)
      numPlayers.push(response[key].length)
    }
  
  var plot2 = document.getElementById('agedistribution');
  Plotly.restyle(plot2, 'x', [age]);
  Plotly.restyle(plot2, 'y', [numPlayers]);
}

  //updating  plot with new values 
  function updateageAndTop3Pts(response) {
    var age = [];
    var topThreePM = [];
    for (var key in response){
      age.push(key)
      topThreePM.push(response[key])
    }
  var plot2 = document.getElementById('ageAndTop3Pts');
  Plotly.restyle(plot2, 'x', [age]);
  Plotly.restyle(plot2, 'y', [topThreePM]);
}

  //updating  plot with new values 
  function updateageAndTopFGM(response) {
    var age = [];
    var topFGM = [];
    for (var key in response){
      age.push(key)
      topFGM.push(response[key])
    }
  var plot2 = document.getElementById('ageAndTopFGM');
  Plotly.restyle(plot2, 'x', [age]);
  Plotly.restyle(plot2, 'y', [topFGM]);
}

  //updating  plot with new values 
  function updateageAndTopPWin(response) {
    var age = [];
    var topPWin = [];
    for (var key in response){
      age.push(key)
      topPWin.push(response[key])
    }
  var plot2 = document.getElementById('ageandTopPWin');
  Plotly.restyle(plot2, 'x', [age]);
  Plotly.restyle(plot2, 'y', [topPWin]);
}
