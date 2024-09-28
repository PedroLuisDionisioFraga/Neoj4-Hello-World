CREATE (john:Person {name: "John", gender: "Male", age: 55, profession: "Engineer", hobby: "Playing Guitar"});
CREATE (mary:Person {name: "Mary", gender: "Female", age: 52, profession: "Doctor", hobby: "Gardening"});
CREATE (peter:Person {name: "Peter", gender: "Male", age: 28, profession: "Programmer", hobby: "Cycling"});
CREATE (anna:Person {name: "Anna", gender: "Female", age: 25, profession: "Designer", hobby: "Photography"});
CREATE (luke:Person {name: "Luke", gender: "Male", age: 30, profession: "Lawyer", hobby: "Cooking"});
CREATE (julia:Person {name: "Julia", gender: "Female", age: 28, profession: "Architect", hobby: "Painting"});
CREATE (charles:Person {name: "Charles", gender: "Male", age: 60, profession: "Teacher", hobby: "Fishing"});
CREATE (clara:Person {name: "Clara", gender: "Female", age: 58, profession: "Nurse", hobby: "Sewing"});

CREATE (rex:Pet {name: "Rex", gender: "Male", age: 3, type: "Dog", breed: "Labrador"});
CREATE (luna:Pet {name: "Luna", gender: "Female", age: 4, type: "Cat", breed: "Persian"});

MATCH (john:Person {name: "John"}), (mary:Person {name: "Mary"})
CREATE (john)-[:HUSBAND_OF]->(mary),
       (mary)-[:WIFE_OF]->(john);

MATCH (john:Person {name: "John"}), (peter:Person {name: "Peter"}), (anna:Person {name: "Anna"})
CREATE (john)-[:PARENT_OF]->(peter),
       (john)-[:PARENT_OF]->(anna);

MATCH (mary:Person {name: "Mary"}), (peter:Person {name: "Peter"}), (anna:Person {name: "Anna"})
CREATE (mary)-[:PARENT_OF]->(peter),
       (mary)-[:PARENT_OF]->(anna);

MATCH (peter:Person {name: "Peter"}), (anna:Person {name: "Anna"})
CREATE (peter)-[:SIBLING_OF]->(anna),
       (anna)-[:SIBLING_OF]->(peter);

MATCH (peter:Person {name: "Peter"}), (rex:Pet {name: "Rex"})
CREATE (peter)-[:OWNER_OF {since: 2020}]->(rex);

MATCH (anna:Person {name: "Anna"}), (luna:Pet {name: "Luna"})
CREATE (anna)-[:OWNER_OF {since: 2021}]->(luna);

MATCH (luke:Person {name: "Luke"}), (julia:Person {name: "Julia"})
CREATE (luke)-[:MARRIED_TO]->(julia),
       (julia)-[:MARRIED_TO]->(luke);

MATCH (charles:Person {name: "Charles"}), (john:Person {name: "John"})
CREATE (charles)-[:PARENT_OF]->(john);

MATCH (clara:Person {name: "Clara"}), (john:Person {name: "John"})
CREATE (clara)-[:PARENT_OF]->(john);
