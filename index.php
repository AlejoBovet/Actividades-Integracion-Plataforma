<?php 

$namespace = "soapIntegracionP";
$server = new soap_server();
$server->configureWDLS("Soap2020",$namespace);
$server->wsd1->shemaTargetNamespace = $namespace;

$server->wsd1->addcomplexType(
    'ordendecompra',
    'complexType',
    'struct',
    'all',
    '',
    array(
        'numeroOrden' => array('name' => 'numeroOrden', 'type' => 'xsd:string'),
        'ordenante' => array('name' => 'ordenante', 'type' => 'xsd:string'),
        'moneda' => array('name' => 'moneda', 'type' => 'xsd:string'),
        'tipodecambio' => array('name' => 'tipodecambio', 'type' => 'xsd:decimal')
    )
);


$server->wsd1->addcomplexType(
    'response',
    'complexType',
    'struct',
    'all',
    '',
    array(
        'Numerodeautorizacion' => array('name'=>'Numerodeautorizacion','type'=>'xsd:string'),
        'Resultado' => array('name'=>'Resultado','type'=>'xsd:boolean'),
    )
);

$server->register(
    'guardarordendeCompra',
    array('name' => 'tns:ordendecompra'),
    array('name' => 'tns:response'),
    $namespace,
    false,
    'rpc',
    'encode',
    'recibe una orden de compra de un numero aurtorizado'

);

function guardarordendeCompra($request){
    return array(
        "Numerodeautorizacion" => "la orden de compra".$request["numeroOrden"]."ha sido autorizda con el numero".rand(10000.100000),
        "Resultado" => true 
    );
}

$POST_DATA = file_get_contents("php://input");
$server->service($POST_DATA);
exit();