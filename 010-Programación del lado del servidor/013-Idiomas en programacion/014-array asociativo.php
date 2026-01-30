<?php

$csv = array_map('str_getcsv', file('idiomas.csv'));
$header = array_shift($csv);

$data = array_map(
    fn($row) => array_combine($header, $row),
    $csv
);

var_dump($data);
?>
