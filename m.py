import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

def modernize_code(code_snippet):
    prompt = f"""You are an expert in Java EAP and Quarkus technologies. You are going to assist with modernizing EAP applications to  
    Quarkus 3.4.1, Jakarta EE 9 and Java 11. There are some sample scenarios provided below,
   

Example 1:
Incident metadata: Configuring database. In this case, it is a postgres db.

Issue details:
persistence.xml is present and configured with db details


Resolution:
persistence.xml is optional, hence it is deleted. Application.properties file is updated with the following db details

```
quarkus.hibernate-orm.log.sql=true
quarkus.hibernate-orm.database.generation=drop-and-create

quarkus.datasource.db-kind=postgresql 
quarkus.datasource.username=name
quarkus.datasource.password=pass

quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/dbname
```

Example 2:
Incident metadata: Stateless annotation can be replaced with scope
    Stateless EJBs can be converted to a cdi bean by replacing the `@Stateless` annotation with a scope eg `@ApplicationScoped`

Issue details:
```
@Stateless
public class MemberRegistration {
 '....'
 '....'
}
```

Resolution:
```
@ApplicationScoped
public class MemberRegistration {
 '....'
 '....'
}
```
"""

    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=200, 
        temperature=0,
    )
    
    return response.choices[0].text.strip()

# Example code snippet to modernize
java_code_snippet = """
Incident metdata: Switch to Quarkus' DI solution

Issue details:
The below code is from pom.xml 

```
<dependency>
			<groupId>jakarta.enterprise</groupId>
			<artifactId>jakarta.enterprise.cdi-api</artifactId>
			<scope>provided</scope>
</dependency>
```


"""

code =f"""
You have been provided with prior solved examples. It is time to resolve a similar incident. Find a solution for the issue in #{java_code_snippet}.
Make sure it is compatible with Quarkus 3.4.1 as well as Jakarta EE 9 and Java 11.

"""
modernized_code = modernize_code(java_code_snippet)
print(f"Modernized Code:\n{modernized_code}")