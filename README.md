# Family Graph
I'll use a neo4j sandbox.

## Mermaid Graph
```mermaid
graph TD
  %% Nodes
  A["Name: John<br>Gender: Male<br>Age: 55<br>Profession: Engineer<br>Hobby: Playing Guitar"]
  B["Name: Mary<br>Gender: Female<br>Age: 52<br>Profession: Doctor<br>Hobby: Gardening"]
  C["Name: Peter<br>Gender: Male<br>Age: 28<br>Profession: Programmer<br>Hobby: Cycling"]
  D["Name: Anna<br>Gender: Female<br>Age: 25<br>Profession: Designer<br>Hobby: Photography"]
  E["Name: Luke<br>Gender: Male<br>Age: 30<br>Profession: Lawyer<br>Hobby: Cooking"]
  F["Name: Julia<br>Gender: Female<br>Age: 28<br>Profession: Architect<br>Hobby: Painting"]
  G["Name: Rex<br>Gender: Male<br>Age: 3<br>Type: Pet<br>Breed: Dog"]
  H["Name: Luna<br>Gender: Female<br>Age: 4<br>Type: Pet<br>Breed: Cat"]
  I["Name: Charles<br>Gender: Male<br>Age: 60<br>Profession: Teacher<br>Hobby: Fishing"]
  J["Name: Clara<br>Gender: Female<br>Age: 58<br>Profession: Nurse<br>Hobby: Sewing"]

  %% Relationships
  A --|HUSBAND_OF|--> B
  B --|WIFE_OF|--> A
  A --|PARENT_OF|--> C
  A --|PARENT_OF|--> D
  B --|PARENT_OF|--> C
  B --|PARENT_OF|--> D
  C --|SIBLING_OF|--> D
  D --|SIBLING_OF|--> C
  C --|OWNER_OF<br>Property: Since 2020|--> G
  D --|OWNER_OF<br>Property: Since 2021|--> H
  E --|MARRIED_TO|--> F
  F --|MARRIED_TO|--> E
  I --|PARENT_OF|--> A
  J --|PARENT_OF|--> A
```

## Neo4j Graph
![Family Graph](docs/graph.svg)

## Run the Project
1. Clone the repository
```bash
git clone
```
2. Run the cypher script, in `cypher/family_graph.cypher` in the neo4j browser to create the graph.
3. Install the requirements
```bash
pip install -r requirements.txt
```
4. Create a `.env` file running the following script:
  - UNIX/Mac
  ```bash
  ./create_env.sh
  ```
  - Windows
  ```bash
  ./create_env.bat
  ```
5. Edit the `.env` file with your neo4j sandbox credentials, provided when you create an account or new project.
6. Run the project
```bash
python main.py
```
