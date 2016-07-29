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
• 管理纯文本文件
• 使用 .gitignore文件
• 使用分支
• 合理的使用标签
• 规范 commit message 写法
• 规范项目编码（推荐 UTF-8）
• 尽量不要去改写历史
• 尽量保持仓库较新
• 按照代码的完成度提交

git command list:
1.配置工具 
对本地仓库的用户信箱进行配置 
git config --global user.name "[name]"    		---对commit操作设置关联的账号
git config --gloabl user.email "[email addrs]" 	---对commit操作设置的关联邮箱
2.创建仓库 
git init [project name]							---创建本地仓库，并设置名称
git clone [url] 								---下载一个项目以及它所有的版本历史
3.重构文件
git rm [filename]								---从工作目录中删除文件并暂存此删除
git rm --cached [filename]						---从版本控制中移除文件，并在本地保存文件
git mv [filename-orig] [filename-rename]		---改变文件名并commit
4.停止追踪
文本文件.gitignore可以防止一些特定的文件进入到版本控制中
windows下，到需要创建.gitignore文件的文件夹, 右键选择Git Bash 进入命令行，进入项目所在目录
输入 touch .gitignore 然后vi .gitignore文件，添加过滤的文件
git ls-files --other --ignored --exclude-standard	---列出所有项目中忽略的文件
5.保存临时更改
git stash 										---临时存储所有修改的已跟踪文件
git stash pop 									---重新存储所有最近被stash的文件
git stash list 									---列出所有被stash的更改
git stash drop									---放弃所有最近stash的更改
6.更改
git status 										---列出所有更改的文件，通过add添加到暂存区，通过commit提交到本地仓库
git diff 										---展示出那些没有暂存文件的差异
git add [filename]								---将filename放到暂存区
git diff --staged				
git reset [filename]							---将文件移除暂存区，但保留内容
git commit -m "desc messages"					---将暂存区的文件，提交到本地版本库中，并添加描述信息
7.批量更改 
git branch										---列出当前仓库的所有本地分支
git branch [branch-name]						---创建一个branch-name名称的新分支
git merge [branch-name]							---合并branch-name分支的历史到当前分支
git branch -d [branch-name]						---删除名为branch-name的分支
8.查阅历史
git log 										---列出当前分支的版本历史
git log --follow [filename]						---列出文件的版本历史，包括重命名
git diff [first-branch]...[second-branch]		---展示2个不同分支之间的差异
git show [commit]								---输出元数据及特定commit的内容变化
9.撤销commit
git reset [commit]								---撤销所有[commit]后的的commit，在本地保存更改
git reset --hard [commit]						---放弃所有更改并回到某个特定的commit
10.同步更改
git fetch [remote]								---下载远程仓库的所有历史
git merge [remote/branch]						---合并远程分支到当前本地分支
git push [remote] [branch]						---上传所有本地分支commit到GitHub上
git pull 										---下载书签历史并合并更改

