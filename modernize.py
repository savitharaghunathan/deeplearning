import openai

# Set your OpenAI API key here
api_key = ''
openai.api_key = api_key

def predict_app_modernization(code_example, prompt):
    conversation = f"Code Example:\n{code_example}\n\nQuestion: {prompt}\nAnswer:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        max_tokens=100,  # Adjust the token limit as needed
        temperature=0,
    )
    return response.choices[0].text.strip()

# Example usage
code_example = """ You are an expert in Java EAP and quarkus technologies. Can you predict the modernization code using the following example?
Source Tech:
* EAP 7
* Java 8

Target tech:
* Quarkus 3.4.1
* Java 11

Example 1:
action: Remove persistence.xml and replace with the following

```
quarkus.hibernate-orm.log.sql=true
quarkus.hibernate-orm.database.generation=drop-and-create

quarkus.datasource.db-kind=postgresql 
quarkus.datasource.username=name
quarkus.datasource.password=pass

quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/dbname
```

Example 2:
In Quarkus, the @Stateless bean scope is not a built-in scope. it follows a different approach to bean scopes, and the equivalent of a stateless bean is implemented using other CDI (Contexts and Dependency Injection) scopes, such as @RequestScoped, @ApplicationScoped, or @Dependent.
@ApplicationScoped is most common used replacement for @Stateless scope

Action: Replace @Stateless with @ApplicationScoped

Example 3:
Replace javax packages with jakarta wherever applicable
replace the following 
```
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;
```
with
```
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
```
"""



prompt = """What should be changed in the below code block to successfully modernize it to quarkus  3.4.1 and java 11?

```
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
```

"""

answer = predict_app_modernization(code_example, prompt)
print(f"AI's Answer: {answer}")