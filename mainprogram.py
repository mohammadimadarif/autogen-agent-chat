import autogen
import ollama  # Add this import

# Verify local model availability
try:
    ollama.show('llama2')  # Check if model exists
except ollama.ResponseError as e:
    print(f"Error: {e.error}\nRun: ollama pull llama2")

# Configure Ollama
config_list = [{
    "model": "tinyllama",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama"
}]

llm_config = {
    "timeout": 1200,
    "cache_seed": 42,
    "config_list": config_list,
    "temperature": 0.3,
}

# Create agents
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=3,
    code_execution_config={"work_dir": "web",
                            "use_docker": False
                          },
    llm_config=llm_config,
)

# Test with simple query first
user_proxy.initiate_chat(
    assistant,
    message="What is 2+2?"  # Simple test before complex tasks
)
