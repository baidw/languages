#!/usr/bin/perl

$var = 'a' ;
$var_001 = 80 ;


if ( $var eq 'a'){
    print ${var}."\n" ;
}

if($var_001 == 100){
    print ${var_001}."\n";
}else{
    print ${var_001}." is lower than 100 .\n";
}
