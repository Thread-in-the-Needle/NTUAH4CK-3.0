<?php

try {
    $flag = readfile('/var/www/html/flag.txt');
} catch (Exception $e) {
    $flag = 'NH4CK{FAKE_FLAG}';
}

$secret_list = [
    [
        'name' => 'Ms. Claus',
        'description' => 'Keeps the North Pole running smoothly while Santa is away.'
    ],
    [
        'name' => 'Santa Claus',
        'description' => 'Holds the secret of Christmas magic: ' . $flag
    ]
];

// Display the good list
foreach ($secret_list as $secret) {
    echo "<h3>{$secret['name']}</h3>";
    echo "<p>{$secret['description']}</p>";
}
?>