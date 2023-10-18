import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]

text = """You are an expert in Java EAP and Quarkus technologies. You are going to assist with modernizing EAP applications to  
Quarkus 3.4.1, Jakarta EE 9, and Java 11. There are some sample scenarios provided below,

Example 1:
Incident metdata: CDI solution

Issue details:

<dependency>
    <groupId>jakarta.enterprise</groupId>
    <artifactId>jakarta.enterprise.cdi-api</artifactId>
    <scope>provided</scope>
</dependency>

Resolution:

<dependency>
  <groupId>io.quarkus</groupId>
  <artifactId>quarkus-arc</artifactId>
</dependency>

Example 2:
Incident metdata: Producer annotation

Issue details:

@Model
public class MemberController {
    @Produces
    @Named
    private Member newMember;
}

Resolution:

@Model
public class MemberController {
    
    private Member newMember;

    public Member getNewMember() {
        return newMember;
    }
}
"""

# Example code snippet to modernize
java_code_snippet = """
Incident metadata: Stateless scoped bean

Issue details:
```
@Stateless
public class MemberRegistration {
 '....'
 '....'
}
```


"""

prompt =f"""
You have been provided with prior solved examples in #{text}. It is time to resolve a similar incident. Find a solution for the issue in #{java_code_snippet}.
Make sure it is compatible with Quarkus 3.4.1 as well as Jakarta EE 9 and Java 11.

"""
response = get_completion(prompt)
print(response)