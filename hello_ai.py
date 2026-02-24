from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def chat_with_local_llm(user_message: str) -> str:
    """
    与本地大模型对话
    
    Args:
        user_message: 用户输入的消息
        
    Returns:
        AI的回复
    """
    try:
        # 创建客户端（连接本地LM Studio）
        client = OpenAI(
            base_url=os.getenv("LOCAL_LLM_BASE_URL"),
            api_key=os.getenv("LOCAL_LLM_API_KEY")
        )
        
        # 发送对话请求
        response = client.chat.completions.create(
            model=os.getenv("LOCAL_LLM_MODEL"),
            messages=[
                {
                    "role": "system", 
                    "content": "你是一个友好的AI助手，擅长用简洁清晰的方式回答问题。"
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # 提取回复内容
        ai_reply = response.choices[0].message.content
        return ai_reply
        
    except Exception as e:
        return f"发生错误：{str(e)}\n\n请确保：\n1. LM Studio已启动\n2. 已加载模型\n3. 服务器正在运行"


def main():
    """主函数"""
    print("=" * 50)
    print("🤖 Hello AI World - 第一个AI程序")
    print("=" * 50)
    print()
    
    # 测试消息
    test_messages = [
        "你好！请介绍一下你自己",
        "用一句话解释什么是AI大模型",
        "Python和Java哪个更适合AI开发？"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n【测试 {i}】")
        print(f"我：{message}")
        print(f"AI：", end="", flush=True)
        
        # 调用AI
        reply = chat_with_local_llm(message)
        print(reply)
        print("-" * 50)
    
    print("\n✅ 环境配置成功！你已经完成了第一个AI程序！")
    print("\n🎉 接下来可以开始真正的AI学习之旅了！")


if __name__ == "__main__":
    main()
