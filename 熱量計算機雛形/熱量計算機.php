<!DOCTYPE html>
<html>
<head>
    <title>熱量計算機</title>
</head>
<body>
    <h2>熱量計算機</h2>
    份量參考(一份):<br>
    水果:1/2根香蕉|1顆蘋果|13顆葡萄<br>
    蔬菜:1/2碗青菜<br>
    雜糧:1/4碗飯|1/2碗麵|1/2片薄吐司<br>
    蛋豆魚肉:1顆蛋|1/2盒豆腐|3匙肉鬆<br>
    乳製品:1杯牛奶|2片起司|1杯優格<br>
    油脂與堅果:1茶匙油|堅果1湯匙|沙茶醬1/2湯匙<br><br>
    <form method="post">
    早餐:<br>
    水果<select name="b_fruits">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蔬菜<select name="b_vage">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    雜糧<select name="b_rice">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蛋豆魚肉<select name="b_egg">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    乳製品<select name="b_milk">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    油脂與堅果<select name="b_nut">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br><br>

    午餐:<br>
    水果<select name="l_fruits">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蔬菜<select name="l_vage">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    雜糧<select name="l_rice">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蛋豆魚肉<select name="l_egg">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    乳製品<select name="l_milk">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    油脂與堅果<select name="l_nut">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br><br>

    晚餐:<br>
    水果<select name="d_fruits">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蔬菜<select name="d_vage">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    雜糧<select name="d_rice">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    蛋豆魚肉<select name="d_egg">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    乳製品<select name="d_milk">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br>
    油脂與堅果<select name="d_nut">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
    </select>份<br><br>

    <input type="submit" name="submit" value="計算熱量">
</form>

    <?php
    // 檢查表單是否提交
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // 獲取表單數據
        $fruits_t = $_POST['b_fruits'] + $_POST['l_fruits'] + $_POST['d_fruits'];
        $vage_t = $_POST['b_vage'] + $_POST['l_vage'] + $_POST['d_vage'];
        $rice_t = $_POST['b_rice'] + $_POST['l_rice'] + $_POST['d_rice'];
        $egg_t = $_POST['b_egg'] + $_POST['l_egg'] + $_POST['d_egg'];
        $milk_t = $_POST['b_milk'] + $_POST['l_milk'] + $_POST['d_milk'];
        $nut_t = $_POST['b_nut'] + $_POST['l_nut'] + $_POST['d_nut'];

        // 計算總熱量
        $total_calories = ($fruits_t * 60) + ($vage_t * 25) + ($rice_t * 70) + ($egg_t * 75) + ($milk_t * 150) + ($nut_t * 45);

        // 顯示結果
        echo "<p><strong>總熱量: {$total_calories} 大卡</strong></p>";
    }
    ?>
</body>
</html>
