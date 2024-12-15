<?php
$lore = "Santa Claus keeps a list of those who are naughty and nice. The 'good' list includes individuals who have shown kindness and generosity, while the 'naughty' list includes those who have misbehaved.";

$list = isset($_GET['list']) ? $_GET['list'] : null;
$content = '';

function clean($input) {
    $max_depth = 100; # Should be enough right?
    for ($i = 0; $i < $max_depth; $i++) {
        $clean = str_replace(['../'], '', $input);
        if ($clean === $input) { # No changes
            return $clean;
        }
        $input = $clean;
    }
    return $clean;
}

if ($list) {
    $clean_list = clean($list);
    $filePath = __DIR__ . '/lists/' . $clean_list;
    if (file_exists($filePath)) {
        ob_start();
        include($filePath);
        $content .= ob_get_clean();
    } else {
        $content .= "<p>List not found.</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/style.css">
    <title>Santa's Christmas Lore</title>
</head>
<body>
    <div class="container">
        <h1>Christmas Lore</h1>
        <p><?php echo $lore; ?></p>
        
        <h2>Select a List</h2>
        <form method="get">
            <button type="submit" name="list" value="good.php">Good List</button>
            <button type="submit" name="list" value="naughty.php">Naughty List</button>
        </form>

        <div class="content-box">
            <?php echo $content; ?>
        </div>
    </div>
</body>
</html>