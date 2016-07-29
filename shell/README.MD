Unix/Linux命令参考:
文件命令:
ls 									---列出目录
ls -al 								---使用格式化列出所有文件
cd dir 								---更改目录到dir目录下
cd 									---更改目录到home目录
pwd 								---显示当前目录
mkdir dir 							---创建目录dir
rm file  							---删除file文件
rm -r dir 							---删除dir目录
rm -f file 							---强制删除file文件
rm -rf dir 							---强制删除dir目录(包括该目录下的所有 文件和子目录)
cp file1 file2 						---复制file1文件到file2文件
cp -r dir1 dir2 					---复制dir1到dir2(若dir2不存在则创建一个新的目录)
mv file1 file2 						---将file1重命名或者移动到file2,若file2存在则是将file1移动到file2中
ln -s file links					---创建file的符号链接links
touch file 							---创建file文件
cat > file 							---将标注输入添加到file 
more file 							---查看file的内容
head file 							---查看file的开头的内容
