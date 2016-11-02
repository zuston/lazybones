<?php
$weather = new weatherService();
try {
    if (!method_exists($weather, $argv[1])) {
        throw new Exception('weatherService function:' . $argv[1] . ' not exist');
    }
    //echo json_encode([1, $weather->{$argv[1]}($argv[2])]);
    echo $weather->{$argv[1]}($argv[2]);
} catch(Exception $e) {
    echo json_encode([0, $e->getMessage()]);
}

class weatherService
{
    /**
     * 根据关键字获取返回内容
     *
     * @param $str_key
     * @return array|string
     */
    public function getAction($str_key)
    {
        if (!empty($str_key)) {
            $content = $this->weatherInfo($str_key);
            if (empty($content)) {
                $content = "抱歉，没有查到\"" . $str_key . "\"的天气信息！";
            }
        } else {
            $content = "请输入城市名称，如‘上海’！";
        }

        return $content ? json_encode($content) : '';
    }

    /**
     * 多条消息格式整合
     *
     * @param $n
     * @return mixed|null
     */
    private function weatherInfo($cityName)
    {
        $result = $this->getWeatherData($cityName);
        if ($result["error"] != 0) {
            return $result["status"];
        }
        $weather = $result["results"][0];//按照微信公众号开发文档,组建设多图文回复信息

        $weatherArray[] = $weather['currentCity'] . "当前天气:" . "温度:" . $weather['weather_data'][0]['temperature'] . "," . $weather['weather_data'][0]['weather'] . "," . "风力:" . $weather['weather_data'][0]['wind'] . ".";
        for ($i = 0; $i < count($weather["weather_data"]); $i++) {
            $weatherArray[] = $weather["weather_data"][$i]["date"] . "\n" . $weather["weather_data"][$i]["weather"] . " " . $weather["weather_data"][$i]["wind"] . " " . $weather["weather_data"][$i]["temperature"];
        }

        return $weatherArray;
    }

    /**
     * 对象转换成数组
     *
     * @param $obj
     * @return mixed
     */
    private function objectToArray($obj)
    {
        $_arr = is_object($obj) ? get_object_vars($obj) : $obj;
        foreach ($_arr as $key => $val) {
            $val = (is_array($val) || is_object($val)) ? $this->objectToArray($val) : $val;
            $arr[$key] = $val;
        }
        return $arr;
    }

    /**
     * 调取天气信息
     *
     * @param $cityName
     * @return mixed
     */
    private function getWeatherData($cityName)
    {
        $url = "http://api.map.baidu.com/telematics/v3/weather?location=" . urlencode($cityName) . "&output=json&ak=qPFnHQ18Y3mbqGmrTolRqhKd";
        $json = file_get_contents($url);

        return $this->objectToArray(json_decode($json));
    }
}
