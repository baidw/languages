#!/usr/bin/perl

#undef 
#变量在第一次赋值前有一个特殊值 undef

while($n < 10){
    $sum += $n ;
    $n += 2;
    print "current number is ${n}.\n" ;
}

print "The total sum is: ${sum}.\n";


$string .=",hi!\n";
print $string ;
#去掉换行符,返回值是去掉换行符的数量
$c = chomp($string);
print $string ;
print "remove \\n count number is : $c ";

$var  = undef ;
if(defined($var)){
    print "The input  was $var .\n"
}else{
    print "No input variable!\n";
}
