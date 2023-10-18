import os
import openai

api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

def modernize_code(code_snippet):
    prompt = f"""You are an expert in Java EAP and Quarkus technologies. You are going to assist with modernizing EAP applications to  Quarkus 3.4.1, Jakarta EE 9 and Java 11.
   

Example 1:
Incident metadata: Configure database. In this case, it is a postgres db.

Before change: persistence.xml is present and configured with db details
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.1"
   xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="
        http://xmlns.jcp.org/xml/ns/persistence
        http://xmlns.jcp.org/xml/ns/persistence/persistence_2_1.xsd">
   <persistence-unit name="primary">
      <jta-data-source>java:jboss/datasources/databaseDS</jta-data-source>
      <properties>
         <!-- Properties for Hibernate -->
         <property name="hibernate.dialect" value="org.hibernate.dialect.PostgreSQLDialect"/>
         <property name="hibernate.hbm2ddl.auto" value="create-drop" />
         <property name="hibernate.show_sql" value="false" />
      </properties>
   </persistence-unit>
</persistence>

After change: persistence.xml is optional, hence it is deleted. Application.properties file is updated with the following db details

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
Before change: 
```
@Stateless
public class MemberRegistration {
 '....'
 '....'
}

```
After change:
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
        max_tokens=100, 
        temperature=0,
    )
    
    return response.choices[0].text.strip()

# Example code snippet to modernize
java_code_snippet = """
Incident metdata: Replace javax.enterprise:cdi-api dependency

Before changes:
This is an excerpt from the pom file
```
<dependency>
			<groupId>jakarta.enterprise</groupId>
			<artifactId>jakarta.enterprise.cdi-api</artifactId>
			<scope>provided</scope>
</dependency>
```


"""

code =f"""

Modernize the #{java_code_snippet} to be compatible with Quarkus 3.4.1 as well as Jakarta EE 9 and Java 11.
Provide an after change section with the updated code.
print the response in a json format with keys - before change, after change
"""
modernized_code = modernize_code(java_code_snippet)
print(f"Modernized Code:\n{modernized_code}")