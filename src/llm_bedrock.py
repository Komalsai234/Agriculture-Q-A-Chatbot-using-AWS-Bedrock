from langchain_community.llms.bedrock import Bedrock

def get_llama2_llm(bedrock):
    llm=Bedrock(model_id="meta.llama2-70b-chat-v1",client=bedrock,
                model_kwargs={'max_gen_len':512})
    
    return llm