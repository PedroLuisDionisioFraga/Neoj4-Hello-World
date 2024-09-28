from neo4j import GraphDatabase
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
dotenv_path = find_dotenv()
if dotenv_path:
    print(f"Loading .env file from: {dotenv_path}")
else:
    print("No .env file found")

load_dotenv(dotenv_path)

# Access the environment variables
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")

print(f"URI: {uri}")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Database: {database}")

# Neo4j driver initialization
driver = GraphDatabase.driver(uri, auth=(username, password))

# Query functions
def get_family_engineers(tx):
  query = "MATCH (p:Person {profession: 'Engineer'}) RETURN p.name AS name"
  result = tx.run(query)
  return [record["name"] for record in result]

def get_parents_of_person(tx, person_name):
  query = "MATCH (parent)-[:PARENT_OF]->(child:Person {name: $person_name}) RETURN parent.name AS name"
  result = tx.run(query, person_name=person_name)
  return [record["name"] for record in result]

def get_pet_owners(tx, pet_name):
  query = "MATCH (owner)-[:OWNER_OF]->(pet:Pet {name: $pet_name}) RETURN owner.name AS name, pet.name AS pet"
  result = tx.run(query, pet_name=pet_name)
  return [record["name"] for record in result]

def get_children_of_person(tx, person_name):
  query = "MATCH (parent:Person {name: $person_name})-[:PARENT_OF]->(child) RETURN child.name AS name"
  result = tx.run(query, person_name=person_name)
  return [record["name"] for record in result]

def get_pets_of_person(tx, person_name):
  query = "MATCH (owner:Person {name: $person_name})-[:OWNER_OF]->(pet) RETURN pet.name AS name"
  result = tx.run(query, person_name=person_name)
  return [record["name"] for record in result]

def get_people_by_profession(tx, profession):
  query = "MATCH (p:Person {profession: $profession}) RETURN p.name AS name"
  result = tx.run(query, profession=profession)
  return [record["name"] for record in result]

def get_people_by_city(tx, city):
  query = "MATCH (p:Person {city: $city}) RETURN p.name AS name"
  result = tx.run(query, city=city)
  return [record["name"] for record in result]

def get_people_by_pet_type(tx, pet_type):
  query = "MATCH (owner)-[:OWNER_OF]->(pet:Pet {type: $pet_type}) RETURN owner.name AS name"
  result = tx.run(query, pet_type=pet_type)
  return [record["name"] for record in result]

def get_shortest_path_between_people(tx, person1, person2):
  query = """
  MATCH (p1:Person {name: $person1}), (p2:Person {name: $person2}),
        path = shortestPath((p1)-[*]-(p2))
  RETURN path
  """
  result = tx.run(query, person1=person1, person2=person2)
  return [record["path"] for record in result]

def get_people_with_pets_and_professions(tx, pet_type):
  query = """
  MATCH (p:Person)-[:OWNS]->(pet:Pet {type: $pet_type}),
        (p)-[:WORKS_AS]->(profession:Profession)
  RETURN p.name AS name, pet.name AS pet_name, profession.title AS profession
  """
  result = tx.run(query, pet_type=pet_type)
  return [{"name": record["name"], "pet_name": record["pet_name"], "profession": record["profession"]} for record in result]

def get_family_members_within_degree(tx, person, degree):
  query = """
  MATCH (p:Person {name: $person})-[:RELATED_TO*1..$degree]-(relative:Person)
  RETURN relative.name AS relative_name, relative.relation AS relation
  """
  result = tx.run(query, person=person, degree=degree)
  return [{"relative_name": record["relative_name"], "relation": record["relation"]} for record in result]

# Helper function to format the path
def format_path(path):
  nodes = [f"{node['name']} ({node['profession']})" for node in path.nodes]
  return " -> ".join(nodes)

# Example usage
with driver.session(database=database) as session:
  # Query 1: Who in the family is an Engineer?
  engineers = session.execute_write(get_family_engineers)
  print("==========================================================")
  print(f"Family Engineers: {engineers}")

  # Query 2: Who are the parents of Peter?
  parents_of_peter = session.execute_write(get_parents_of_person, "Peter")
  print("==========================================================")
  print(f"Peter's Parents: {parents_of_peter}")
  print("==========================================================")

  # Query 3: Who owns the pet named Rex?
  owners_of_rex = session.execute_write(get_pet_owners, "Rex")
  print(f"Owners of Rex: {owners_of_rex}")
  print("==========================================================")

  # Query 4: Who are the children of John?
  children_of_john = session.execute_write(get_children_of_person, "John")
  print(f"Children of John: {children_of_john}")
  print("==========================================================")

  # Query 5: What pets does Mary own?
  pets_of_mary = session.execute_write(get_pets_of_person, "Mary")
  print(f"Pets of Mary: {pets_of_mary}")
  print("==========================================================")

  # Query 6: Who are the doctors in the family?
  doctors = session.execute_write(get_people_by_profession, "Doctor")
  print(f"Family Doctors: {doctors}")
  print("==========================================================")

  # Query 9: Who owns dogs?
  dog_owners = session.execute_write(get_people_by_pet_type, "Dog")
  print(f"Dog Owners: {dog_owners}")
  print("==========================================================")

  # Query 10: The shortest path between John and Mary
  shortest_path = session.execute_write(get_shortest_path_between_people, "John", "Mary")
  if shortest_path:
    formatted_path = format_path(shortest_path[0])
    print(f"Shortest Path between John and Mary: {formatted_path}")
  else:
    print("No path found between John and Mary.")
  print("==========================================================")

  # Query 11: The shortest path between Clara and Peter
  shortest_path = session.execute_write(get_shortest_path_between_people, "Clara", "Peter")
  if shortest_path:
    formatted_path = format_path(shortest_path[0])
    print(f"Shortest Path between Clara and Peter: {formatted_path}")
  else:
    print("No path found between Clara and Peter.")
  print("==========================================================")

driver.close()
