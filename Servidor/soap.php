<?php
require_once "src/nusoap.php";

$namespace = "miSoap2";
$servicio = new soap_server();
$servicio->configureWSDL("SOAP2",$namespace);
$servicio->wsdl->schemaTargetNamespace = $namespace;

$servicio->register("Suma", array('num1' => 'xsd:integer', 'num2' => 'xsd:integer'), array('return' => 'xsd:string'), $namespace);

function Suma($num1, $num2){
    $resultadoSuma = $num1 + $num2;
    $resultado = "el resultado de la suma es: ".$resultadoSuma;
    return $resultado;
}

$servicio->register("resta", array('num1' => 'xsd:integer', 'num2' => 'xsd:integer'), array('return' => 'xsd:string'), $namespace);

function resta($num1, $num2){
    $resultadoSuma = $num1 - $num2;
    $resultado = "el resultado de la resta es: ".$resultadoSuma;
    return $resultado;
}






$HTTP_RAW_POST_DATA = isset($HTTP_RAW_POST_DATA)? $HTTP_RAW_POST_DATA : '';
$servicio->service(file_get_contents("php://input"));
exit();

?>