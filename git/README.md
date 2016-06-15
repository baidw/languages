echo "# languages" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:baidw/languages.git
git push -u origin master

2016-06-01
id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDe5MbvNZFvpVlgwMVjgu6ioM9Ses1wiPuwEtTtzYcCzQqr8AycUQ88iu5RRXsf0cnIu88+BpJCiqRCiT2sDci049IZT3ftW8SFLVgambho1QmDkjUxL/HJ6kEi71tK2a6NOjMWfmhDjb8P0SuvvsA+1NlqN/tiSghWZlrecAvR4R0eF6+cgRG2bIT592+pjOfZm6q3RnTFeVEYSINry9LgeUe6nxt6JxXg8J6+XSpzAVqoESxK0kEz9nSuiCeUUUQJIypXgFEVQbkFazFYaHZ/DXRls5GmffSkPlkixhfRUupCKativd0M9hV9BUYMSZfSTu2E181WWnkpF0aZP4AH baidwei@126.com


git dir
目录结构
一、安装GIT 
二、初始配置
三、版本库操作命令
四、
五、

git是分布式版本控制系统
参考：http://www.bootcss.com/p/git-guide/
一、安装GIT
Linux系统:
git --version    #查看git版本，若没有则提示：git: command not found
sudo apt-get install git  #Debian或Ubuntu Linux系统   
#若是老版本的Debian或Ubuntu Linux 参考安装命令：sudo apt-get install git-core
#源码安装步骤：
1.官网下载源码
2.执行 ./configure ; make ;sudo make install

Window系统：
http://msysgit.github.io/下载最新版本安装

二、初始配置
1.创建仓库respository
cd 源码目录        #源码目录(工作区)，没有可以创建空的工作区目录
git init 		   #初始化，即创建respository仓库，创建成功会生成一个.git的目录[windows下，是隐藏文件夹]
2.配置用户信息
git config --global user.name  XXXXXX 	#XXXXXX 用户名
git config --global user.email XXXXXX 	#XXXXXX 用户邮箱

git config --list 						#查看用户信息
git rev-parse --git-dir 				#显示.git所在目录位置
git rev-parse --show-toplevel           #显示工作区根目录



三、版本库操作命令
1.添加、删除文件[add到暂存区]
git add filename 	#添加单个文件
git add . 			#添加当前目录下的所有未提交的文件
git add [path]      #添加目录或文件
2.提交文件[commit到git仓库]
git commit -m "xx"  #提交，同时添加"xx"简单地 提交版本描述
3.查看版本库状态 及 版本信息
git status 			#查看工作区状态
git log 			#查看版本信息
git log --pretty=oneline  #精简单行显示：已提交的版本信息
3.版本撤销、恢复
git reset				  #将所有暂存区的文件，返回到非暂存区时的状态
git reset --hard          #回到原来编辑的地方,这中间的修改会丢失
git reset --hard XXXXXX   #回到指定的版本


4.查看修改内容不同之处
git diff filename   #比较未add的文件 与 add的文件区别


几个 Git 的基础最佳实践
12
• 管理纯文本文件
• 使用 .gitignore文件
• 使用分支
• 合理的使用标签
• 规范 commit message 写法
• 规范项目编码（推荐 UTF-8）
• 尽量不要去改写历史
• 尽量保持仓库较新
• 按照代码的完成度提交
