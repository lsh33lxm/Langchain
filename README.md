# LangChain 学习资料整理版

把 3 套 LangChain / RAG 教程资料整理到一个目录里，方便统一保存、上传 GitHub、按来源学习和对照运行结果。

## 这个仓库里有什么

- 3 套来源不同的 LangChain / RAG 学习资料
- 每套都尽量保留：
  - 可逐步运行版 Notebook
  - 已运行结果对照版 Notebook
- 只保留主 Notebook 直接依赖的数据、脚本和示例文件
- 不保留缓存、向量库、聊天历史等运行产物

## 适合谁

- 想按教程来源分别学习 LangChain 的人
- 想一边跑 Notebook，一边对照已有输出的人

## 快速开始

### 1. 安装基础依赖

```powershell
python -m pip install -U langchain langchain-core langchain-community langchain-openai langchain-text-splitters langchain-chroma chromadb openai dashscope pypdf beautifulsoup4 streamlit lark defusedxml nbconvert nbformat nbclient
```

### 2. 配置百炼 Key

很多模型调用和 Embedding 单元都依赖 `DASHSCOPE_API_KEY`：

```powershell
$env:DASHSCOPE_API_KEY = "你的阿里云百炼Key"
```

如果要长期使用，也可以设置为用户级环境变量。

### 3. 进入对应目录再打开 Notebook

很多 Notebook 依赖当前工作目录，不建议直接从别的目录启动。

示例：

```powershell
cd D:\Langchain\01_github_langchain_tutorial
```

然后再打开对应的 `.ipynb`。

### 4. 学习时优先打开哪一类文件

- `*.ipynb`：适合自己一步步运行
- `*.executed.ipynb` 或 `_executed.ipynb`：适合对照输出结果

## 推荐学习顺序

如果你是按“从浅到深”学习，建议这样看：

1. `01_github_langchain_tutorial`
   - 适合先熟悉 LangChain 的基础组件
   - 数据依赖简单，主线更清晰
2. `02_bilibili_langchain_bailian`
   - 适合看一份更偏“综合整理版”的 LangChain 复现
   - 内容比较集中
3. `03_heima_rag_agent`
   - 适合进阶看 RAG、项目案例、Agent 方向
   - 对环境要求更高，也更依赖模型服务

如果你是按“想先看项目案例”学习，建议这样看：

1. `03_heima_rag_agent/03_RAG项目案例`
2. `03_heima_rag_agent/02_LangChainRAG开发`
3. 再回头看 `01_github_langchain_tutorial`

## 目录结构

```text
D:\Langchain
├─ README.md
├─ 01_github_langchain_tutorial
│  ├─ 01_LangChain.ipynb
│  ├─ 01_LangChain.executed.ipynb
│  ├─ requirements.txt
│  └─ examples
├─ 02_bilibili_langchain_bailian
│  ├─ 02-LangChain.ipynb
│  ├─ 02-LangChain_executed.ipynb
│  ├─ pdf
│  └─ txt
└─ 03_heima_rag_agent
   ├─ 01_OpenAI库的基础使用
   ├─ 02_LangChainRAG开发
   └─ 03_RAG项目案例
```

## 三套资料说明

### 1. `01_github_langchain_tutorial`

来源：

- GitHub：[QunBB/DeepLearning - llms/langchain_tutorial](https://github.com/QunBB/DeepLearning/tree/main/llms/langchain_tutorial)

当前保留内容：

- `01_LangChain.ipynb`
- `01_LangChain.executed.ipynb`
- `requirements.txt`
- `examples/rag.txt`
- `examples/test.csv`
- `examples/sql.pdf`
- `examples/sql.md`

### 2. `02_bilibili_langchain_bailian`

来源：

- B 站教程：[LangChain 综合复现相关视频](https://www.bilibili.com/video/BV1ZDo5YWE7e/?spm_id_from=333.1387.favlist.content.click)

当前保留内容：

- `02-LangChain.ipynb`
- `02-LangChain_executed.ipynb`
- `txt/1.md`
- `txt/faq-4359.txt`
- `txt/faq-7923.txt`
- `txt/test.html`
- `pdf/2312.04005.pdf`

### 3. `03_heima_rag_agent`

来源：

- 黑马教程：[黑马程序员大模型 RAG 与 Agent 智能体项目实战教程](https://www.bilibili.com/video/BV1yjz5BLEoY/?spm_id_from=333.1387.favlist.content.click&vd_source=1883ace75f3996b45995309c86acd625)

当前保留内容：

- `01_OpenAI库的基础使用/一、提示词工程.ipynb`
- `01_OpenAI库的基础使用/一、提示词工程.executed.ipynb`
- `02_LangChainRAG开发/二、LangChain_RAG.ipynb`
- `02_LangChainRAG开发/二、LangChain_RAG.executed.ipynb`
- `02_LangChainRAG开发/data/info.csv`
- `02_LangChainRAG开发/data/pdf2.pdf`
- `02_LangChainRAG开发/data/Python基础语法.txt`
- `02_LangChainRAG开发/data/stu_json_lines.json`
- `02_LangChainRAG开发/data/stu.csv`
- `03_RAG项目案例/三、RAGcase.ipynb`
- `03_RAG项目案例/三、RAGcase.executed.ipynb`
- `03_RAG项目案例/app_file_uploader.py`
- `03_RAG项目案例/app_qa.py`
- `03_RAG项目案例/config_data.py`
- `03_RAG项目案例/file_history_store.py`
- `03_RAG项目案例/knowledge_base.py`
- `03_RAG项目案例/rag.py`
- `03_RAG项目案例/vector_stores.py`
- `03_RAG项目案例/data/尺码推荐.txt`
- `03_RAG项目案例/data/洗涤养护.txt`
- `03_RAG项目案例/data/颜色选择.txt`

## Notebook 命名说明

- 可逐步运行版：
  - `01_LangChain.ipynb`
  - `02-LangChain.ipynb`
  - `一、提示词工程.ipynb`
  - `二、LangChain_RAG.ipynb`
  - `三、RAGcase.ipynb`
- 已运行结果版：
  - `01_LangChain.executed.ipynb`
  - `02-LangChain_executed.ipynb`
  - `一、提示词工程.executed.ipynb`
  - `二、LangChain_RAG.executed.ipynb`
  - `三、RAGcase.executed.ipynb`

