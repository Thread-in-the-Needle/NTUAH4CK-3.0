<?php
$naughty_list = [
    [
        'name' => 'John Doe',
        'description' => 'Known for stealing cookies from the cookie jar.'
    ],
    [
        'name' => 'Jane Smith',
        'description' => 'Frequently breaks the rules and causes mischief.'
    ],
    [
        'name' => 'Tom Brown',
        'description' => 'Has a habit of being rude to others during the holiday season.'
    ],
];

foreach ($naughty_list as $individual) {
    echo "<h3>{$individual['name']}</h3>";
    echo "<p>{$individual['description']}</p>";
}
?>