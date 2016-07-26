#!/usr/bin/perl

$var_01 = 17;
$var_02 = 'hello';
print $var_01 ;
print "\n";
print $var_02 ; 
print "\n";
$var_02 = $var_01 + 3;
print $var_02 ;
print "\n";
$var_02 = $var_02 * 2 ;
print $var_02 ;
print "\n";

#二元赋值
#1.未使用二元赋值值操作符
$var_02 = $var_02 + 5 ;
print $var_02 ;
print "\n";
#2.使用二元赋值操作符
$var_02 += 5 ; 
print $var_02 ;
print "\n";

$str_001 = 'hello' ; 
$str_002 = 'hello' ;
$str_001 = $str_001.' perl.' ;
print $str_001 ; 
print "\n";
$str_002 .= ' perl.' ; 
print $str_002 ;
print "\n";

print $str_001,$str_002 ;
print "\n";

#字符串中标量变量的内插
$var_user = 'users' ;
$banner = "welcome to $var_user \n";
print "$banner" ;
$banner_001 = "welcome to ".$var_user."\n" ;
print "$banner_001" ;
$banner_002 = "welcome to ${var_user}\n" ;
print $banner_002;

