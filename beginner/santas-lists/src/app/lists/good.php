<?php
$goodList = [
    [
        'name' => 'Rudolph the Red-Nosed Reindeer',
        'description' => 'Guides Santa\'s sleigh with his bright red nose.'
    ],
    [
        'name' => 'Frosty the Snowman',
        'description' => 'Brings joy and happiness to children during the winter season.'
    ],
    [
        'name' => 'The Elves',
        'description' => 'Help Santa make toys and spread Christmas cheer.'
    ],
    [
        'name' => 'The Grinch (after his transformation)',
        'description' => 'Learns the true meaning of Christmas and spreads joy.'
    ]
];

// Display the good list
foreach ($goodList as $good) {
    echo "<h3>{$good['name']}</h3>";
    echo "<p>{$good['description']}</p>";
}
?>