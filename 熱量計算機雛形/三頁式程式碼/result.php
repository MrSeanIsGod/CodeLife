<!DOCTYPE html>
<html>
<head>
    <title>熱量計算機 - 結果頁面</title>
</head>
<body>
    <h2>熱量計算機 - 結果頁面</h2><br>

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

    <a href="home.php">返回首頁</a>

</body>
</html>
