<!DOCTYPE html>
<html>
<head>
    <title>熱量計算機 - 輸入頁面</title>
</head>
<body>
    <h2>熱量計算機 - 輸入頁面</h2><br>

    <form method="post" action="result.php">
    水果:<br>
    一份:1/2根香蕉|1顆蘋果|13顆葡萄<br>    
    早餐<select name="b_fruits">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_fruits">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_fruits">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br>

    蔬菜:<br>
    一份:1/2碗青菜<br>    
    早餐<select name="b_vage">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_vage">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_vage">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br>    

    雜糧:<br>
    一份:1/4碗飯|1/2碗麵|1/2片薄吐司<br>    
    早餐<select name="b_rice">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_rice">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_rice">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br> 

    蛋豆魚肉:<br>
    一份:1顆蛋|1/2盒豆腐|3匙肉鬆<br>    
    早餐<select name="b_egg">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_egg">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_egg">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br> 

    乳製品:<br>
    一份:1杯牛奶|2片起司|1杯優格<br>    
    早餐<select name="b_milk">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_milk">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_milk">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br> 

    油脂與堅果:<br>
    一份:1茶匙油|堅果1湯匙|沙茶醬1/2湯匙<br>    
    早餐<select name="b_nut">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    午餐<select name="l_nut">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br>
    晚餐<select name="d_nut">
        <?php for ($i = 0; $i <= 9; $i++) echo "<option value='{$i}'>{$i}</option>"; ?>
    </select>份<br><br> 


    <input type="submit" name="submit" value="計算熱量">
    </form>

</body>
</html>
