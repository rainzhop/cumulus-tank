/* 数据格式演示
var aqiSourceData = {
  "北京": {
    "2016-01-01": 10,
    "2016-01-02": 10,
    "2016-01-03": 10,
    "2016-01-04": 10
  }
};
*/

// 以下两个函数用于随机模拟生成测试数据
function getDateStr(dat) {
  var y = dat.getFullYear();
  var m = dat.getMonth() + 1;
  m = m < 10 ? '0' + m : m;
  var d = dat.getDate();
  d = d < 10 ? '0' + d : d;
  return y + '-' + m + '-' + d;
}
function randomBuildData(seed) {
  var returnData = {};
  var dat = new Date("2016-01-01");
  var datStr = ''
  for (var i = 1; i < 92; i++) {
    datStr = getDateStr(dat);
    returnData[datStr] = Math.ceil(Math.random() * seed);
    dat.setDate(dat.getDate() + 1);
  }
  return returnData;
}

var aqiSourceData = {
  "北京": randomBuildData(500),
  "上海": randomBuildData(300),
  "广州": randomBuildData(200),
  "深圳": randomBuildData(100),
  "成都": randomBuildData(300),
  "西安": randomBuildData(500),
  "福州": randomBuildData(100),
  "厦门": randomBuildData(100),
  "沈阳": randomBuildData(500)
};

// 用于渲染图表的数据
var chartData = {};

// 记录当前页面的表单选项
var pageState = {
  nowSelectCity: -1,
  nowGraTime: "day"
}

/**
 * 渲染图表
 */
function renderChart() {
  var colors = ['#f00', '#0f0', '#00f', '#ff0', '#f0f', '#0ff', '#000'];
  var city = chartData[pageState.nowSelectCity];
  var data = city[pageState.nowGraTime];
  var chart = document.getElementsByClassName('aqi-chart-wrap')[0];
  chart.innerHTML = "";
  for (var i = 0; i < data.length; i++) {
    var aqi = data[i];
    var rect = document.createElement('div');
    rect.setAttribute('class', 'chart-' + pageState.nowGraTime);
    rect.setAttribute('style', 'height: ' + aqi + 'px; background-color: ' + colors[Math.floor(Math.random() * 7)]);
    rect.setAttribute('title', 'aqi: ' + aqi);
    chart.appendChild(rect);
  }
}

/**
 * 日、周、月的radio事件点击时的处理函数
 */
function graTimeChange(e) {
  // 确定是否选项发生了变化
  var newGraTime = e.target.value;
  if (newGraTime == pageState.nowGraTime) {
    return;
  }

  // 设置对应数据
  pageState.nowGraTime = newGraTime;

  // 调用图表渲染函数
  renderChart();
}

/**
 * select发生变化时的处理函数
 */
function citySelectChange(e) {
  // 确定是否选项发生了变化
  var index = e.target.selectedIndex;
  var newSelectCity = e.target.options[index];
  if (newSelectCity == pageState.nowSelectCity) {
    return;
  }

  // 设置对应数据
  pageState.nowSelectCity = newSelectCity.value;

  // 调用图表渲染函数
  renderChart();
}

/**
 * 初始化日、周、月的radio事件，当点击时，调用函数graTimeChange
 */
function initGraTimeForm() {
  var forms = document.getElementsByName('gra-time');
  for (var i = 0; i < forms.length; i++) {
    forms[i].onclick = graTimeChange;
  }
}

/**
 * 初始化城市Select下拉选择框中的选项
 */
function initCitySelector() {
  // 读取aqiSourceData中的城市，然后设置id为city-select的下拉列表中的选项
  var city_select = document.getElementById('city-select');
  for (var city in aqiSourceData) {
    var op = document.createElement('option');
    op.innerText = city;
    city_select.appendChild(op);
  }

  // 给select设置事件，当选项发生变化时调用函数citySelectChange
  city_select.onchange = citySelectChange;

  var index = city_select.selectedIndex;
  var selectedCity = city_select[index];
  pageState.nowSelectCity = selectedCity.value;
}

/**
 * 初始化图表需要的数据格式
 */
function initAqiChartData() {
  // 将原始的源数据处理成图表需要的数据格式
  for (var city in aqiSourceData) {
    var cityData = {
      day: [],
      week: [],
      month: []
    }

    var weekInit = 4; // 2016-01-01 is Friday
    var weekDayCnt = 0;
    var weekTotalAqi = 0;

    var monthLast = 1;
    var monthDayCnt = 0;
    var monthTotalAqi = 0;

    for (var date in aqiSourceData[city]) {
      var aqi = parseInt(aqiSourceData[city][date]);
      // day
      cityData.day.push(aqi);

      // week
      weekDayCnt++;
      weekTotalAqi += aqi;
      if ((weekDayCnt + weekInit) % 7 == 0) {
        cityData.week.push(weekTotalAqi / weekDayCnt);
        weekInit = 0;
        weekDayCnt = 0;
        weekTotalAqi = 0;
      }

      // month
      var dateArr = date.split('-');
      var m = dateArr[1];
      if (m != monthLast) {
        cityData.month.push(monthTotalAqi / monthDayCnt);
        monthLast = m;
        monthDayCnt = 0;
        monthTotalAqi = 0;
      }
      monthDayCnt++;
      monthTotalAqi += aqi;
    }

    if (weekDayCnt != 0) {
        cityData.week.push(weekTotalAqi / weekDayCnt);
    }

    cityData.month.push(monthTotalAqi / monthDayCnt);

    // 处理好的数据存到 chartData 中
    chartData[city] = cityData;
  }
}

/**
 * 初始化函数
 */
function init() {
  initGraTimeForm()
  initCitySelector();
  initAqiChartData();
}

init();
