$(document).ready(function () {
            $.ajax({
                url:'/jobbar',
                method:'post',
                dataType:'json',
                success: function(data){
                    xData = []
                    yData = []
                    for(var i=0;i<data.length;i++){
                        xData[i] = data[i].book_type
                        yData[i] = data[i].book_grade
                    }

                    var chartDom = document.getElementById('jobbar');
                    var myChart = echarts.init(chartDom);
                    var option;

                    option = {
                      title: {
                            text: '各类数据书籍评分图',
                            subtext: '',
                            left: 'center'
                          },
                      xAxis: {
                        type: 'category',
                        data: xData
                      },
                      yAxis: {
                        type: 'value'
                      },
                      series: [
                        {
                          data: yData,
                          type: 'bar',
                          showBackground: true,
                          backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                          }
                        }
                      ]
                    };

                    option && myChart.setOption(option);
                },

            })
        })