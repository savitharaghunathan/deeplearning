import semantic_kernel as sk
from semantic_kernel.connectors.ai.hugging_face import HuggingFaceTextCompletion

kernel = sk.Kernel()

kernel.add_text_completion_service("huggingface", HuggingFaceTextCompletion("gpt2", task="text-generation"))

print("You made an open source kernel using an open source AI model!")

sk_prompt = """
{{$input}}

Summarize the content above in less than 140 characters.
"""
summary_function = kernel.create_semantic_function(prompt_template = sk_prompt,
                                                    description="Summarizes the input to length of an old tweet.",
                                                    max_tokens=200,
                                                    temperature=0.1,
                                                    top_p=0.5)       
print("A semantic function for summarization has been registered.")

sk_input = """
Let me illustrate an example. Many weekends, I drive a few minutes from my house to a local pizza store to buy 
a slice of Hawaiian pizza from the gentleman that owns this pizza store. And his pizza is great, but he always 
has a lot of cold pizzas sitting around, and every weekend some different flavor of pizza is out of stock. 
But when I watch him operate his store, I get excited, because by selling pizza, he is generating data. 
And this is data that he can take advantage of if he had access to AI.

AI systems are good at spotting patterns when given access to the right data, and perhaps an AI system could spot 
if Mediterranean pizzas sell really well on a Friday night, maybe it could suggest to him to make more of it on a 
Friday afternoon. Now you might say to me, "Hey, Andrew, this is a small pizza store. What's the big deal?" And I 
say, to the gentleman that owns this pizza store, something that could help him improve his revenues by a few 
thousand dollars a year, that will be a huge deal to him.
""";
# Text source: https://www.ted.com/talks/andrew_ng_how_ai_could_empower_any_business/transcript

summary_result = summary_function(sk_input)

print(summary_result)