#!/usr/bin/perl
#列表和数组可以包含任意数量的元素。最少含有0 元素，最多可以填满你的可用内存


$fred =undef ;
$fred[0] = "hello" ; 
$fred[1] = "perl" ;
$fred[2] = 2 ;
$fred[3] = undef;

print $fred[0] ;
print $fred[1] ;
print $fred[2] ;
print $fred[3] ;
print "\n" ;
print $#fred ;

#数组是由括号括起来并且其元素由逗号分隔开的列表。这些值组成了数组的元素
$ar = (1,3 ... 6 );
print $ar;