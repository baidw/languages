#!/usr/bin/perl
#如果能处理整个数组或列表，那将是非常方便的，因此 Perl提供了这种方法。
#foreach 从列表的第一个元素一直循环执行到最后一个元素，一次迭代一个
foreach $rock (qw / hello perl world/){
    print "one rock is $rock .\n";
}

@rocks =qw(perl ni hao);
foreach $rock(@rocks){
    $rock="\t$rock \n";
}
print @rocks;


#Perl  最常用的默认变量 ：$_
foreach(1...10){
    print "I can count to $_ !\n";
}
#reverse（逆转）操作将输入的一串列表（可能是数组）按相反的顺序返回
@fred = 1...100;
@rev_fred = reverse(@fred);
print @rev_fred;

#sort操作
@s_rocks=sort(@rocks);
print @s_rocks;

