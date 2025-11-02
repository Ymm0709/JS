# Flask Ajax 动态生成 Span 元素项目

这个项目展示了如何使用 Flask 后端和 Ajax 前端动态生成 HTML 元素。

## 功能特点

- 从 Flask 后端获取数据
- 使用 Ajax 动态创建 span 元素
- 点击 span 元素显示详细信息

## 项目结构

```
JS/
├── app.py                 # Flask 应用
├── templates/
│   └── index.html        # 前端页面
└── README.md
```

## 安装和运行

1. 安装依赖：
```bash
pip install flask
```

2. 运行应用：
```bash
python app.py
```

3. 在浏览器中访问：
```
http://localhost:5000
```

## API 接口

- `GET /` - 主页面
- `GET /students` - 获取学生/球员数据（JSON格式）

