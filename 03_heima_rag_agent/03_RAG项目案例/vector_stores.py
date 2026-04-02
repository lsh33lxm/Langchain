from langchain_chroma import Chroma
import config_data as config


class VectorStoreService(object):
    def __init__(self, embedding=None):
        # 不传则默认读取配置文件中的 embedding
        self.embedding = embedding or config.get_embedding()

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        """返回向量检索器，方便加入 chain"""
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == '__main__':
    retriever = VectorStoreService().get_retriever()

    res = retriever.invoke("我的体重180斤，尺码推荐")
    print(res)
