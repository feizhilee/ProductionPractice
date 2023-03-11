       $(document).ready(function () {
            $.ajax({
                url:'/jobPie',
                method:'post',
                dataType:'json',
                success: function(data){
                    yData = []
                    for(var i=0;i<data.length;i++){
                        yData[i] = data[i]
                    }
                    var myChart = echarts.init(document.getElementById('jobPie'));
                    var app = {};

                    var option;

                    option = {
                          title: {
                            text: '各类数量分布饼状图',
                            subtext: '',
                            left: 'center'
                          },
                          tooltip: {
                            trigger: 'item'
                          },
                          legend: {
                            orient: 'vertical',
                            left: 'left'
                          },
                          series: [
                            {
                              name: 'Access From',
                              type: 'pie',
                              radius: '50%',
                              data: [
                                  { value: yData[0][0], name: yData[0][1],url: "http://127.0.0.1:5000/joblist" },
                                  { value: yData[1][0], name: yData[1][1],url: "http://127.0.0.1:5000/joblist2" },
                                  { value: yData[2][0], name: yData[2][1],url: "http://127.0.0.1:5000/joblist3" },
                                  { value: yData[3][0], name: yData[3][1],url: "http://127.0.0.1:5000/joblist4" },
                                  { value: yData[4][0], name: yData[4][1],url: "http://127.0.0.1:5000/joblist5" },
                                  { value: yData[5][0], name: yData[5][1],url: "http://127.0.0.1:5000/joblist6" }
                              ],
                              emphasis: {
                                itemStyle: {
                                  shadowBlur: 10,
                                  shadowOffsetX: 0,
                                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                              }
                            }
                          ]
                        };
                    option && myChart.setOption(option);
                    myChart.on("click", function (params) {
                      console.log(params);
                      var url = params.data.url;
                      window.location.href = url;
                  });
                },

            })
        })