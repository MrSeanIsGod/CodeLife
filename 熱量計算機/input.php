<!DOCTYPE html>
<html>
<head>
    <title>熱量計算機 - 輸入頁面</title>
    <link rel="icon" type="image/png" href="11.png" sizes="96x96">
    <style>
        body {
            background-color: #f3f0e4; 
            margin: 0;
            padding: 0;
            font-family: '標楷體'; 
        }
        form {
            margin: 50px auto; 
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.75);
            max-width: 900px; 
        }
        h3 {
            text-align: center;
            font-size: 35px; 
        }
        .category {
            font-size: 23px;
            text-align: left;
        }
        .highlight {
            background-color: #ffff66;
        }
        .item {
            font-size: 18px; 
        }
        select, input[type="submit"] {
            font-size: 16px;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: 30%; 
            box-sizing: border-box; 
            display: inline-block;
        }
        input[type="submit"] {
            background-color: #ff9966; 
            color: white;
            cursor: pointer;
            display: block; 
            margin: 20px auto; 
            width: 150px;
            height: 70px; 
            font-size: 28px; 
            font-family: '標楷體';
        }
        input[type="submit"]:hover {
            background-color: #ff8533;
        }
        .category img {
            display: block;
            margin: 0 auto;
            width: 300px;
            height: auto;
            margin-bottom: 20px;
        }
        .category strong {
            font-size: 28px;
        }
        .text-left {
            text-align: left;
        }
        .select-wrapper {
            text-align: center;
            margin-top: 20px;
        }
        .bread-images {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
     }
        .bread-images img {
            width: 250px; 
            height: auto; 
            margin: 0 0.05cm; 
        }
        .bread-category {
            margin-top: 20px; 
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <form method="post" action="result.php">
        <h3>早餐</h3>
        <div class="category">
            <div class="text-left">
                <strong class="highlight">水果:</strong>
            </div>
            <img src='fruit.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="b_fruits">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;"> 
            <div class="text-left">
                <strong class="highlight">蔬菜:</strong>
            </div>
            <img src='vegetable.png' width='200' height='200' />
            <div class="select-wrapper">
                <select name="b_vage">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">雜糧:</strong>
            </div>
            <div class="bread-images">
                <img src='bread1.png' width='200' height='200' />   
                <img src='bread2.jpg' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="b_rice">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">蛋豆魚肉:</strong>
            </div>
            <div class="bread-images">
                <img src='egg1.png' width='200' height='200' />   
                <img src='egg2.png' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="b_egg">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">乳製品:</strong>
            </div>
            <img src='milk.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="b_milk">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">油脂與堅果:</strong>
            </div>
            <img src='oil.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="b_nut">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <hr style="width: 80%; margin: 0 auto; margin-top: 1cm; border-top: 1px solid #ccc;">
        <h3 style="margin-top: 1cm;">午餐</h3>
        <div class="category">
        <div class="text-left">
                <strong class="highlight">水果:</strong>
            </div>
            <img src='fruit.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="c_fruits">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;"> 
            <div class="text-left">
                <strong class="highlight">蔬菜:</strong>
            </div>
            <img src='vegetable.png' width='200' height='200' />
            <div class="select-wrapper">
                <select name="c_vage">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">雜糧:</strong>
            </div>
            <div class="bread-images">
                <img src='bread1.png' width='200' height='200' />   
                <img src='bread2.jpg' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="c_rice">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">蛋豆魚肉:</strong>
            </div>
            <div class="bread-images">
                <img src='egg1.png' width='200' height='200' />   
                <img src='egg2.png' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="c_egg">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">乳製品:</strong>
            </div>
            <img src='milk.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="c_milk">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">油脂與堅果:</strong>
            </div>
            <img src='oil.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="c_nut">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
    <hr style="width: 80%; margin: 0 auto; margin-top: 1cm; border-top: 1px solid #ccc;">
    <h3 style="margin-top: 1cm;">晚餐</h3>
        <div class="category">
            <div class="text-left">
                <strong class="highlight">水果:</strong>
            </div>
            <img src='fruit.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="d_fruits">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;"> 
            <div class="text-left">
                <strong class="highlight">蔬菜:</strong>
            </div>
            <img src='vegetable.png' width='200' height='200' />
            <div class="select-wrapper">
                <select name="d_vage">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">雜糧:</strong>
            </div>
            <div class="bread-images">
                <img src='bread1.png' width='200' height='200' />   
                <img src='bread2.jpg' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="d_rice">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category bread-category">
            <div class="text-left">
                <strong class="highlight">蛋豆魚肉:</strong>
            </div>
            <div class="bread-images">
                <img src='egg1.png' width='200' height='200' />   
                <img src='egg2.png' width='200' height='200' />
            </div>
            <div class="select-wrapper">
                <select name="d_egg">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">乳製品:</strong>
            </div>
            <img src='milk.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="d_milk">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <div class="category" style="margin-top: 40px;">
            <div class="text-left">
                <strong class="highlight">油脂與堅果:</strong>
            </div>
            <img src='oil.png' width='200' height='200' />  
            <div class="select-wrapper">
                <select name="d_nut">
                    <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
                </select>份<br>
            </div>
        </div>
        <input type="submit" name="submit" value="計算熱量">
    </form>
</body>
</html> 