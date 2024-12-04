dev容器使用教程:
> 好处：
> - 不使用主机环境
>   - 采取的是这种ide环境和运行环境分开的方案
>   - 业务运行环境重新构建时，代码还可以正常编辑的
> - 多个项目的环境相互隔离,不共用


- 将当前目录下的`文件(.vscode 和 .devcontainer)`拷贝到`项目根目录`中
- 在`项目目录`下的`.gitignore`文件中添加忽略, 添加内容: `.devcontainer`和`.vscode`
- 项目的`compose文件`中的`volumes`部分,不能使用`相对路径`,需要使用`绝对路径`
  - `- /home/jwf/PhishOne-backend/phishone:/phishone`

---

具体运行流程:
- 首次打开,时会自动生成该项目的环境
- 第二次打开,将使用已经存在的环境