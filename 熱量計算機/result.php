<!DOCTYPE html>
<html>
<head>
    <title>熱量計算機 - 結果頁面</title>
    <link rel="icon" type="image/png" href="11.png" sizes="96x96">
    <style>
        body {
            background-color: #f3f0e4;
            margin: 0;
            padding: 0;
            font-family: '標楷體';
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #000000; 
        }
        .container {
            width: 60%;
            padding: 70px;
            background-color: #ffffff; 
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.75);
        }
        h2 {
            text-align: center;
            font-size: 80px;
            margin-bottom: 50px;
        }
        p {
            text-align: center;
            padding: 20px;
            font-size: 50px; 
            margin-bottom: 20px;
        }
        a {
            display: block;
            padding: 50px;
            text-align: center;
            margin-top: 20px;
            font-size: 25px;
            color: #007bff; 
            text-decoration: none;
        }
        .third-line {
            margin-top: 20px;
        }
        form {
            margin-top: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        input[type="submit"] {
            margin-top: 20px;
            font-size: 20px;
            padding: 15px 30px;
            background-color: #ff6600;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #ff8533;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>熱量計算機</h2>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $total_calories = 0;
            $fruits_t = $_POST['b_fruits'] + $_POST['c_fruits'] + $_POST['d_fruits'];
            $vage_t = $_POST['b_vage'] + $_POST['c_vage'] + $_POST['d_vage'];
            $rice_t = $_POST['b_rice'] + $_POST['c_rice'] + $_POST['d_rice'];
            $egg_t = $_POST['b_egg'] + $_POST['c_egg'] + $_POST['d_egg'];
            $milk_t = $_POST['b_milk'] + $_POST['c_milk'] + $_POST['d_milk'];
            $nut_t = $_POST['b_nut'] + $_POST['c_nut'] + $_POST['d_nut'];
            $total_calories = ($fruits_t * 60) + ($vage_t * 25) + ($rice_t * 70) + ($egg_t * 75) + ($milk_t * 150) + ($nut_t * 45);
            echo "<p class='third-line'><strong>您今天攝取的總熱量為：{$total_calories} 大卡</strong></p>";
        } else {
            echo "<p class='third-line'>未收到有效的數據。</p>"; 
        }
        ?>
        <a href="home.php">返回首頁</a>
        <form method="post" action="result.php">
        </form>
    </div>
</body>
</html>