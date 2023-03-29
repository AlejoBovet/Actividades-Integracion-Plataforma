<?php 



$cliente = new ("http://localhost/Actividades-Integracion-Plataforma-main/index.php?wsdl");

var_dump($cliente);


$guardarOrdenDeCompraS = $cliente->guardarOrdenDeCompra([
    'NumeroOrden' => 23234,
    'Ordenante' => 'DEDE',
    'Moneda' => 'EURO',
    'TipoCambio' => 1,
])->return;

echo $guardarOrdenDeCompraS;



